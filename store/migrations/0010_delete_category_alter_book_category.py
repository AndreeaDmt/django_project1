# Generated by Django 4.2.4 on 2023-08-20 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_remove_book_book_slug_remove_category_category_slug_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('Novel', 'Novel'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Fantasy', 'Fantasy'), ('Young Adult', 'Young Adult'), ('Thriller', 'Thriller'), ('Self-Help & Personal Growth', 'Self-Help & Personal Growth')], max_length=50),
        ),
    ]
