from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.api import APIField


class Home(Page):
    head = models.CharField(default="", max_length=50)
    introduction_title = models.CharField(default="", max_length=50)
    introduction = RichTextField(default="")
    read_more = models.CharField(default="了解更多", max_length=50)

    education_philosophy_title = models.CharField(default="", max_length=50)

    motto_title = models.CharField(default="", max_length=50)
    motto_content = models.CharField(default="", max_length=50)
    spirit_title = models.CharField(default="", max_length=50)
    spirit_content = models.CharField(default="", max_length=50)
    key_competency_title = models.CharField(default="", max_length=50)
    key_competency_content = models.CharField(default="", max_length=50)
    cultivation_title = models.CharField(default="", max_length=50)
    cultivation_content = models.CharField(default="", max_length=50)

    principal_message = models.CharField(default="", max_length=50)
    principal_name = models.CharField(default="", max_length=50)

    meet_baid_title = models.CharField(default="", max_length=50)
    admission_results_title = models.CharField(default="", max_length=50)
    admission_results_content = RichTextField(default="")

    news_title = models.CharField(default="", max_length=50)

    search_fields = Page.search_fields + [
        index.SearchField('head'),
        index.SearchField('introduction_title'),
        index.SearchField('introduction'),
        index.SearchField('education_philosophy_title'),
        index.SearchField('motto_title'),
        index.SearchField('motto_content'),
        index.SearchField('spirit_title'),
        index.SearchField('spirit_content'),
        index.SearchField('key_competency_title'),
        index.SearchField('key_competency_content'),
        index.SearchField('cultivation_title'),
        index.SearchField('cultivation_content'),
        index.SearchField('principal_message'),
        index.SearchField('principal_name'),
        index.SearchField('meet_baid_title'),
        index.SearchField('admission_results_title'),
        index.SearchField('admission_results_content'),
        index.SearchField('news_title'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("head"),
        FieldPanel("introduction_title"),
        FieldPanel("introduction"),
        FieldPanel("read_more"),
        FieldPanel("education_philosophy_title"),
        FieldPanel("motto_title"),
        FieldPanel("motto_content"),
        FieldPanel("spirit_title"),
        FieldPanel("spirit_content"),
        FieldPanel("key_competency_title"),
        FieldPanel("key_competency_content"),
        FieldPanel("cultivation_title"),
        FieldPanel("cultivation_content"),
        FieldPanel("principal_message"),
        FieldPanel("principal_name"),
        FieldPanel("meet_baid_title"),
        FieldPanel("admission_results_title"),
        FieldPanel("admission_results_content"),
        FieldPanel("news_title"),
    ]

    api_fields = [
        APIField("head"),
        APIField("introduction_title"),
        APIField("introduction"),
        APIField("read_more"),
        APIField("education_philosophy_title"),
        APIField("motto_title"),
        APIField("motto_content"),
        APIField("spirit_title"),
        APIField("spirit_content"),
        APIField("key_competency_title"),
        APIField("key_competency_content"),
        APIField("cultivation_title"),
        APIField("cultivation_content"),
        APIField("principal_message"),
        APIField("principal_name"),
        APIField("meet_baid_title"),
        APIField("admission_results_title"),
        APIField("admission_results_content"),
        APIField("news_title"),
    ]
