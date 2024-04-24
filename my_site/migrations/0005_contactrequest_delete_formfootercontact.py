# Generated by Django 5.0.4 on 2024-04-21 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0004_delete_formpopup'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
            ],
        ),
        migrations.DeleteModel(
            name='FormFooterContact',
        ),
    ]
