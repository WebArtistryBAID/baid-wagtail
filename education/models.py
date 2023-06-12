from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.api import APIField


# Create your models here.

class Education(Page):
    curriculum_tilte = models.CharField(default="", max_length=50)
    curriculum_sub_title_1 = models.CharField(default="", max_length=50)
    curriculum_content_1 = RichTextField(default="")
    curriculum_sub_title_2 = models.CharField(default="", max_length=50)
    curriculum_content_2 = RichTextField(default="")
    curriculum_sub_title_3 = models.CharField(default="", max_length=50)
    curriculum_content_3 = RichTextField(default="")

    learning_methods_title = models.CharField(default="", max_length=50)
    learning_methods_sub_title_1 = models.CharField(default="", max_length=50)
    learning_methods_content_1 = RichTextField(default="")
    learning_methods_sub_title_2 = models.CharField(default="", max_length=50)
    learning_methods_content_2 = RichTextField(default="")
    learning_methods_sub_title_3 = models.CharField(default="", max_length=50)
    learning_methods_content_3 = RichTextField(default="")

    student_guidance_title = models.CharField(default="", max_length=50)

    wonderful_moments_title = models.CharField(default="", max_length=50)

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('curriculum_tilte'),
        index.SearchField('curriculum_sub_title_1'),
        index.SearchField('curriculum_content_1'),
        index.SearchField('curriculum_sub_title_2'),
        index.SearchField('curriculum_content_2'),
        index.SearchField('curriculum_sub_title_3'),
        index.SearchField('curriculum_content_3'),
        index.SearchField('learning_methods_title'),
        index.SearchField('learning_methods_sub_title_1'),
        index.SearchField('learning_methods_content_1'),
        index.SearchField('learning_methods_sub_title_2'),
        index.SearchField('learning_methods_content_2'),
        index.SearchField('learning_methods_sub_title_3'),
        index.SearchField('learning_methods_content_3'),
        index.SearchField('student_guidance_title'),
        index.SearchField('wonderful_moments_title'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("title"),
        FieldPanel("curriculum_tilte"),
        FieldPanel("curriculum_sub_title_1"),
        FieldPanel("curriculum_content_1"),
        FieldPanel("curriculum_sub_title_2"),
        FieldPanel("curriculum_content_2"),
        FieldPanel("curriculum_sub_title_3"),
        FieldPanel("curriculum_content_3"),
        FieldPanel("learning_methods_title"),
        FieldPanel("learning_methods_sub_title_1"),
        FieldPanel("learning_methods_content_1"),
        FieldPanel("learning_methods_sub_title_2"),
        FieldPanel("learning_methods_content_2"),
        FieldPanel("learning_methods_sub_title_3"),
        FieldPanel("learning_methods_content_3"),
        FieldPanel("student_guidance_title"),
        FieldPanel("wonderful_moments_title"),
    ]

    api_fields = [
        APIField("title"),
        APIField("curriculum_tilte"),
        APIField("curriculum_sub_title_1"),
        APIField("curriculum_content_1"),
        APIField("curriculum_sub_title_2"),
        APIField("curriculum_content_2"),
        APIField("curriculum_sub_title_3"),
        APIField("curriculum_content_3"),
        APIField("learning_methods_title"),
        APIField("learning_methods_sub_title_1"),
        APIField("learning_methods_content_1"),
        APIField("learning_methods_sub_title_2"),
        APIField("learning_methods_content_2"),
        APIField("learning_methods_sub_title_3"),
        APIField("learning_methods_content_3"),
        APIField("student_guidance_title"),
        APIField("wonderful_moments_title"),
    ]

