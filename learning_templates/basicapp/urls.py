from django.urls import path
from basicapp import views

# TEMPLATE TAGGING
# this is what allows Django to use template tagging to map differnet url to basicapp
app_name = 'basicapp'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other')
]
