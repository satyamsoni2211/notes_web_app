from django.views import generic

class Welcome(generic.TemplateView):
    template_name = 'welcome.html'

class SuccessfulRegistration(generic.TemplateView):
    template_name = 'success.html'