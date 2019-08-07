# Generated by Django 2.2.3 on 2019-08-07 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('template_nm', models.TextField(max_length=1000)),
                ('create_dt', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_modified_dt', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theme_author', to=settings.AUTH_USER_MODEL)),
                ('last_modified_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='last_modified_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
