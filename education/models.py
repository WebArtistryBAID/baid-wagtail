from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.api import APIField
from baid.api import ImageUrlField


class LearningMethod(models.Model):
    page = ParentalKey("Education", related_name="learning_methods")

    title = models.CharField(default="", max_length=50)
    content = RichTextField(default="")
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("content"),
        FieldPanel("image"),
    ]

    api_fields = [
        APIField("title"),
        APIField("content"),
        APIField("image"),
    ]


class Curriculum(models.Model):
    page = ParentalKey("Education", related_name="curriculums")

    name = models.CharField(default="", max_length=50)
    content = RichTextField(default="")


class Education(Page):
    carousel_images = StreamField(
        [
            ("image", ImageChooserBlock()),
        ],
        use_json_field=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("carousel_images"),
        InlinePanel("curriculums", heading="Curriculums"),
        InlinePanel("learning_methods", heading="Learning Methods"),
    ]

    api_fields = [
        APIField("carousel_images", serializer=ImageUrlField()),
        APIField("curriculums"),
        APIField("learning_methods"),
    ]
