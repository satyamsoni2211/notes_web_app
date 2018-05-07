from django.views import generic

class Welcome(generic.TemplateView):
    template_name = 'welcome.html'

class Loggedin(generic.TemplateView):
    template_name = 'loggedin.html'

class Loggedout(generic.TemplateView):
    template_name = 'loggedout.html'

class SuccessfulRegistration(generic.TemplateView):
    template_name = 'success.html'