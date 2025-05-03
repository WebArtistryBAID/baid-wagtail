from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.api import APIField
from wagtail.fields import RichTextField
from wagtail.models import Page

from baid.api import ImageUrlField


class AcademicsPageCurriculum(models.Model):
    page = ParentalKey("AcademicsPage", related_name="curricula")
    name = models.CharField(max_length=32)
    description = RichTextField()

    panels = [
        FieldPanel("name"),
        FieldPanel("description"),
    ]

    api_fields = [
        APIField("name"),
        APIField("description"),
    ]


class AcademicsPageCourseType(models.Model):
    page = ParentalKey("AcademicsPage", related_name="courses")
    name = models.CharField(max_length=32)
    courses = models.JSONField(default=list, help_text="List of courses")

    panels = [
        FieldPanel("name"),
        FieldPanel("courses"),
    ]

    api_fields = [
        APIField("name"),
        APIField("courses"),
    ]


class AcademicsPageStatistic(models.Model):
    page = ParentalKey("AcademicsPage", related_name="statistics")
    name = models.CharField(max_length=64)
    content = RichTextField()

    panels = [
        FieldPanel("name"),
        FieldPanel("content"),
    ]

    api_fields = [
        APIField("name"),
        APIField("content"),
    ]


class AcademicsPageSpecialtyHighlight(models.Model):
    page = ParentalKey("AcademicsPage", related_name="specialties_highlights")
    title = models.CharField(max_length=64)
    description = RichTextField()
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        related_name="+",
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


class AcademicsPageSpecialty(models.Model):
    page = ParentalKey("AcademicsPage", related_name="specialties")
    name = models.CharField(max_length=32)
    description = RichTextField()
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        related_name="+",
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


class AcademicsPage(Page):
    top_title = models.CharField(max_length=32)
    top_text = RichTextField()
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
    )

    curriculum_title = models.CharField(max_length=32)

    courses_title = models.CharField(max_length=32)

    statistics_title = models.CharField(max_length=32)

    specialties_title = models.CharField(max_length=32)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('top_title'),
            FieldPanel('top_text'),
        ], heading="Top Section"),
        FieldPanel('hero_image'),
        MultiFieldPanel([
            FieldPanel('curriculum_title'),
            InlinePanel("curricula", heading="Curricula"),
        ], heading="Curriculum Section"),
        MultiFieldPanel([
            FieldPanel('courses_title'),
            InlinePanel("courses", heading="Courses"),
        ], heading="Courses Section"),
        MultiFieldPanel([
            FieldPanel('statistics_title'),
            InlinePanel("statistics", heading="Statistics"),
        ], heading="Statistics Section"),
        MultiFieldPanel([
            FieldPanel('specialties_title'),
            InlinePanel("specialties_highlights", heading="Specialties Highlights"),
            InlinePanel("specialties", heading="Specialties"),
        ], heading="Specialties Section"),
    ]

    api_fields = [
        APIField('top_title'),
        APIField('top_text'),
        APIField('hero_image', serializer=ImageUrlField()),
        APIField('curriculum_title'),
        APIField('curricula'),
        APIField('courses_title'),
        APIField('courses'),
        APIField('statistics_title'),
        APIField('statistics'),
        APIField('specialties_title'),
        APIField('specialties_highlights'),
        APIField('specialties'),
    ]
