# Generated by Django 4.2.1 on 2023-05-15 18:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("address", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
