# Generated by Django 4.1.2 on 2023-03-10 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0003_post_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]