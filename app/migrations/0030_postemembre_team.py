# Generated by Django 5.0.2 on 2024-03-26 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_poste_service_sous_text_equipe2'),
    ]

    operations = [
        migrations.CreateModel(
            name='PosteMembre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=200)),
                ('title2', models.CharField(max_length=200)),
                ('title3', models.CharField(max_length=200)),
                ('text_team', models.CharField(max_length=200)),
                ('sous_text_team', models.CharField(max_length=200)),
                ('text_meth', models.CharField(max_length=200)),
                ('sous_text_meth', models.CharField(max_length=200)),
                ('text_cadre', models.CharField(max_length=200)),
                ('sous_text_cadre', models.CharField(max_length=200)),
                ('text_outil', models.CharField(max_length=200)),
                ('sous_text_outil', models.CharField(max_length=200)),
            ],
        ),
    ]
