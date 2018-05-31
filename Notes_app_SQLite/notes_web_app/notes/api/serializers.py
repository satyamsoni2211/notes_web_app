from rest_framework import serializers
from notes.models import Notes

# from rest_framework import

class NotesSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ['id','title','text','created','user']
        model = Notes
        read_only_fields = ['user']
        