# Generated by Django 4.2.1 on 2023-08-23 21:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sponsors", "0007_alter_level_options_alter_level_order_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sponsor",
            name="logo",
            field=models.FileField(
                blank=True, help_text="SVG only", null=True, upload_to="sponsors/"
            ),
        ),
    ]