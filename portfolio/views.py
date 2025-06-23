
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .forms import ContactForm

def home_view(request):
    """
    This view handles both displaying the page and processing the form submission.
    """
    if request.method == 'POST':
        # If the form is submitted, process the data
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get the clean data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Prepare email content
            subject = f'New Contact Form Submission from {name}'
            
            html_message = render_to_string('portfolio/email_template.html', {
                'name': name,
                'email': email,
                'message': message,
            })
            
            plain_message = f"You have a new message from {name} ({email}):\n\n{message}"

            # Send the email
            try:
                send_mail(
                    subject,
                    plain_message, # Fallback for email clients that don't support HTML
                    settings.EMAIL_HOST_USER, # From email
                    [settings.EMAIL_HOST_USER], # To email (sending to yourself)
                    html_message=html_message # The pretty HTML version
                )
                # Set a success message to display on the page
                context = {'form': ContactForm(), 'success_message': 'Thank you! Your message has been sent.'}
                return render(request, 'portfolio/index.html', context)

            except Exception as e:
                # If email fails, show an error message
                # In a real app, you would log this error `print(e)`
                context = {'form': form, 'error_message': 'Sorry, there was an error sending your message. Please try again.'}
                return render(request, 'portfolio/index.html', context)

    else:
        # If it's a GET request, just display the page with a blank form
        form = ContactForm()

    context = {'form': form}
    return render(request, 'portfolio/index.html', context)
