from django.contrib import admin

from .models import Question, Serie, Acteur, Genre, Plateform, Realisateur

admin.site.register(Question)
admin.site.register(Serie)
admin.site.register(Acteur)
admin.site.register(Genre)
admin.site.register(Plateform)
admin.site.register(Realisateur)