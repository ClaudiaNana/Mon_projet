# Generated by Django 5.0.3 on 2024-04-20 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangalib', '0003_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Quantité'),
        ),
    ]
