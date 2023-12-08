# Generated by Django 5.0 on 2023-12-08 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('anwser1', models.CharField(max_length=255)),
                ('anwser2', models.CharField(max_length=255)),
                ('anwser3', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('anwser4', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('anwser5', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('anwser6', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('anwser7', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('anwser8', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('anwser', models.TextField()),
            ],
        ),
    ]