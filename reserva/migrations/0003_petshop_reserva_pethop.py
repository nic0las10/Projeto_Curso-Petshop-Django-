# Generated by Django 4.2.10 on 2024-04-25 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0002_rename_dia_reserva_dia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Petshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('rua', models.CharField(max_length=100, verbose_name='Rua')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
            ],
        ),
        migrations.AddField(
            model_name='reserva',
            name='pethop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='reserva.petshop'),
        ),
    ]
