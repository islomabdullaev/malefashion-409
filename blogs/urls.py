from django.urls import path
from blogs.views import blog_details

app_name = "blogs"

urlpatterns = [
    path('post/<int:pk>/', blog_details, name='details')
]