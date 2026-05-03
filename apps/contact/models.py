from django.db import models


class ContactPage(models.Model):
    map = models.TextField()
    title = models.CharField(max_length=100)
    desc = models.TextField()
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Инфо контактов'
        verbose_name = 'инфа контакта'


class ContactRequest(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.email}"
    
    class Meta:
        verbose_name_plural = 'Сообщение с сайта'
        verbose_name = 'сообщение с сайта'
