from django.db import models
from django.db.models.fields import CharField

from wagtail.models import Page, ParentalKey
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.api import APIField
from wagtail.images.blocks import ImageChooserBlock

from baid.api import ImageUrlField


class ImageCard(models.Model):
    """
    An card with image
    """

    page = ParentalKey("JoinUs", related_name="student_cards")
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


class JoinUs(Page):
    carousel_images = StreamField(
        [
            ("image", ImageChooserBlock()),
        ],
        use_json_field=True,
        null=True,
    )

    student = RichTextField(default="")

    student_first_title = models.CharField(default="", max_length=100)
    student_first_content = RichTextField(default="")
    student_first_image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.SET_NULL, related_name="+", null=True
    )

    faculty = RichTextField(default="")

    faculty_requirements_title = models.CharField(default="", max_length=100)
    faculty_requirements_left = RichTextField(default="")
    faculty_requirements_right = RichTextField(default="")

    faculty_card_title = models.CharField(default="", max_length=100)
    faculty_card_content = RichTextField(default="")
    faculty_card_image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.SET_NULL, related_name="+", null=True
    )

    faculty_process_title = models.CharField(default="", max_length=100)
    faculty_process_left = RichTextField(default="")
    faculty_process_right = RichTextField(default="")

    faculty_epilogue = RichTextField(default="")

    content_panels = Page.content_panels + [
        FieldPanel("carousel_images"),
        MultiFieldPanel(
            [
                FieldPanel("student", heading="Introduction"),
                MultiFieldPanel(
                    [
                        FieldPanel("student_first_title", heading="Title"),
                        FieldPanel("student_first_content", heading="Content"),
                        FieldPanel("student_first_image", heading="Image"),
                    ],
                    heading="First card",
                ),
                InlinePanel("student_cards", heading="Other cards"),
            ],
            heading="Student",
        ),
        MultiFieldPanel(
            [
                FieldPanel("faculty", heading="Introduction"),
                MultiFieldPanel(
                    [
                        FieldPanel(
                            "faculty_requirements_title", heading="Requirements title"
                        ),
                        FieldPanel("faculty_requirements_left", heading="Left"),
                        FieldPanel("faculty_requirements_right", heading="Right"),
                    ],
                    heading="Requirements",
                ),
                MultiFieldPanel(
                    [
                        FieldPanel("faculty_card_title", heading="Title"),
                        FieldPanel("faculty_card_content", heading="Content"),
                        FieldPanel("faculty_card_image", heading="Image"),
                    ],
                    heading="Card",
                ),
                MultiFieldPanel(
                    [
                        FieldPanel("faculty_process_title", heading="Title"),
                        FieldPanel("faculty_process_left", heading="Left"),
                        FieldPanel("faculty_process_right", heading="Right"),
                    ],
                    heading="Process",
                ),
                FieldPanel("faculty_epilogue", heading="Epilogue"),
            ],
            heading="Faculty",
        ),
    ]

    api_fields = [
        APIField("carousel_images", serializer=ImageUrlField()),
        APIField("student"),
        APIField("student_first_title"),
        APIField("student_first_content"),
        APIField("student_first_image", serializer=ImageUrlField()),
        APIField("student_cards"),
        APIField("faculty"),
        APIField("faculty_requirements_title"),
        APIField("faculty_requirements_left"),
        APIField("faculty_requirements_right"),
        APIField("faculty_card_title"),
        APIField("faculty_card_content"),
        APIField("faculty_card_image", serializer=ImageUrlField()),
        APIField("faculty_process_title"),
        APIField("faculty_process_left"),
        APIField("faculty_process_right"),
        APIField("faculty_epilogue"),
    ]
