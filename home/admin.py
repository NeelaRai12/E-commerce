import slug as slug
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Slider)
admin.site.register(Brand)
admin.site.register(Item)

admin.site.register(Contact)
admin.site.register(ContactInformation)
admin.site.register(Cart)
admin.site.register(Review)
admin.site.register(Blog)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("title","status","slug","author")
admin.site.register(Post, AuthorAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("post","name","email","publish","status")
    list_filter = ("status","publish")
    search_fields = ("name","email","content")
admin.site.register(Comment, CommentAdmin)














