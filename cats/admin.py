from django.contrib import admin
from .models import Cat, Paint

class PaintInline(admin.StackedInline):
    model = Paint

class CatAdmin(admin.ModelAdmin):
    inlines = [PaintInline,]

admin.site.register(Cat,CatAdmin)
admin.site.register(Paint)

