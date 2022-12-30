# Generated by Django 4.1.4 on 2022-12-21 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0003_author_date_of_death_alter_author_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='browser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
