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

    student_title = models.CharField(default="", max_length=50)
    student_content = RichTextField(default="")
    student_join = models.CharField(default="", max_length=50)

    faculty_title = models.CharField(default="", max_length=50)
    faculty_content = RichTextField(default="")
    faculty_join = models.CharField(default="", max_length=50)

    content_panels = Page.content_panels + [
        FieldPanel("carousel_images"),
        MultiFieldPanel(
            [
                FieldPanel("student_title"),
                FieldPanel("student_content"),
                FieldPanel("student_join"),
            ],
            heading="Student",
        ),
        MultiFieldPanel(
            [
                FieldPanel("faculty_title"),
                FieldPanel("faculty_content"),
                FieldPanel("faculty_join"),
            ],
            heading="Faculty",
        ),
    ]

    api_fields = [
        APIField("carousel_images"),
        APIField("student_title"),
        APIField("student_content"),
        APIField("student_join"),
        APIField("faculty_title"),
        APIField("faculty_content"),
        APIField("faculty_join"),
    ]
