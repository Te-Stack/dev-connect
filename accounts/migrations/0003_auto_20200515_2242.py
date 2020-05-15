# Generated by Django 3.0.5 on 2020-05-15 21:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200515_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='github_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='linkedin_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='professional_status',
            field=models.CharField(blank=True, choices=[('DEV', 'Developer'), ('JNR_DEV', 'Junior Developer'), ('SNR_DEV', 'Senior Developer'), ('INT', 'Intern'), ('MAN', 'Manager'), ('STU_LEA', 'Student or Learning'), ('INS_TEA', 'Instructor or Teacher'), ('OTH', 'Other')], default='OTH', max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
