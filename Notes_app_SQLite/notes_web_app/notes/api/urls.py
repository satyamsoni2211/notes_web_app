from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^list/$',views.NotesListView.as_view(),name='notes-list'),
    url(r'^Notes/(?P<pk>\d+)/$',views.UpdateViewNotes,name='update-notes'),
    url(r'^create/$',views.CreateNote,name='create-note'),
]