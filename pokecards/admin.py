from django.contrib import admin

from .models import Card, CardInstance, GameState


admin.site.register(Card)
admin.site.register(CardInstance)
admin.site.register(GameState)


# @admin.register(CardInstance)
# class CardInstanceAdmin(admin.ModelAdmin):
#     list_display = ('card', 'owner', 'id')
#
#
# class CardInstanceInline(admin.TabularInline):
#     model = CardInstance
#
#
# @admin.register(Card)
# class CardAdmin(admin.ModelAdmin):
#     list_display = ('character')
#     inlines = [CardInstanceInline]
