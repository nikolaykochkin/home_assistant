from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


class User(AbstractUser):
    pass


class Task(models.Model):
    name = models.CharField(
        max_length=200, verbose_name='наименование', db_index=True)
    executor = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='исполнитель', related_name='+', db_index=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='+', verbose_name='автор')
    description = models.TextField(verbose_name='описание', blank=True)
    active = models.BooleanField(verbose_name='активно', default=True)
    done = models.BooleanField(verbose_name='сделано', default=False)
    start_date = models.DateTimeField(verbose_name='дата начала')
    end_date = models.DateTimeField(
        verbose_name='дата окончания', null=True, blank=True)
    start_time = models.TimeField(
        verbose_name='время начала', null=True, blank=True)
    everyday = models.BooleanField(verbose_name='каждый день')
    day_of_month = models.IntegerField(
        verbose_name='день месяца',
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(31)])
    monday = models.BooleanField(verbose_name='понедельник')
    tuesday = models.BooleanField(verbose_name='вторник')
    wednesday = models.BooleanField(verbose_name='среда')
    thursday = models.BooleanField(verbose_name='четверг')
    friday = models.BooleanField(verbose_name='пятница')
    saturday = models.BooleanField(verbose_name='суббота')
    sunday = models.BooleanField(verbose_name='воскресенье')
    created = models.DateTimeField(
        verbose_name='дата создания', auto_now_add=True)
    changed = models.DateTimeField(
        verbose_name='дата изменения', auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('scheduler:task', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'
