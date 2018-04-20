from decimal import Decimal
from django.db.models import ExpressionWrapper, F, FloatField, Sum
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, pagination
from rest_framework.response import Response

from universities.models import (UnivBaseTable, DegreesbyMajorEthnicity, 
        DegreesbyEthnicity, GraduationRates4Yr, ETHNICITY_CHOICES, GENDER_CHOICES)
from universities.serializers import UniversitiesDetailsSerializer,\
UniversitiesListSerializer, AwardsDetailsSerializer, DemogSerializer, GradRateSerializer


# helper function for generating sql expression to filter by major/cip family
def majors_sql_expr(majors_str):
        majors_list = []
        majors_expr = 'FLOOR("CIPCODE") IN ('
        for maj in majors_str.split(','):
            majors_list.append(int(maj))
            majors_expr += '%s,'
        majors_expr = majors_expr[:-1] + ')'
        return majors_expr, majors_list

class UniversitiesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns IPEDS data at a summary level for a list of universities or at a 
    detailed level for a specific university.
    """
    queryset = UnivBaseTable.objects.all()

    def list(self, request):
        # get query parameters
        location = self.request.query_params.get('location', None)
        levels = self.request.query_params.get('level')
        majors = self.request.query_params.get('major', None)
        gender = self.request.query_params.get('gender', None)
        ethnicity = self.request.query_params.get('ethnicity', None)

        # filter by states
        if location:
            location_list = location.split(',')
            self.queryset = self.queryset.filter(state__in=location_list)

        # get education levels by which to filter
        levels_list = [1,3,5,7,17,18,19] # codes for all educ. levels we wish to show
        if levels is not None:
            levels_list = levels.split(',')
            levels_list = [int(lev) for lev in levels_list]

        # get majors by which to filter
        if majors is not None:
            majors_expr, majors_list = majors_sql_expr(majors)
        else:
            majors_list = [99] # 99 is code for all majors
            majors_expr = '"CIPCODE" = %s'

        # get columns to aggregate to get total # of degrees matching query
        f_cols = []

        if gender is not None and ethnicity is not None:
            ethnicity_list = ethnicity.split(',')
            gender_list = gender.split(',')
            for eth in ethnicity_list:
                for g in gender_list:
                    f_cols.append('awardsdetails__c_' + eth + '_' + g)

        elif ethnicity is not None:
            ethnicity_list = ethnicity.split(',')
            for eth in ethnicity_list:
                f_cols.append('awardsdetails__c_tot_' + eth)

        elif gender is not None:
            gender_list = gender.split(',')
            for g in gender_list:
                f_cols.append('awardsdetails__total_' + g + '_degrees')

        else:
            f_cols.append('awardsdetails__total_degrees')

        # add up Django F expressions (columns) to get total degree count
        f_expr = None
        for f in f_cols:
            if not f_expr:
                f_expr = F(f)
            else:
                f_expr = f_expr + F(f)

        try:
            # get and order queryset of all schools with some value for degree count
            # NOTE: inclusion of 2nd majors may result in double counting of graduates
            schools = self.queryset.extra(where=[majors_expr,], params=majors_list # filter by majors
                    ).filter(awardsdetails__awlevel__in=levels_list, # filter by educ. level
                            app_flow_rates__gt=0
                            ).annotate(degree_count=Sum(f_expr), # add degree counts
                                    ).filter(degree_count__gt=0,app_flow_rates__gte=0 # only include values > 0
                                            ).select_related('app_flow_rates', 'affiliation') # add fields in query
            # add potential hires
            schools = schools.annotate(potential_hires=
                    ExpressionWrapper(F('app_flow_rates__hire_on')*F('degree_count'),
                        output_field=FloatField()),
                    ).order_by('-degree_count')
        except:
            raise Http404('Invalid query parameter.')
        
        # page = self.paginate_queryset(schools)
        # if page is not None:
        #     serializer = UniversitiesListSerializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
    
        serializer = UniversitiesListSerializer(schools, many=True)

        # add total degrees
        total_degrees = dict((sch['unitid'], sch['total_degrees']) for sch in 
            DegreesbyMajorEthnicity.objects.filter(cipcode=99,
                awlevel__in=[1,3,5,7,17,18,19]).values('unitid').annotate(
                        total_degrees=Sum('total_degrees')))

        data = serializer.data
        for sch in data:
            sch['total_degrees'] = total_degrees[sch['unitid']]

        return Response(data)

    def retrieve(self, request, pk=None):
        # get school queryset
        school = get_object_or_404(self.queryset, pk=pk)

        # default values for each query param
        levels_list = [1,3,5,7,17,18,19] # codes for all educ. levels we wish to show
        majors_list = [99] # 99 is the total (not major-specific)
        majors_expr = '"CIPCODE" = %s'
        ethnicity_list = [eth[0] for eth in ETHNICITY_CHOICES]
        gender_list = [g[0] for g in GENDER_CHOICES]
        cols_dict = {}

        # get query parameters
        levels = self.request.query_params.get('level')
        majors = self.request.query_params.get('major', None)
        gender = self.request.query_params.get('gender', None)
        ethnicity = self.request.query_params.get('ethnicity', None)

        if levels is not None:
            levels_list = levels.split(',')

        if majors is not None:
            majors_expr, majors_list = majors_sql_expr(majors)

        if ethnicity is not None:
            ethnicity_list = ethnicity.split(',')

        if gender is not None:
            gender_list = gender.split(',')

        # create dict of ethnicity/gender columsn for which to include degree counts
        for eth in ethnicity_list:
            for g in gender_list:
                cols_dict[eth + '_' + g + '_degrees'] = Sum('c_' + eth + '_' + g)

        # get degree counts
        try:
            # NOTE: inclusion of 2nd majors may result in double counting of graduates
            school.awardsdetailscounts = school.awardsdetails.extra(
                            where=[majors_expr,], params=majors_list,
                            select={'cip_family': 'FLOOR("CIPCODE")::INT'} # get cip family
                    ).filter(awlevel__in=levels_list # filter by major/cip
                    # group by cip family and award level 
                    ).values('cip_family','awlevel').annotate(
                            # sum up other columns
                            **cols_dict
                    ).order_by('cip_family','awlevel')
        except:
            raise Http404('Error retrieving school info.')

        awardsdetails_fields = ['cip_family','awlevel'] + list(cols_dict.keys())
        serializer = UniversitiesDetailsSerializer(school, 
                context={'awardsdetails_fields': awardsdetails_fields})

        # reformat awardsdetailscounts data to flatten for each awlevel/cip_family/ethnicity/gender combo
        formatted_data = serializer.data
        formatted_awardsdetailscounts = []
        total_degrees = 0
        for cip_awlevel_dict in serializer.data['awardsdetailscounts']:
            flat_data = []
            cip_family = cip_awlevel_dict['cip_family']
            awlevel = cip_awlevel_dict['awlevel']
            for key, val in cip_awlevel_dict.items():
                if key != 'cip_family' and key != 'awlevel' and val > 0:
                    ethnicity, gender, degrees = key.split('_')
                    data_dict = {}
                    data_dict['cip_family'] = cip_family
                    data_dict['awlevel'] = awlevel
                    data_dict['ethnicity'] = ethnicity
                    data_dict['gender'] = gender
                    data_dict['degrees'] = val
                    total_degrees += val
                    flat_data.append(data_dict)
            formatted_awardsdetailscounts += flat_data
        formatted_data['awardsdetailscounts'] = formatted_awardsdetailscounts
        formatted_data['total_degrees'] = total_degrees

        # add applicant flow counts
        app_flow_counts = {}
        for key, val in formatted_data['app_flow_rates'].items():
            app_flow_counts[key] = Decimal(val) * Decimal(total_degrees)
        formatted_data['app_flow_counts'] = app_flow_counts

        return Response(formatted_data)     

class AwardsDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DegreesbyMajorEthnicity.objects.all()
    serializer_class = AwardsDetailsSerializer

class DemogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DegreesbyEthnicity.objects.all()
    serializer_class = DemogSerializer

class GradRateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GraduationRates4Yr.objects.all()
    serializer_class = GradRateSerializer
