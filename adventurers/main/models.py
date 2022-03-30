from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мероприятия'
        verbose_name_plural = 'Мероприятия'



class Story(models.Model):
    chapter = models.CharField('Глава', max_length=50)
    date = models.CharField('Дата', max_length=50)
    Story_text = models.TextField('Описание событий')

    def __str__(self):
        return self.date

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'История'