# Generated by Django 4.2.4 on 2023-08-15 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Novels', 'Novels'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Fantasy', 'Fantasy'), ('Young Adult', 'Young Adult'), ('Thriller', 'Thriller'), ('Self-Help & Personal Growth', 'Self-Help & Personal Growth')], db_index=True, max_length=250),
        ),
    ]
