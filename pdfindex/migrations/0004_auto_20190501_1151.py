# Generated by Django 2.1.7 on 2019-05-01 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfindex', '0003_auto_20190408_1707'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pdf',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='pdf',
            name='title',
            field=models.CharField(max_length=32),
        ),
    ]
