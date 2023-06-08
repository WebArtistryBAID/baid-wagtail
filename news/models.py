from django.db import models

# Create your models here.
from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField


class NewsIndex(Page):
    pass


class News(Page):
    # Lang is a multi selection field
    lang = models.CharField(default="zh", max_length=2)

    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("lang"),
        FieldPanel("date"),
        FieldPanel("intro"),
        FieldPanel("body"),
    ]

    api_fields = [
        APIField("intro"),
        APIField("lang"),
        APIField("date"),
        APIField("body"),
        APIField("title"),
    ]
