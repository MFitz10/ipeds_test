from itertools import groupby
import json

from dashboard.models import CIPFamily, Job
from universities.models import (ETHNICITY_CHOICES, GENDER_CHOICES, 
    AWARD_LEVEL_CHOICES, STATE_ABBR)

# Create your views here.
from django.shortcuts import render_to_response

def main(request):

    # get input values

    # get levels to show on front end
    levels = [(val, descr) for val, descr in AWARD_LEVEL_CHOICES if val in [1,3,5,7,17,18,19]]

    # get all majors (CIP code families) mapped to jobs
    majors = CIPFamily.objects.values('code', 'description')

    # get all jobs mapped to json list of majors (CIP code families)
    jobs_qs = Job.objects.values('description', 'cip__cip_family')
    jobs_qs = sorted(jobs_qs, key=lambda x: x['description'])
    jobs = []
    for job_description, group in groupby(jobs_qs, lambda x: x['description']):
        # make a string of comma-separated cip code families for each job
        cip_codes = ','.join([str(result['cip__cip_family']) for result in 
            group if result['cip__cip_family']])
        # add job description and json version of cip codes list to the jobs list
        jobs.append((job_description, cip_codes))

    # get json objects
    stem_json = json.dumps(list(CIPFamily.objects.filter(stem=True).values_list(
        'code', flat=True)))
    genders_json = json.dumps(dict(GENDER_CHOICES))
    ethnicities_json = json.dumps(dict(ETHNICITY_CHOICES))

    inputs_dict = {
            'locations': STATE_ABBR,
            'levels': levels,
            'genders': GENDER_CHOICES,
            'ethnicities': ETHNICITY_CHOICES,
            'majors': majors,
            'jobs': jobs,
            'stem_majors_json': stem_json,
            'genders_json': genders_json,
            'ethnicities_json': ethnicities_json,
    }
    return render_to_response('dashboard/main.html', inputs_dict)
