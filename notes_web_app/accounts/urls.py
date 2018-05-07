from django.conf.urls import url
from . import views
from django.contrib.auth import views as authviews

app_name = 'accounts'

urlpatterns = [
    url('^signup/$',views.SignUp.as_view(),name='signup'),
    url(r'^login/$',authviews.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    url(r'^logout/$',authviews.LogoutView.as_view(),name='logout'),
]
