# Generated by Django 2.1.7 on 2019-04-02 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_pdf'),
    ]

    operations = [
        migrations.DeleteModel(
            name='pdf',
        ),
    ]