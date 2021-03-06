# Generated by Django 3.1.1 on 2020-10-11 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('makerlab', '0007_auto_20201008_1821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=200, unique=True)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='vendor_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='makerlab.vendor', to_field='vendor_name'),
            preserve_default=False,
        ),
    ]
