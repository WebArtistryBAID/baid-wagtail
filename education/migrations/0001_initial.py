# Generated by Django 4.2.2 on 2023-06-26 04:09

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0083_workflowcontenttype"),
    ]

    operations = [
        migrations.CreateModel(
            name="LaerningMethods",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(default="", max_length=50)),
                ("content", wagtail.fields.RichTextField(default="")),
                ("image", models.ImageField(default="", upload_to="learning_methods/")),
            ],
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("curriculum_tilte", models.CharField(default="", max_length=50)),
                ("curriculum_sub_title_1", models.CharField(default="", max_length=50)),
                ("curriculum_content_1", wagtail.fields.RichTextField(default="")),
                ("curriculum_sub_title_2", models.CharField(default="", max_length=50)),
                ("curriculum_content_2", wagtail.fields.RichTextField(default="")),
                ("curriculum_sub_title_3", models.CharField(default="", max_length=50)),
                ("curriculum_content_3", wagtail.fields.RichTextField(default="")),
                ("learning_methods_title", models.CharField(default="", max_length=50)),
                ("student_guidance_title", models.CharField(default="", max_length=50)),
                (
                    "wonderful_moments_title",
                    models.CharField(default="", max_length=50),
                ),
                (
                    "learning_methods",
                    models.ManyToManyField(to="education.laerningmethods"),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
