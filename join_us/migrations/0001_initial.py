# Generated by Django 4.2.3 on 2023-08-03 00:38

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinUs',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('carousel_images', wagtail.fields.StreamField([('image', wagtail.images.blocks.ImageChooserBlock())], null=True, use_json_field=True)),
                ('student', wagtail.fields.RichTextField(default='')),
                ('student_portal', models.URLField(blank=True, null=True)),
                ('faculty', wagtail.fields.RichTextField(default='')),
                ('faculty_portal', models.URLField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
