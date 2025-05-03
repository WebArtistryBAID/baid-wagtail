from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.admin.panels import InlinePanel
from wagtail.api import APIField
from wagtail.fields import RichTextField
from wagtail.models import Page

from baid.api import ImageUrlField


class AboutPageOverviewItem(models.Model):
    page = ParentalKey("AboutPage", related_name="overview_items")
    text = RichTextField()

    panels = [
        FieldPanel("text"),
    ]

    api_fields = [
        APIField("text"),
    ]


class AboutPageStatistic(models.Model):
    page = ParentalKey("AboutPage", related_name="statistics")
    name = models.CharField(max_length=32)
    content = models.CharField(max_length=32)

    panels = [
        FieldPanel("name"),
        FieldPanel("content"),
    ]

    api_fields = [
        APIField("name"),
        APIField("content"),
    ]


class AboutPageAccreditation(models.Model):
    page = ParentalKey("AboutPage", related_name="accreditations")
    name = models.CharField(max_length=32)
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        related_name="+",
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("image"),
    ]

    api_fields = [
        APIField("name"),
        APIField("image", serializer=ImageUrlField()),
    ]


class AboutPageAlumnus(models.Model):
    page = ParentalKey("AboutPage", related_name="alumni")
    name = models.CharField(max_length=32)
    content = RichTextField()
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        related_name="+",
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


class AboutPage(Page):
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,

        related_name='+',
    )

    top_title = models.CharField(max_length=32)
    top_text = RichTextField()

    overview_title = models.CharField(max_length=32)

    statistics_title = models.CharField(max_length=32)

    accreditation_title = models.CharField(max_length=32)
    accreditation_text = RichTextField()

    alumni_title = models.CharField(max_length=32)

    quote_title = models.CharField(max_length=32)
    quote = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('hero_image'),
        MultiFieldPanel([
            FieldPanel('top_title'),
            FieldPanel('top_text')
        ], heading="Top Section"),
        MultiFieldPanel([
            FieldPanel('overview_title'),
            InlinePanel("overview_items", heading="Overview"),
        ], heading="Overview Section"),
        MultiFieldPanel([
            FieldPanel('statistics_title'),
            InlinePanel("statistics", heading="Statistics"),
        ], heading="Statistics Section"),
        MultiFieldPanel([
            FieldPanel('accreditation_title'),
            FieldPanel('accreditation_text'),
            InlinePanel("accreditations", heading="Accreditations"),
        ], heading="Accreditations Section"),
        MultiFieldPanel([
            FieldPanel('alumni_title'),
            InlinePanel("alumni", heading="Alumni"),
        ], heading="Alumni Section"),
        MultiFieldPanel([
            FieldPanel('quote_title'),
            FieldPanel('quote')
        ], heading="Quote Section")
    ]

    api_fields = [
        APIField('top_title'),
        APIField('top_text'),
        APIField('overview_title'),
        APIField("overview_items"),
        APIField('statistics_title'),
        APIField("statistics"),
        APIField('accreditation_title'),
        APIField('accreditation_text'),
        APIField("accreditations"),
        APIField('alumni_title'),
        APIField("alumni"),
        APIField('quote_title'),
        APIField('quote'),
    ]
