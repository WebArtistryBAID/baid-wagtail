# Create your models here.
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.search import index

from baid.api import ImageUrlField


class NewsIndex(Page):
    pass


class News(Page):
    # Lang is a multi selection field
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    cover = models.ImageField(null=True)
    body = RichTextField()

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro"),
        FieldPanel("cover"),
        FieldPanel("body"),
    ]

    api_fields = [
        APIField("intro"),
        APIField("date"),
        APIField("cover", serializer=ImageUrlField()),
        APIField("body"),
        APIField("title"),
    ]
