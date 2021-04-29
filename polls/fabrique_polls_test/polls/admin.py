from django.contrib import admin
from .models import Polls, Questions  # импортировали нашу модель


# Register your models here.
admin.site.register(Polls)
admin.site.register(Questions)
