# Generated by Django 4.0.6 on 2022-08-09 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200, null=True)),
                ('description', models.TextField(max_length=200, null=True)),
                ('keywords', models.TextField(max_length=200, null=True)),
                ('heading', models.TextField(max_length=200, null=True)),
                ('details', models.TextField(null=True)),
                ('featureimage', models.ImageField(null=True, upload_to='static')),
                ('status', models.BooleanField(null=True)),
                ('createdate', models.DateField(auto_now=True)),
                ('updatedate', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.category', verbose_name='categoryid')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]