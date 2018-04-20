from django.db import models

from universities.models import UnivBaseTable

AFFILIATION_CHOICES = (
        ('onsite', 'On-Campus'),
        ('offsite', 'Virtual'),
        ('none', 'No Affiliation'),
)

class Job(models.Model):
    code = models.CharField(db_column='JobCode', max_length=10, primary_key=True)
    description = models.CharField(db_column='JobDescription', max_length=1000)

    class Meta:
        managed = False
        db_table = 'Jobs'
        ordering = ['description']

class CIPFamily(models.Model):
    code = models.IntegerField(db_column='CIPFamily', primary_key=True)
    description = models.CharField(db_column='Name', max_length=1000)
    stem = models.BooleanField(db_column='Stem', default=False)

    class Meta:
        managed = False
        db_table = 'CIPFamily'
        ordering = ['description']

class JobCIP(models.Model):
    job_code = models.ForeignKey('Job', db_column='JobCode', related_name='cip')
    cip_family = models.ForeignKey('CIPFamily', db_column='CIPFamily', related_name='job')

    class Meta:
        managed = False
        db_table = 'JobCIP'
        ordering = ['job_code__description']

class Affiliation(models.Model):
    unitid = models.OneToOneField(UnivBaseTable, db_column='UNITID', verbose_name='School', related_name='affiliation')
    affiliation = models.CharField(max_length=50, db_column='Affiliation', choices=AFFILIATION_CHOICES)

    def __str__(self):
        return self.unitid.school_name

    class Meta:
        managed = False
        db_table = 'affiliation'
        ordering = ['unitid__school_name']
        verbose_name = 'school recruiting affiliation'
