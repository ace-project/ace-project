# Generated by Django 3.2.9 on 2022-03-19 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0005_auto_20220312_0543'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='coordinates',
            field=models.CharField(default='33.361365, 126.529669', max_length=100),
        ),
        migrations.AddField(
            model_name='travel',
            name='image_second',
            field=models.ImageField(null=True, upload_to='travels'),
        ),
    ]