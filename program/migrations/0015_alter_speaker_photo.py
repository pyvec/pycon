# Generated by Django 4.2.1 on 2023-08-24 17:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("program", "0014_alter_speaker_github_alter_speaker_linkedin_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="speaker",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="speakers/"),
        ),
    ]