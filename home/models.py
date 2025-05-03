from django.db import models
from modelcluster.fields import ParentalKey
from wagtail import blocks
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.api import APIField
from wagtail.fields import StreamField, RichTextField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page

from baid.api import ImageUrlField


class HomePageHighlight(models.Model):
    page = ParentalKey("HomePage", related_name="highlights")

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


class HomePage(Page):
    hero_images = StreamField(
        [
            ("image", ImageChooserBlock())
        ],
        use_json_field=True,
        null=True
    )
    hero_subtitle = models.CharField(max_length=128)

    intro_title = models.CharField(max_length=32)
    intro_text = RichTextField()

    motto_title = models.CharField(max_length=32)
    motto_content = RichTextField()
    motto_bg = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,

        related_name='+',
    )

    spirit_title = models.CharField(max_length=32)
    spirit_content = RichTextField()
    spirit_bg = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,

        related_name='+',
    )

    literacy_title = models.CharField(max_length=32)
    literacy_content = RichTextField()
    literacy_bg = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,

        related_name='+',
    )

    pathway_title = models.CharField(max_length=32)
    pathway_content = RichTextField()
    pathway_bg = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,

        related_name='+',
    )

    principal_quote = RichTextField()
    principal_name = models.CharField(max_length=32)
    principal_avatar = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,

        related_name='+',
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_images'),
            FieldPanel('hero_subtitle'),
        ], heading="Hero Section"),

        MultiFieldPanel([
            FieldPanel('intro_title'),
            FieldPanel('intro_text')
        ], heading="Introduction Section"),

        InlinePanel("highlights", heading="Highlights"),

        MultiFieldPanel([
            FieldPanel('motto_title'),
            FieldPanel('motto_content'),
            FieldPanel('motto_bg'),

            FieldPanel('spirit_title'),
            FieldPanel('spirit_content'),
            FieldPanel('spirit_bg'),

            FieldPanel('literacy_title'),
            FieldPanel('literacy_content'),
            FieldPanel('literacy_bg'),

            FieldPanel('pathway_title'),
            FieldPanel('pathway_content'),
            FieldPanel('pathway_bg')
        ], heading="Philosophy Section"),

        MultiFieldPanel([
            FieldPanel('principal_quote'),
            FieldPanel('principal_name'),
            FieldPanel('principal_avatar'),
        ], heading="Quote Section")
    ]

    api_fields = [
        APIField('hero_images', serializer=ImageUrlField()),
        APIField('hero_subtitle'),
        APIField('intro_title'),
        APIField('intro_text'),
        APIField("highlights"),
        APIField('motto_title'),
        APIField('motto_content'),
        APIField('motto_bg', serializer=ImageUrlField()),
        APIField('spirit_title'),
        APIField('spirit_content'),
        APIField('spirit_bg', serializer=ImageUrlField()),
        APIField('literacy_title'),
        APIField('literacy_content'),
        APIField('literacy_bg', serializer=ImageUrlField()),
        APIField('pathway_title'),
        APIField('pathway_content'),
        APIField('pathway_bg', serializer=ImageUrlField()),
        APIField('principal_quote'),
        APIField('principal_name'),
        APIField('principal_avatar', serializer=ImageUrlField())
    ]
