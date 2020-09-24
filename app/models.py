from django.db import models


class Portfolio(models.Model):
    img = models.ImageField(null=True, blank=True, upload_to='static/portfolio')
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=40)
    email = models.CharField(verbose_name='Почта', max_length=100)
    subject = models.CharField(max_length=40, default=None, blank=True, null=True)
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.email
