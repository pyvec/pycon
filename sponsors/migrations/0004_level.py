# Generated by Django 4.2.1 on 2023-08-21 21:32

from django.db import migrations, models
from django.utils.text import slugify


def populate_levels(apps, schema_editor):
    Level = apps.get_model("sponsors", "Level")

    LEVELS = (
        (1, "Platinum"),
        (2, "Gold"),
        (3, "Silver"),
        (4, "Bronze"),
        (5, "Diversity"),
        (6, "Media"),
        (7, "Partners"),
        (9, "Connectivity"),
    )

    for order, title in LEVELS:
        slug = slugify(title)
        Level.objects.create(order=order, title=title, slug=slug, size=0)


class Migration(migrations.Migration):
    dependencies = [
        ("sponsors", "0003_sponsor_linkedin_delete_sponsorsoffer"),
    ]

    operations = [
        migrations.CreateModel(
            name="Level",
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
                ("title", models.CharField(max_length=100)),
                ("slug", models.SlugField(blank=True, unique=True)),
                ("order", models.PositiveIntegerField()),
                ("size", models.PositiveIntegerField(default=0)),
            ],
            options={
                "ordering": ["order"],
            },
        ),
        migrations.RunPython(populate_levels),
    ]