from django.contrib import admin

from .models import Document

class DocumentAdmin(admin.ModelAdmin):
    exclude = []

admin.site.register(Document, DocumentAdmin)
