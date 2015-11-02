# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
<<<<<<< HEAD
=======
import django.utils.timezone
from django.conf import settings
>>>>>>> 58b79890669009e69b4541e50f4c72a82e7bcfff


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
=======
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
>>>>>>> 58b79890669009e69b4541e50f4c72a82e7bcfff
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
=======
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
>>>>>>> 58b79890669009e69b4541e50f4c72a82e7bcfff
            ],
        ),
    ]
