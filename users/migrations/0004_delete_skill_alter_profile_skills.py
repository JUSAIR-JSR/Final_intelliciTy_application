# Generated by Django 5.1.1 on 2025-04-11 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_skill_alter_jobposting_required_skills'),
        ('users', '0003_skill_alter_profile_skills'),
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
