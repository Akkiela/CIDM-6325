# Generated by Django 5.1.1 on 2024-11-24 04:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CheckoutSessionRecord",
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
                ("stripe_customer_id", models.CharField(max_length=255)),
                ("stripe_checkout_session_id", models.CharField(max_length=255)),
                ("stripe_price_id", models.CharField(max_length=255)),
                ("has_access", models.BooleanField(default=False)),
                ("is_completed", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        help_text="The user who initiated the checkout.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
