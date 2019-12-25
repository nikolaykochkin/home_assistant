from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


class User(AbstractUser):
    pass


class Task(models.Model):
    name = models.CharField(
        max_length=200, verbose_name='задача', db_index=True)
    description = models.TextField(verbose_name='что делать', blank=True)
    executor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='кто делает',
        related_name='+',
        db_index=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='+',
        verbose_name='автор',
        null=True,
        blank=True)
    due_date = models.DateTimeField(
        verbose_name='когда', null=True, blank=True)
    active = models.BooleanField(verbose_name='активно', default=True)
    done = models.BooleanField(verbose_name='сделано', default=False)
    notify = models.BooleanField(verbose_name='уведомлять', default=False)
    start_date = models.DateTimeField(verbose_name='с', null=True, blank=True)
    end_date = models.DateTimeField(
        verbose_name='по', null=True, blank=True)
    start_time = models.TimeField(
        verbose_name='время начала', null=True, blank=True)
    scheduled = models.BooleanField(
        verbose_name='по расписанию', default=False)
    day_of_month = models.IntegerField(
        verbose_name='день месяца',
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(31)])
    monday = models.BooleanField(verbose_name='пн')
    tuesday = models.BooleanField(verbose_name='вт')
    wednesday = models.BooleanField(verbose_name='ср')
    thursday = models.BooleanField(verbose_name='чт')
    friday = models.BooleanField(verbose_name='пт')
    saturday = models.BooleanField(verbose_name='сб')
    sunday = models.BooleanField(verbose_name='вс')
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
