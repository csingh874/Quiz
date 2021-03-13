from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class AdminQtsAnsSet(ImportExportModelAdmin):
    pass

admin.site.register(QtsAnsSet,AdminQtsAnsSet)
