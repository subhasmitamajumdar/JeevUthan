from django.contrib import admin

# Register your models here.
from .models import Pet
from .models import User
class UserAdmin(admin.ModelAdmin):
    list_display = ['__unicode__','timestamp','updated']
    class Meta:
        model=User
admin.site.register(User,UserAdmin)

admin.site.register(Pet)