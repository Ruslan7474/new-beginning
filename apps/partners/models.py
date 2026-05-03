from django.db import models


class Partner(models.Model):
    title = models.CharField(verbose_name="Название", max_length=100)
    link = models.CharField(
        max_length=255, verbose_name="Ссылка на партнера",
        help_text="Ссылка на сайт или ссылка на инстаграм или что то еще"
    )
    logo = models.ImageField(upload_to='partners/')

    def __str__(self):
        return f"{self.title} {self.link}"
    
    class Meta:
        verbose_name="партнер"
        verbose_name_plural="Партнеры"