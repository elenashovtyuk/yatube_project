from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField('Название группы',
                             help_text='Максимум 200 символов', max_length=200)
    slug = models.SlugField('уникальный адрес',
                            help_text='Обязательное поле.', unique=True)
    description = models.TextField('Описание сообщества')

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField('Tекст поста')
    pub_date = models.DateTimeField('Дата и время', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Имя автора'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Сообщество'
    )

    class Meta:
        ordering = ('-pub_date',)
