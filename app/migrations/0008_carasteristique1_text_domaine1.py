# Generated by Django 5.0.2 on 2024-03-24 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_accueil_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='carasteristique1',
            name='text_domaine1',
            field=models.CharField(default=False, max_length=200),
            preserve_default=False,
        ),
    ]