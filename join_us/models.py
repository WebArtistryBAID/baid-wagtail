from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.api import APIField

# Create your models here.

class JoinUs(Page):
    join = models.CharField(default="", max_length=50)
    
    student_title = models.CharField(default="", max_length=50)
    student_content = RichTextField(default="")
    student_join = models.CharField(default="", max_length=50)

    faculty_title = models.CharField(default="", max_length=50)
    faculty_content = RichTextField(default="")
    faculty_join = models.CharField(default="", max_length=50)

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('join'),
        index.SearchField('student_title'),
        index.SearchField('student_content'),
        index.SearchField('student_join'),
        index.SearchField('faculty_title'),
        index.SearchField('faculty_content'),
        index.SearchField('faculty_join'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('title'),
        FieldPanel('join'),
        FieldPanel('student_title'),
        FieldPanel('student_content'),
        FieldPanel('student_join'),
        FieldPanel('faculty_title'),
        FieldPanel('faculty_content'),
        FieldPanel('faculty_join'),
    ]

    api_fields = [
        APIField('title'),
        APIField('join'),
        APIField('student_title'),
        APIField('student_content'),
        APIField('student_join'),
        APIField('faculty_title'),
        APIField('faculty_content'),
        APIField('faculty_join'),
    ]