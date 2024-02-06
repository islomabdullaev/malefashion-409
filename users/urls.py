from django.urls import path
from users.views import signin, signup, signout

app_name = "users"

urlpatterns = [
    path('signin/', signin, name="signin"),
    path('signup/', signup, name="signup"),
    path('signout/', signout, name="signout")
]