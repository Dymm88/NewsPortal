from django.shortcuts import render, redirect, reverse
from django.template.loader import render_to_string
from django.views import View
from django.core.mail import EmailMultiAlternatives
from datetime import datetime

from NewsPortal.secret_keys import MY_EMAIL
from .models import Appointment


class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        html_content = render_to_string(
            'appointment_created.html',
            {
                'appointment': appointment,
            }
        )
        msg = EmailMultiAlternatives(
            subject=f'{appointment.client_name}'
                    f'{appointment.date.strftime("%Y-%m-%d")}',
            body=appointment.message,
            from_email=MY_EMAIL,
            to=[],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return redirect('appointments:make appointment')
