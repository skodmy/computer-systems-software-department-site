
from django.contrib import admin
from django.db import models

from ckeditor.widgets import CKEditorWidget

from students.models import Year_of_accession, Year_of_study, Course, Students


class Year_of_accessionAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

class Year_of_studyAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

class CourseAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

class StudentsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


admin.site.register(Year_of_accession, Year_of_accessionAdmin)
admin.site.register(Year_of_study, Year_of_studyAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Students, StudentsAdmin)