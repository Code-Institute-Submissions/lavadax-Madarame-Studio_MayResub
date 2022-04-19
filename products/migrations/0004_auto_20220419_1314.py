# Generated by Django 3.2.12 on 2022-04-19 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
        ('products', '0003_rename_price_product_base_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='product',
            name='artist_url',
        ),
        migrations.AddField(
            model_name='product',
            name='artist_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='artists.artist'),
            preserve_default=False,
        ),
    ]
