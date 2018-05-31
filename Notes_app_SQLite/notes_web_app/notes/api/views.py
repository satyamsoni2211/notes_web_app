from rest_framework import generics
from rest_framework.decorators import api_view, renderer_classes
from .serializers import NotesSerializer
from notes.models import Notes
from django.contrib.auth import get_user_model
from rest_framework import mixins
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
# from braces.views import CsrfExemptMixin
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from rest_framework_jwt.views import ObtainJSONWebToken
# from rest_framework.authtoken.models import Token
from rest_framework_jwt.settings import api_settings


User = get_user_model()


class CustomAuthToken(ObtainJSONWebToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']


        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        # request.session['token'] = token
        resp = Response({
            'token': token,
            'user_id': user.pk,
            'email': user.email
        })
        resp.set_cookie('token', token)
        return resp


class NotesListView(generics.ListAPIView):  # ,mixins.CreateModelMixin
    serializer_class = NotesSerializer
    model = Notes

    def get_queryset(self):
        # qs = super(NotesListView, self).get_queryset()
        qs = Notes.objects.filter(
            user__username__iexact=self.request.user.username)
        return qs
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

# class UpdateNotes(generics.UpdateAPIView,mixins.RetrieveModelMixin):
#     serializer_class = NotesSerializer
#     model = Notes

#     def list(self, request):
#         queryset = Notes.objects.get(pk=self.kwargs.get(pk))
#         serializer = NotesSerializer(queryset)
#         return response(serializer.data)


@api_view(['GET', 'POST'])
@renderer_classes((JSONRenderer,))
def UpdateViewNotes(request, pk=None):
    Note = Notes.objects.get(pk=pk)
    serialized_data = NotesSerializer(Note)
    obj = {'Notes': 'Please use post method to update Notes'}
    for k, v in serialized_data.data.items():
        obj[k] = v
    if request.method == 'POST':
        print(request.data)
        if request.data.get('text', None):
            Note.text = request.data['text']
            Note.save()
            serialized_data = NotesSerializer(Note)
            return Response(serialized_data.data)
        else:
            return Response({'Error': 'Not a valid Json'})
    return Response(obj)


@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def CreateNote(request):
    if request.method == 'POST':
        user = request.user
        title = request.data.get('title')
        text = request.data.get('text')
        note = Notes.objects.create(title=title, user=user, text=text)
        note.save()
        serializer = NotesSerializer(note)
        return Response(serializer.data)
