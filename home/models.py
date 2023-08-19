from django.db import models
from wagtail.images.blocks import ImageChooserBlock

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.api import APIField

from baid.api import ImageUrlField


class Home(Page):
    carousel_images = StreamField(
        [
            ("image", ImageChooserBlock()),
        ],
        use_json_field=True,
        null=True,
    )
    head = models.CharField(default="", max_length=50)
    introduction_title = models.CharField(default="", max_length=100)
    introduction = RichTextField(default="")

    motto_title = models.CharField(default="", max_length=50)
    motto_content = models.CharField(default="", max_length=50)
    spirit_title = models.CharField(default="", max_length=50)
    spirit_content = models.CharField(default="", max_length=50)
    key_competency_title = models.CharField(default="", max_length=50)
    key_competency_content = models.CharField(default="", max_length=50)
    cultivation_title = models.CharField(default="", max_length=50)
    cultivation_content = models.CharField(default="", max_length=50)

    principal_message = models.CharField(default="", max_length=50)
    principal_avatar = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.SET_NULL, related_name="+", null=True
    )
    principal_name = models.CharField(default="", max_length=50)

    admission_results_title = models.CharField(default="", max_length=50)
    admission_results_content = RichTextField(default="")

    content_panels = Page.content_panels + [
        FieldPanel("carousel_images"),
        FieldPanel("head"),
        MultiFieldPanel(
            [
                FieldPanel("introduction_title"),
                FieldPanel("introduction"),
            ],
            heading="Introduction",
        ),
        MultiFieldPanel(
            [
                FieldPanel("motto_title"),
                FieldPanel("motto_content"),
                FieldPanel("spirit_title"),
                FieldPanel("spirit_content"),
                FieldPanel("key_competency_title"),
                FieldPanel("key_competency_content"),
                FieldPanel("cultivation_title"),
                FieldPanel("cultivation_content"),
            ],
            heading="Education Philosophy",
        ),
        MultiFieldPanel(
            [
                FieldPanel("principal_message"),
                FieldPanel("principal_avatar"),
                FieldPanel("principal_name"),
            ],
            heading="Principal Remark",
        ),
        FieldPanel("admission_results_content"),
    ]

    api_fields = [
        APIField("carousel_images", serializer=ImageUrlField()),
        APIField("head"),
        APIField("introduction_title"),
        APIField("introduction"),
        APIField("motto_title"),
        APIField("motto_content"),
        APIField("spirit_title"),
        APIField("spirit_content"),
        APIField("key_competency_title"),
        APIField("key_competency_content"),
        APIField("cultivation_title"),
        APIField("cultivation_content"),
        APIField("principal_message"),
        APIField("principal_avatar", serializer=ImageUrlField()),
        APIField("principal_name"),
        APIField("admission_results_content"),
    ]
