from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.api import APIField


# Create your models here.

class AboutUs(Page):
    overview_title = models.CharField(default="", max_length=50)
    overview_content = RichTextField(default="")

    alumni_title = models.CharField(default="", max_length=50)
    alumni_name_1 = models.CharField(default="", max_length=50)
    alumni_content_1 = RichTextField(default="")
    alumni_name_2 = models.CharField(default="", max_length=50)
    alumni_content_2 = RichTextField(default="")
    alumni_name_3 = models.CharField(default="", max_length=50)
    alumni_content_3 = RichTextField(default="",)

    accreditation_title = models.CharField(default="", max_length=50)
    accreditation_content = RichTextField(default="")

    data_title = models.CharField(default="", max_length=50)
    data_sub_title_1 = models.CharField(default="", max_length=50)
    data_content_1 = models.CharField(default="", max_length=50)
    data_sub_title_2 = models.CharField(default="", max_length=50)
    data_content_2 = models.CharField(default="", max_length=50)
    data_sub_title_3 = models.CharField(default="", max_length=50)
    data_content_3 = models.CharField(default="", max_length=50)
    data_sub_title_4 = models.CharField(default="", max_length=50)
    data_content_4 = models.CharField(default="", max_length=50)

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('overview_title'),
        index.SearchField('overview_content'),
        index.SearchField('alumni_title'),
        index.SearchField('alumni_name_1'),
        index.SearchField('alumni_content_1'),
        index.SearchField('alumni_name_2'),
        index.SearchField('alumni_content_2'),
        index.SearchField('alumni_name_3'),
        index.SearchField('alumni_content_3'),
        index.SearchField('accreditation_title'),
        index.SearchField('accreditation_content'),
        index.SearchField('data_title'),
        index.SearchField('data_sub_title_1'),
        index.SearchField('data_content_1'),
        index.SearchField('data_sub_title_2'),
        index.SearchField('data_content_2'),
        index.SearchField('data_sub_title_3'),
        index.SearchField('data_content_3'),
        index.SearchField('data_sub_title_4'),
        index.SearchField('data_content_4'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("title"),
        FieldPanel("overview_title"),
        FieldPanel("overview_content"),
        FieldPanel("alumni_title"),
        FieldPanel("alumni_name_1"),
        FieldPanel("alumni_content_1"),
        FieldPanel("alumni_name_2"),
        FieldPanel("alumni_content_2"),
        FieldPanel("alumni_name_3"),
        FieldPanel("alumni_content_3"),
        FieldPanel("accreditation_title"),
        FieldPanel("accreditation_content"),
        FieldPanel("data_title"),
        FieldPanel("data_sub_title_1"),
        FieldPanel("data_content_1"),
        FieldPanel("data_sub_title_2"),
        FieldPanel("data_content_2"),
        FieldPanel("data_sub_title_3"),
        FieldPanel("data_content_3"),
        FieldPanel("data_sub_title_4"),
        FieldPanel("data_content_4"),
    ]

    api_fields = [
        APIField("title"),
        APIField("overview_title"),
        APIField("overview_content"),
        APIField("alumni_title"),
        APIField("alumni_name_1"),
        APIField("alumni_content_1"),
        APIField("alumni_name_2"),
        APIField("alumni_content_2"),
        APIField("alumni_name_3"),
        APIField("alumni_content_3"),
        APIField("accreditation_title"),
        APIField("accreditation_content"),
        APIField("data_title"),
        APIField("data_sub_title_1"),
        APIField("data_content_1"),
        APIField("data_sub_title_2"),
        APIField("data_content_2"),
        APIField("data_sub_title_3"),
        APIField("data_content_3"),
        APIField("data_sub_title_4"),
        APIField("data_content_4"),
    ]


