# Generated by Django 4.2.5 on 2023-10-12 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0004_alter_project_description_projectsinportfolio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProjectsInPortfolio',
        ),
    ]