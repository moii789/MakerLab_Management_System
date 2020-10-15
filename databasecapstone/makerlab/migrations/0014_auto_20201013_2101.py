# Generated by Django 3.1.1 on 2020-10-14 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('makerlab', '0013_item_warranty'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InUseMachine',
            new_name='InUseItem',
        ),
        migrations.AlterField(
            model_name='item',
            name='vendor_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makerlab.vendor'),
        ),
    ]