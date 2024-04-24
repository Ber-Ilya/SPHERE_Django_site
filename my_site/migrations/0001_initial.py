# Generated by Django 5.0.4 on 2024-04-16 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date_pub', models.DateTimeField(verbose_name='date published')),
                ('review', models.TextField(max_length=300)),
                ('stars', models.CharField(choices=[('1', '*'), ('2', '**'), ('3', '***'), ('4', '****'), ('5', '*****')], max_length=5)),
                ('like', models.CharField(choices=[('like', 'like'), ('dislike', 'dislike')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('like', models.CharField(choices=[('like', 'like'), ('dislike', 'dislike')], max_length=7)),
                ('comment', models.ForeignKey(max_length=300, on_delete=django.db.models.deletion.CASCADE, to='my_site.reviews')),
            ],
        ),
    ]