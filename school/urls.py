from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'schooldata/$',views.schooldata,name='schooldata'),
    url(r'collegedata/$',views.collegedata,name='collegedata'),
    url(r'professionaldata/$',views.professionaldata,name='professionaldata'),
]
