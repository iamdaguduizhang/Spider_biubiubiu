# Generated by Django 2.1.7 on 2019-05-31 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0002_auto_20190531_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='status',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]