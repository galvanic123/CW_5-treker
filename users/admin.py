from django.contrib import admin

from users.models import CustomsUser


@admin.register(CustomsUser)
class UserAdmin(admin.ModelAdmin):
    list_filter = ("id", "email")
