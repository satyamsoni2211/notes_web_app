from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=2000)
    user = models.ForeignKey(User,related_name='notes')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notes:all')

    class Meta:
        ordering = ['-created']

class SharedNotes(models.Model):
    note = models.ForeignKey(Notes,related_name='shared_note')
    user = models.ForeignKey(User,related_name='shared_user')
    shared_by = models.CharField(max_length=30,null=True)
    shared_on = models.DateTimeField(auto_now=True)
    can_edit = models.BooleanField(default=False)

    class Meta:
        unique_together = ('note','user')

    def __str__(self):
        return self.note.title

    def get_absolute_url(self):
        return reverse('notes:all')