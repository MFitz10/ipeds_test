from decimal import Decimal
from django.forms import widgets
from rest_framework import serializers
from dashboard.models import CIPFamily
from universities.models import (UnivBaseTable, DegreesbyMajorEthnicity, 
        DegreesbyEthnicity, GraduationRates4Yr, InstitutionalChars, USNWR,
        AppFlowRate, AWARD_LEVEL_CHOICES)
from universities.fields import CustomChoiceField

CIP_FAMILY_CHOICES = list(CIPFamily.objects.values_list('code','description')) + [(99,'Grand Total')]

class CustomModelSerializer(serializers.ModelSerializer):
    serializer_choice_field = CustomChoiceField

class DynamicFieldsSerializer(serializers.Serializer):
    """
    A Serializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class AwardsDetailsSerializer(CustomModelSerializer):
    class Meta:
        model = DegreesbyMajorEthnicity

class GradRateSerializer(CustomModelSerializer):
    class Meta:
        model = GraduationRates4Yr
        fields = ('bachdegrees_100','bach_gradrate_100','bachdegrees_150','bach_gradrate_150','bachdegrees_200','bach_gradrate_200')

class DemogSerializer(CustomModelSerializer):
    class Meta:
        model = DegreesbyEthnicity
        fields = ('cs_grand_tot','cs_tot_male','cs_tot_female')

class InstCharsSerializer(CustomModelSerializer):
    accept_rate = serializers.SerializerMethodField()

    def get_accept_rate(self, obj):
        try:
            app_rate = round(obj.admssn/obj.applcn * 100,1)
        except TypeError:
            app_rate = 100

        return app_rate

    class Meta:
        model = InstitutionalChars
        fields = ('accept_rate','applcn','admssn','satvr25','satvr75','satmt25',
                  'satmt75','satwr25','satwr75','actcm25','actcm75')

class AwardsDetailsCountsSerializer(DynamicFieldsSerializer):
    cip_family = CustomChoiceField(choices=CIP_FAMILY_CHOICES)
    awlevel = CustomChoiceField(choices=AWARD_LEVEL_CHOICES)
    aian_male_degrees = serializers.IntegerField()
    aian_female_degrees = serializers.IntegerField()
    asian_male_degrees = serializers.IntegerField()
    asian_female_degrees = serializers.IntegerField()
    black_male_degrees = serializers.IntegerField()
    black_female_degrees = serializers.IntegerField()
    hispanic_male_degrees = serializers.IntegerField()
    hispanic_female_degrees = serializers.IntegerField()
    nhpi_male_degrees = serializers.IntegerField()
    nhpi_female_degrees = serializers.IntegerField()
    biracial_male_degrees = serializers.IntegerField()
    biracial_female_degrees = serializers.IntegerField()
    unknown_male_degrees = serializers.IntegerField()
    unknown_female_degrees = serializers.IntegerField()
    white_male_degrees = serializers.IntegerField()
    white_female_degrees = serializers.IntegerField()

class AppFlowRateSerializer(CustomModelSerializer):
    class Meta:
        model = AppFlowRate
        fields = ('app_on','app_off','qual_on','qual_off','bqual_on',
                'bqual_off','hire_on','hire_off')

class UniversitiesDetailsSerializer(serializers.Serializer):
    gradrate = GradRateSerializer()
    awardsdetailscounts = serializers.SerializerMethodField()
    school_name = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    rank = serializers.SerializerMethodField()
    app_flow_rates = AppFlowRateSerializer()
    main_web = serializers.CharField()
    instchars = InstCharsSerializer()

    def get_awardsdetailscounts(self, obj):
        fields = self.context.get('awardsdetails_fields', 
                ['cip_family','awlevel'])
        serializer = AwardsDetailsCountsSerializer(obj.awardsdetailscounts, 
                many=True, fields=fields)
        return serializer.data

    def get_rank(self, obj):
        try:
            return obj.rank.rank
        except:
            return None

    class Meta:
        model = UnivBaseTable
        fields = ('school_name','city','state','gradrate','awardsdetailscounts','instchars')

class UniversitiesListSerializer(serializers.Serializer):
    unitid = serializers.ReadOnlyField()
    school_name = serializers.ReadOnlyField()
    latitude = serializers.ReadOnlyField()
    longitude = serializers.ReadOnlyField()
    degree_count = serializers.ReadOnlyField()
    potential_hires = serializers.ReadOnlyField()
    affiliation = serializers.SerializerMethodField()

    def get_affiliation(self, obj):
        try:
            return obj.affiliation.affiliation
        except:
            return 'none'

    class Meta:
        model = UnivBaseTable
        fields = ('unitid','school_name','latitude','longitude','degree_count')

