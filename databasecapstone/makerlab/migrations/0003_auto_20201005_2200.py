# Generated by Django 3.1.1 on 2020-10-05 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('makerlab', '0002_auto_20201005_0121'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MachinesInUse',
            new_name='InUseMachine',
        ),
        migrations.RenameModel(
            old_name='Inventory',
            new_name='Item',
        ),
        migrations.RenameModel(
            old_name='RegisteredUsers',
            new_name='RegisteredUser',
        ),
        migrations.RenameModel(
            old_name='Supervisors',
            new_name='Supervisor',
        ),
    ]
