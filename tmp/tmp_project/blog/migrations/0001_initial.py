# Generated by Django 4.1.3 on 2022-11-29 10:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Articles",
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
                ("titles", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=100, unique=True)),
                ("descriptions", models.TextField()),
                ("thumbnail", models.ImageField(upload_to="images")),
                ("publish", models.DateField(default=django.utils.timezone.now)),
                ("created", models.DateField(auto_now_add=True)),
                ("updated", models.DateField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("d", "Draft"), ("p", "Published")], max_length=1
                    ),
                ),
            ],
        ),
    ]