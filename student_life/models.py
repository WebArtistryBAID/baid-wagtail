from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.search import index
from wagtail.images.blocks import ImageChooserBlock
from wagtail.api import APIField
from baid.api import ImageUrlField


class Activity(models.Model):
    page = ParentalKey("StudentLife", related_name="activities")
    name = models.CharField(default="", max_length=50)
    content = RichTextField(default="")
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    panels = [
        FieldPanel("name"),
        FieldPanel("content"),
        FieldPanel("image"),
    ]

    api_fields = [
        APIField("name"),
        APIField("content"),
        APIField("image"),
    ]


class Club(models.Model):
    page = ParentalKey("StudentLife", related_name="clubs")

    name = models.CharField(default="", max_length=50)
    content = RichTextField(default="")
    icon = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    images = StreamField(
        [
            ("image", ImageChooserBlock()),
        ],
        use_json_field=True,
        null=True,
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("icon"),
        FieldPanel("content"),
        FieldPanel("images"),
    ]

    api_fields = [
        APIField("name"),
        APIField("icon"),
        APIField("content"),
        APIField("images"),
    ]


class StudentLife(Page):
    carousel_images = StreamField(
        [
            ("image", ImageChooserBlock()),
        ],
        use_json_field=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("carousel_images"),
        InlinePanel("activities", heading="Activities", min_num=6, max_num=6),
        InlinePanel("clubs", heading="Clubs", min_num=1),
    ]

    api_fields = [
        APIField("carousel_images", serializer=ImageUrlField()),
        APIField("activities"),
        APIField("clubs"),
    ]
