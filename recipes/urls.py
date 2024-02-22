from django.urls import path
from recipes.views import myusers, contact


urlpatterns = [
    
    path('', myusers),
    path('contact/', contact)
]
