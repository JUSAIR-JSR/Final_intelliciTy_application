# Generated by Django 5.1.1 on 2025-04-11 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_skill_alter_jobposting_required_skills'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.ManyToManyField(blank=True, to='jobs.skill'),
        ),
    ]
