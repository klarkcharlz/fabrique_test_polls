from django.db import models


# Create your models here.
class Polls(models.Model):
    """Опросы"""
    name = models.CharField(verbose_name="Название опроса", max_length=50)
    description = models.TextField(verbose_name="Описание опроса")
    start_date = models.DateTimeField(verbose_name="Дата начала опроса",auto_now=True, editable=False)
    finish_date = models.DateTimeField(verbose_name="Дата окончания опроса")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"
        ordering = ["start_date"]


class Questions(models.Model):
    """Вопросы"""
    types = {"Text": "Ответ текстом",
             "one options": "Один вариант ответа",
             "few options": "Несколько вариантов ответа"}
    poll = models.ForeignKey('Polls', on_delete=models.CASCADE, verbose_name="Опрос")
    type = models.CharField(verbose_name="Тип вопроса", choices=types.items(), max_length=50)
    text = models.TextField(verbose_name="Текст вопроса")

    def __str__(self):
        return f"{self.poll}: {self.text[:50]}"

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        ordering = ['poll']


class CompetedPoll(models.Model):
    """Пройденные опросы"""
    user_id = models.IntegerField(verbose_name="Уникальный ID пользователя")
    answer = models.CharField(max_length=150, verbose_name="Ответ")
    poll = models.ManyToManyField('Polls', verbose_name="Опрос", related_name="polls_name")
    question = models.ManyToManyField('Questions', verbose_name="Вопрос", related_name="questions_text")

    class Meta:
        verbose_name = "Пройденный опрос"
        verbose_name_plural = "Пройденные опросы"
