from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import School,College,Professional

import json
# Create your views here.
@csrf_exempt
def schooldata(request):
    schoolname = request.GET.get('name')
    school = School.objects.filter(name=schoolname)
    if school:
        school = school[0]
        return HttpResponse(json.dumps({
            'action':'schooldata',
            'result':'succeed',
            'info':json.dumps(school.info,ensure_ascii=False,indent=2),
        })) 
    else:
        return HttpResponse(json.dumps({
            'action':'schooldata',
            'result':'error',
            'info':'SchoolDoNotExist',
        })) 


@csrf_exempt
def collegedata(request):
    name = request.GET.get('name')
    school = request.GET.get('school')
    school = School.objects.filter(name=school)
    if not school:
        return HttpResponse(json.dumps({
            'action':'schooldata',
            'result':'error',
            'info':'SchoolDoNotExist',
        })) 
    school = school[0]
    college = College.objects.filter(name=name,school=school)
    if college:
        college = college[0]
        return HttpResponse(json.dumps({
            'action':'collegedata',
            'result':'succeed',
            'info':json.dumps(college.info,ensure_ascii=False,indent=2),
        })) 
    else:
        return HttpResponse(json.dumps({
            'action':'collegedata',
            'result':'error',
        })) 

@csrf_exempt
def professionaldata(request):
    school = request.GET.get('school')
    school = School.objects.filter(name=school)
    if not school:
        return HttpResponse(json.dumps({
            'action':'professionaldata',
            'result':'error',
            'info':'SchoolDoNotExist',
        })) 
    school = school[0]
    college = request.GET.get('college')
    college = College.objects.filter(name=college,school=school)
    if not college:
        return HttpResponse(json.dumps({
            'action':'professionaldata',
            'result':'error',
            'info':'CollegeDoNotExist',
        })) 
    college = college[0]
    name = request.GET.get('name')
    professional = Professional.objects.filter(name=name,college=college)
    if not professional:
        return HttpResponse(json.dumps({
            'action':'professionaldata',
            'result':'error',
            'info':'ProfessionalDoNotExist',
        })) 
    professional = professional[0]
    return HttpResponse(json.dumps({
        'action':'professionaldata',
        'result':'succeed',
        'info':json.dumps(professional.info,ensure_ascii=False,indent=2),
    }))
