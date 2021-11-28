from django.contrib import admin
from .models import Comment, Post, PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PhoneNumberField: {'widget': PhoneNumberInternationalFallbackWidget},
    }


admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)
