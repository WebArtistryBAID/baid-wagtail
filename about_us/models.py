from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.api import APIField
from modelcluster.fields import ParentalKey
from wagtail.images.blocks import ImageChooserBlock
from baid.api import ImageUrlField


class Alumnus(models.Model):
    """
    Alumnus information
    """

    page = ParentalKey("AboutUs", related_name="alumni")

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
        APIField("image", serializer=ImageUrlField()),
    ]


class Stat(models.Model):
    """
    Statistical data about school
    Example: Student-faculty ratio
    """

    page = ParentalKey("AboutUs", related_name="data")

    name = models.CharField(default="", max_length=50)
    content = models.CharField(default="", max_length=50)

    api_fields = [APIField("name"), APIField("content")]


class AboutUs(Page):
    carousel_images = StreamField(
        [
            ("image", ImageChooserBlock()),
        ],
        use_json_field=True,
        null=True,
    )

    overview = RichTextField(default="")

    accreditation = RichTextField(default="")

    content_panels = Page.content_panels + [
        FieldPanel("carousel_images"),
        FieldPanel("overview"),
        InlinePanel("alumni", heading="Alumni"),
        FieldPanel("accreditation"),
        InlinePanel("data", heading="Data"),
    ]

    api_fields = [
        APIField("carousel_images", serializer=ImageUrlField()),
        APIField("overview"),
        APIField("alumni"),
        APIField("accreditation"),
        APIField("data"),
    ]
