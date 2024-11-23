# Generated by Django 5.1.1 on 2024-11-23 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="image",
            name="cuisineType",
        ),
        migrations.RemoveField(
            model_name="image",
            name="mealType",
        ),
        migrations.AddField(
            model_name="image",
            name="blogType",
            field=models.CharField(
                choices=[
                    ("breakfast", "Breakfast"),
                    ("lunch", "Lunch"),
                    ("dinner", "Dinner"),
                    ("travelPost", "TravelPost"),
                    ("moviePost", "MoviePost"),
                    ("dietPost", "DietPost"),
                ],
                default="breakfast",
                max_length=50,
            ),
        ),
    ]
