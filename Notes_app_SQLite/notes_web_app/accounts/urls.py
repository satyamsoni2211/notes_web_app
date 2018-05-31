from django.conf.urls import url
from . import views
from django.contrib.auth import views as authviews
from rest_framework.authtoken import views as authtoken_view
from django.views.decorators.csrf import csrf_exempt
from notes.api.views import CustomAuthToken
# from rest_framework_jwt.views import obtain_jwt_token

app_name = 'accounts'

urlpatterns = [
    url('^signup/$', views.SignUp.as_view(), name='signup'),
    url(r'^login/$', authviews.LoginView.as_view(template_name='accounts/login_temp.html'), name='login'),
    url(r'^logout/$', authviews.LogoutView.as_view(), name='logout'),
    url(r'^password_reset/$', authviews.password_reset, name='password_reset',
        kwargs={'template_name': 'registration/password_reset_form.html'}),
    url(r'^password_reset/done/$', authviews.password_reset_done,
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        authviews.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', authviews.password_reset_complete,
        name='password_reset_complete'),
    url(r'^api-token-auth/', csrf_exempt(CustomAuthToken.as_view())),
    #  url(r'^api-token-auth/', obtain_jwt_token),
]
