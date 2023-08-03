from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.api import APIField
from wagtail.images.blocks import ImageChooserBlock


class JoinUs(Page):
    carousel_images = StreamField(
        [
            ("image", ImageChooserBlock()),
        ],
        use_json_field=True,
        null=True,
    )

    student = RichTextField(default="")
    student_portal = models.URLField(blank=True, null=True)

    faculty = RichTextField(default="")
    faculty_portal = models.URLField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("carousel_images"),
        MultiFieldPanel(
            [
                FieldPanel("student"),
                FieldPanel("student_portal"),
            ],
            heading="Student",
        ),
        MultiFieldPanel(
            [
                FieldPanel("faculty"),
                FieldPanel("faculty_portal"),
            ],
            heading="Faculty",
        ),
    ]

    api_fields = [
        APIField("carousel_images"),
        APIField("student"),
        APIField("student_portal"),
        APIField("faculty"),
        APIField("faculty_portal"),
    ]
