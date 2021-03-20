# Generated by Django 2.2.4 on 2021-03-20 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ninja',
            name='dojo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ninjas', to='dojos.Dojo'),
        ),
        migrations.AlterField(
            model_name='ninja',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
    ]
