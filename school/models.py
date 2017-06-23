from django.db import models
from django.utils import timezone
from django.utils.encoding import smart_unicode

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField(blank=True,default=None,null=True)
    def __unicode__(self):
        return smart_unicode(self.name) 

class College(models.Model):
    school = models.ForeignKey(School)
    name = models.CharField(max_length=100)
    info = models.TextField(blank=True,default=None,null=True)
    def __unicode__(self):
        return smart_unicode(self.name) 
        
class Professional(models.Model):
    college = models.ForeignKey(College)
    name = models.CharField(max_length=100)
    info = models.TextField(blank=True,default=None,null=True)
    def __unicode__(self):
        return smart_unicode(self.name) 