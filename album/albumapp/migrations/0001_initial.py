# Generated by Django 3.2.16 on 2022-12-09 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Engagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=250)),
                ('e_img', models.ImageField(upload_to='gallery')),
            ],
        ),
    ]