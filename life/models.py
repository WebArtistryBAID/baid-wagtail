from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.admin.panels import InlinePanel
from wagtail.api import APIField
from wagtail.fields import RichTextField
from wagtail.models import Page

from baid.api import ImageUrlField


class StudentLifePageHighlight(models.Model):
    page = ParentalKey("StudentLifePage", related_name="highlights")

    title = models.CharField(max_length=32, help_text="Highlight title")
    description = RichTextField(help_text="Highlight description")
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        related_name="+",
        help_text="Highlight image"
    )
    link = models.URLField(blank=True, help_text="Highlight link")

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


class StudentLifePageActivity(models.Model):
    page = ParentalKey("StudentLifePage", related_name="activities")

    name = models.CharField(max_length=32, help_text="Activity name")
    description = RichTextField(help_text="Activity description")
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        related_name="+",
        help_text="Activity image"
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("description"),
        FieldPanel("image"),
    ]

    api_fields = [
        APIField("name"),
        APIField("description"),
        APIField("image", serializer=ImageUrlField()),
    ]


class StudentLifePageClub(models.Model):
    page = ParentalKey("StudentLifePage", related_name="clubs")

    name = models.CharField(max_length=32, help_text="Club name")
    description = RichTextField(help_text="Club description")
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        related_name="+",
        help_text="Club image"
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("description"),
        FieldPanel("image"),
    ]

    api_fields = [
        APIField("name"),
        APIField("description"),
        APIField("image", serializer=ImageUrlField()),
    ]


class StudentLifePage(Page):
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,

        related_name='+',
    )
    intro_title = models.CharField(max_length=32)
    intro_text = RichTextField()

    quote = RichTextField()

    activities_title = models.CharField(max_length=32)

    clubs_title = models.CharField(max_length=32)

    content_panels = Page.content_panels + [
        FieldPanel('hero_image'),
        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro_text')
        ], heading="Introduction Section"),
        InlinePanel("highlights", heading="Highlights"),
        FieldPanel('quote'),
        MultiFieldPanel([
            FieldPanel('activities_title'),
            InlinePanel("activities", heading="Activities"),
        ], heading="Activities Section"),
        MultiFieldPanel([
            FieldPanel('clubs_title'),
            InlinePanel("clubs", heading="Clubs"),
        ], heading="Clubs Section")
    ]

    api_fields = [
        APIField('hero_image', serializer=ImageUrlField()),
        APIField('intro_title'),
        APIField('intro_text'),
        APIField("highlights"),
        APIField('quote'),
        APIField('activities_title'),
        APIField("activities"),
        APIField('clubs_title'),
        APIField("clubs"),
    ]
