from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path('all/', views.reaStudentAll, name = 'stuAll'),
    path('reg/', views.regStudent, name = 'reg'),
    path('regCon/', views.regConStudent, name = 'regCon'),
    path('<str:student_name>/det', views.detStudent, name = 'stuDet'),
    path('<str:student_name>/mod', views.modStudent, name = 'mod'),
    path('modCon/', views.modConStudent, name='modCon'),
    path('<str:student_name>/del', views.delStudent, name = 'del')
]