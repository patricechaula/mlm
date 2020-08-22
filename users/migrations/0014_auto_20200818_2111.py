# Generated by Django 3.0.5 on 2020-08-18 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20200818_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_child_of',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='child_of', to='users.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='is_grand_child_of',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='grand_child_of', to='users.Profile'),
            preserve_default=False,
        ),
    ]