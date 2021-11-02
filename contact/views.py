from django.views import generic
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib.auth.models import User


# Create your views here.
class ContactView(generic.FormView):
    template_name = 'contact/index.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.save()

        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        subject = f'{name} contacted you!'
        recipient_list = [user.email for user in User.objects.filter(is_staff=True)]

        try:
            send_mail(subject=subject, message=message, from_email=email, recipient_list=recipient_list)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        messages.success(self.request, 'Thank you. We will be in touch soon.')

        return super(ContactView, self).form_valid(form)
