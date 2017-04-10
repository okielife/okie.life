from django.contrib import admin

from .models import Person, Publication, Education, Experience, Skill

# Register your models here.
admin.site.register(Person)
admin.site.register(Publication)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
