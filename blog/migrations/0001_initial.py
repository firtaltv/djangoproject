# Generated by Django 4.0.4 on 2023-03-29 15:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=250)),
                ('text', models.TextField(max_length=50)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
