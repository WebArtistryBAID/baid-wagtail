from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.api import APIField

# Create your models here.

class StudentLife(Page):
    activities_title = models.CharField(default="", max_length=50)
    activities_sub_title_1 = models.CharField(default="", max_length=50)
    activities_content_1 = RichTextField(default="")
    activities_sub_title_2 = models.CharField(default="", max_length=50)
    activities_content_2 = RichTextField(default="")
    activities_sub_title_3 = models.CharField(default="", max_length=50)
    activities_content_3 = RichTextField(default="")
    activities_sub_title_4 = models.CharField(default="", max_length=50)
    activities_content_4 = RichTextField(default="")
    activities_sub_title_5 = models.CharField(default="", max_length=50)
    activities_content_5 = RichTextField(default="")
    activities_sub_title_6 = models.CharField(default="", max_length=50)
    activities_content_6 = RichTextField(default="")

    clubs_title = models.CharField(default="", max_length=50)
    clubs_sub_title_1 = models.CharField(default="", max_length=50)
    clubs_content_1 = RichTextField(default="")
    clubs_sub_title_2 = models.CharField(default="", max_length=50)
    clubs_content_2 = RichTextField(default="")
    clubs_sub_title_3 = models.CharField(default="", max_length=50)
    clubs_content_3 = RichTextField(default="")
    clubs_sub_title_4 = models.CharField(default="", max_length=50)
    clubs_content_4 = RichTextField(default="")
    clubs_sub_title_5 = models.CharField(default="", max_length=50)
    clubs_content_5 = RichTextField(default="")
    clubs_sub_title_6 = models.CharField(default="", max_length=50)
    clubs_content_6 = RichTextField(default="")

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('activities_title'),
        index.SearchField('activities_sub_title_1'),
        index.SearchField('activities_content_1'),
        index.SearchField('activities_sub_title_2'),
        index.SearchField('activities_content_2'),
        index.SearchField('activities_sub_title_3'),
        index.SearchField('activities_content_3'),
        index.SearchField('activities_sub_title_4'),
        index.SearchField('activities_content_4'),
        index.SearchField('activities_sub_title_5'),
        index.SearchField('activities_content_5'),
        index.SearchField('activities_sub_title_6'),
        index.SearchField('activities_content_6'),
        index.SearchField('clubs_title'),
        index.SearchField('clubs_sub_title_1'),
        index.SearchField('clubs_content_1'),
        index.SearchField('clubs_sub_title_2'),
        index.SearchField('clubs_content_2'),
        index.SearchField('clubs_sub_title_3'),
        index.SearchField('clubs_content_3'),
        index.SearchField('clubs_sub_title_4'),
        index.SearchField('clubs_content_4'),
        index.SearchField('clubs_sub_title_5'),
        index.SearchField('clubs_content_5'),
        index.SearchField('clubs_sub_title_6'),
        index.SearchField('clubs_content_6'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('title'),
        FieldPanel('activities_title'),
        FieldPanel('activities_sub_title_1'),
        FieldPanel('activities_content_1'),
        FieldPanel('activities_sub_title_2'),
        FieldPanel('activities_content_2'),
        FieldPanel('activities_sub_title_3'),
        FieldPanel('activities_content_3'),
        FieldPanel('activities_sub_title_4'),
        FieldPanel('activities_content_4'),
        FieldPanel('activities_sub_title_5'),
        FieldPanel('activities_content_5'),
        FieldPanel('activities_sub_title_6'),
        FieldPanel('activities_content_6'),
        FieldPanel('clubs_title'),
        FieldPanel('clubs_sub_title_1'),
        FieldPanel('clubs_content_1'),
        FieldPanel('clubs_sub_title_2'),
        FieldPanel('clubs_content_2'),
        FieldPanel('clubs_sub_title_3'),
        FieldPanel('clubs_content_3'),
        FieldPanel('clubs_sub_title_4'),
        FieldPanel('clubs_content_4'),
        FieldPanel('clubs_sub_title_5'),
        FieldPanel('clubs_content_5'),
        FieldPanel('clubs_sub_title_6'),
        FieldPanel('clubs_content_6'),
    ]

    api_fields = [
        APIField('title'),
        APIField('activities_title'),
        APIField('activities_sub_title_1'),
        APIField('activities_content_1'),
        APIField('activities_sub_title_2'),
        APIField('activities_content_2'),
        APIField('activities_sub_title_3'),
        APIField('activities_content_3'),
        APIField('activities_sub_title_4'),
        APIField('activities_content_4'),
        APIField('activities_sub_title_5'),
        APIField('activities_content_5'),
        APIField('activities_sub_title_6'),
        APIField('activities_content_6'),
        APIField('clubs_title'),
        APIField('clubs_sub_title_1'),
        APIField('clubs_content_1'),
        APIField('clubs_sub_title_2'),
        APIField('clubs_content_2'),
        APIField('clubs_sub_title_3'),
        APIField('clubs_content_3'),
        APIField('clubs_sub_title_4'),
        APIField('clubs_content_4'),
        APIField('clubs_sub_title_5'),
        APIField('clubs_content_5'),
        APIField('clubs_sub_title_6'),
        APIField('clubs_content_6'),
    ]