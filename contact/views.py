from django.views import generic
from django.contrib import messages
from .forms import ContactForm


# Create your views here.
class ContactView(generic.FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you. We will be in touch soon.')

        return super(ContactView, self).form_valid(form)
