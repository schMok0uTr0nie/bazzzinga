# Generated by Django 4.0.4 on 2022-06-07 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_alter_profile_options_remove_profile_nick'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['nick'], 'verbose_name': 'Registered User', 'verbose_name_plural': 'Зареганты'},
        ),
        migrations.AddField(
            model_name='profile',
            name='nick',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Nomad'),
        ),
    ]
