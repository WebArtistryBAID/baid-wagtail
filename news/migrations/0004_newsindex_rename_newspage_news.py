# Generated by Django 4.2.2 on 2023-06-08 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailcore", "0083_workflowcontenttype"),
        ("news", "0003_newspage_lang"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewsIndex",
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
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.RenameModel(
            old_name="NewsPage",
            new_name="News",
        ),
    ]
