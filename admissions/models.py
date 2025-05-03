from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.api import APIField
from wagtail.fields import RichTextField
from wagtail.models import Page

from baid.api import ImageUrlField


class AdmissionsPageStatistic(models.Model):
    page = ParentalKey("AdmissionsPage", related_name="statistics")
    name = models.CharField(max_length=32)
    content = models.CharField(max_length=64)

    panels = [
        FieldPanel("name"),
        FieldPanel("content"),
    ]

    api_fields = [
        APIField("name"),
        APIField("content"),
    ]


class AdmissionsPageHighlight(models.Model):
    page = ParentalKey("AdmissionsPage", related_name="highlights")
    title = models.CharField(max_length=64)
    description = RichTextField()
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        related_name="+"
    )
    link = models.URLField(blank=True)

    panels = [
        FieldPanel("title"),
        FieldPanel("description"),
        FieldPanel("image"),
        FieldPanel("link"),
    ]

    api_fields = [
        APIField("title"),
        APIField("description"),
        APIField("image", serializer=ImageUrlField()),
        APIField("link"),
    ]


class AdmissionsPageOverview(models.Model):
    page = ParentalKey("AdmissionsPage", related_name="overview_items")
    title = models.CharField(max_length=32)
    content = RichTextField()

    panels = [
        FieldPanel("title"),
        FieldPanel("content"),
    ]

    api_fields = [
        APIField("title"),
        APIField("content"),
    ]


class AdmissionsPageStep(models.Model):
    page = ParentalKey("AdmissionsPage", related_name="steps")
    name = models.CharField(max_length=32)
    content = RichTextField()

    panels = [
        FieldPanel("name"),
        FieldPanel("content"),
    ]

    api_fields = [
        APIField("name"),
        APIField("content"),
    ]


class AdmissionsPageContactEmail(models.Model):
    page = ParentalKey("AdmissionsPage", related_name="contact_emails")
    email = models.CharField(max_length=256)

    panels = [
        FieldPanel("email"),
    ]

    api_fields = [
        APIField("email"),
    ]


class AdmissionsPageContactPhone(models.Model):
    page = ParentalKey("AdmissionsPage", related_name="contact_phones")
    phone = models.CharField(max_length=256)

    panels = [
        FieldPanel("phone"),
    ]

    api_fields = [
        APIField("phone"),
    ]


class AdmissionsPage(Page):
    top_title = models.CharField(max_length=32)
    top_text = RichTextField()
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,

        related_name='+'
    )

    intro_title = models.CharField(max_length=32)
    intro_text = RichTextField()

    statistics_title = models.CharField(max_length=32)

    highlights = None

    overview_title = models.CharField(max_length=32)

    application_status_text = RichTextField()

    steps_title = models.CharField(max_length=32)

    application_form_link = models.URLField()

    contact_title = models.CharField(max_length=32)
    contact_description = models.CharField(max_length=256)

    contact_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,

        related_name='+'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('top_title'),
            FieldPanel('top_text')
        ], heading="Top Section"),
        FieldPanel('hero_image'),
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro_text')
        ], heading="Introduction Section"),
        MultiFieldPanel([
            FieldPanel('statistics_title'),
            InlinePanel("statistics", heading="Statistics"),
        ], heading="Statistics Section"),
        InlinePanel("highlights", heading="Highlights"),
        MultiFieldPanel([
            FieldPanel('overview_title'),
            InlinePanel("overview_items", heading="Overview"),
        ], heading="Overview Section"),
        MultiFieldPanel([
            FieldPanel('application_status_text'),
            FieldPanel('steps_title'),
            InlinePanel("steps", heading="Steps"),
            FieldPanel('application_form_link')
        ], heading="Steps Section"),
        MultiFieldPanel([
            FieldPanel('contact_title'),
            FieldPanel('contact_description'),
            InlinePanel("contact_emails", heading="Contact Emails"),
            InlinePanel("contact_phones", heading="Contact Phones"),
            FieldPanel('contact_image')
        ], heading="Contact Section")
    ]

    api_fields = [
        APIField('top_title'),
        APIField('top_text'),
        APIField('hero_image', serializer=ImageUrlField()),
        APIField('intro_title'),
        APIField('intro_text'),
        APIField('statistics_title'),
        APIField("statistics"),
        APIField("highlights"),
        APIField('overview_title'),
        APIField("overview_items"),
        APIField('application_status_text'),
        APIField('steps_title'),
        APIField("steps"),
        APIField('application_form_link'),
        APIField('contact_title'),
        APIField('contact_description'),
        APIField("contact_emails"),
        APIField("contact_phones"),
        APIField('contact_image', serializer=ImageUrlField()),
    ]
