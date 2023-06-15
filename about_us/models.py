from django.db import models

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index
from wagtail.api import APIField
from modelcluster.fields import ParentalKey


# Create your models here.


class Alumnus(models.Model):
    page = ParentalKey("AboutUs", related_name="alumni")

    name = models.CharField(default="", max_length=50)
    content = RichTextField(default="")
    image = models.ImageField(upload_to="alumni/", default="")

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


class AboutUs(Page):
    overview_title = models.CharField(default="", max_length=50)
    overview_content = RichTextField(default="")

    alumni_title = models.CharField(default="", max_length=50)
    # alumni = models.ManyToManyField(Alumni)

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

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("overview_title"),
                FieldPanel("overview_content"),
            ],
            heading="Overview",
        ),
        MultiFieldPanel(
            [
                FieldPanel("alumni_title"),
                InlinePanel("alumni"),
            ],
            heading="Alumni",
        ),
        MultiFieldPanel(
            [
                FieldPanel("accreditation_title"),
                FieldPanel("accreditation_content"),
            ],
            heading="Accreditation",
        ),
        MultiFieldPanel(
            [
                FieldPanel("data_title"),
                FieldPanel("data_sub_title_1"),
                FieldPanel("data_content_1"),
                FieldPanel("data_sub_title_2"),
                FieldPanel("data_content_2"),
                FieldPanel("data_sub_title_3"),
                FieldPanel("data_content_3"),
                FieldPanel("data_sub_title_4"),
                FieldPanel("data_content_4"),
            ],
            heading="Data",
        ),
    ]

    api_fields = [
        APIField("title"),
        APIField("overview_title"),
        APIField("overview_content"),
        APIField("alumni_title"),
        APIField("alumni"),
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
