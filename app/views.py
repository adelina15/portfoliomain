from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Portfolio
import telebot
from .forms import ContactForm
from django.views import View

bot = telebot.TeleBot('1154411457:AAHb5pk3IhsIstQezqc4tJZGbvadXKoJvgk')


def index(request):
    portfolio = Portfolio.objects.all()
    form = ContactForm()
    return render(request, 'app/index.html', {'port': portfolio, 'form': form})


class ContactView(View):
    def post(self, request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
        # print(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data['email']
                name = form.cleaned_data['name']
                message = form.cleaned_data['message']
                subject = 'Новая заявка на подписку!'
                from_email = 'adelina.aidarbekova@gmail.com'
                to_email = ['adelina.aidarbekova@gmail.com']
                message1 = 'Новая заявка!' + '\r\n' + '\r\n' + 'Почта: ' + email + '\r\n' + '\r\n' + 'Имя:' + name + '\r\n' + 'Коммент' + message
                send_mail(subject, message, from_email, to_email, fail_silently=False)
                bot.send_message(626292575, message1)
        return redirect('home')
