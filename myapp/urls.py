from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.home,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('services/',views.services,name='services'),
    path('blog/',views.blog,name='blog'),
    path('products/',views.products,name='products')

    ]