from django.conf.urls import url
from emp.employees import views

urlpatterns = [
    url(r'^employees/$', views.employee_list),
    url(r'^employees/(?P<pk>[0-9]+)/$', views.employee_detail),
]