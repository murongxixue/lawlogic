# Generated by Django 4.2.4 on 2023-08-03 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('这是name', models.IntegerField(blank=True, default=0, help_text='这是一个测试')),
            ],
            options={
                'verbose_name': '测试表',
            },
        ),
    ]
