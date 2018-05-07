from django.conf.urls import url
from . import views

app_name = 'notes'

urlpatterns = [
    url(r'^create/',views.CreateNotes.as_view(),name='create'),
    url(r'^view/$',views.ViewNotes.as_view(),name='all'),
    url(r'^update/(?P<pk>\d+)/$',views.UpdateNotes.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.DeleteNotes.as_view(),name='delete'),
    url(r'^sharenotes/$',views.sharenotes,name='sharenote'),
    url(r'sharesingle/(?P<pk>\d+)/$',views.sharesingle,name='sharesingle'),
    url(r'^shared_with_me/$',views.SharedWithMe.as_view(),name='sharedwithmenotes'),
    url(r'^shared_by_me/$',views.SharedByMe.as_view(),name='sharedbymenotes'),
]