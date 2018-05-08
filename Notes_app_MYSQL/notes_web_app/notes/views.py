from django.shortcuts import render
from .models import Notes,SharedNotes
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse,reverse_lazy
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from . import forms



# Create your views here.

class CreateNotes(LoginRequiredMixin,generic.CreateView):
    model = Notes
    form_class = forms.MyModelForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class ViewNotes(LoginRequiredMixin,generic.ListView):
    model = Notes


class DeleteNotes(LoginRequiredMixin,generic.DeleteView):
    model = Notes
    success_url = reverse_lazy('notes:all')


class UpdateNotes(LoginRequiredMixin,generic.UpdateView):
    model = Notes
    form_class = forms.MyModelForm
    template_name = 'notes/notes_update_form.html'
    success_url = reverse_lazy('notes:all')

class SharedWithMe(LoginRequiredMixin,generic.ListView):
    model = SharedNotes

    def get_queryset(self):
        User = get_user_model()
        try:
            self.shared_notes = SharedNotes.objects.filter(user__username__iexact=self.request.user.username)
        except User.DoesNotExist:
            raise Http404
        else:
            return self.shared_notes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shared_notes'] = self.shared_notes
        return context

class SharedByMe(LoginRequiredMixin,generic.ListView):
    model = SharedNotes
    template_name = 'notes/sharedbyme_list.html'

    def get_queryset(self):
        User = get_user_model()
        try:
            self.shared_notes = SharedNotes.objects.filter(shared_by__iexact=self.request.user.username)
        except User.DoesNotExist:
            raise Http404
        else:
            return self.shared_notes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shared_notes'] = self.shared_notes
        return context

@login_required
def sharenotes(request): #To choose among available notes
    notes = Notes.objects.filter(user__username__iexact=request.user.username)

    if request.method == 'POST':
        pk = request.POST.get('note')
        username = request.POST.get('user')
        edit = True if request.POST.get('can_edit') else False
        try:
            share = SharedNotes(note=Notes.objects.get(pk=pk), user=User.objects.get(username__iexact=username),
                                can_edit=edit, shared_by=request.user.username)
            share.save()
            messages.success(request,'Note shared successfully with {}'.format(username))
        except IntegrityError as e:
            messages.error(request,'You have already shared this Note with {}'.format(username))
        return render(request,'notes/share_success.html')
    return render(request,'notes/sharednotes_form.html',{'notes':notes,
                                                         'users':User.objects.exclude(username__iexact=request.user.username)})

@login_required
def sharesingle(request,pk=None): #if you want to share a single note

    if request.method == 'POST':
        pk = request.POST.get('note')
        username = request.POST.get('user')
        edit = True if request.POST.get('can_edit') else False
        # print(pk)
        try:
            share = SharedNotes(note=Notes.objects.get(pk=pk), user=User.objects.get(username__iexact=username),
                                can_edit=edit,shared_by=request.user.username)
            share.save()
            messages.success(request,'Note shared successfully')
        except IntegrityError as e:
            messages.error(request,'You can\'t share post with same user Twice')
        return render(request,'notes/share_success.html')
    return render(request,'notes/share_single.html',{'users':User.objects.exclude(username__iexact=request.user.username),
                                                     'note': Notes.objects.get(pk=pk)})