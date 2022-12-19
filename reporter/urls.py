from django.urls import path
from .views import HomePageView, airport_dataset

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    #path('incidence/', HomePageView.as_view(), name='incidence'),
    path('airport/', airport_dataset, name='airport'),
]
