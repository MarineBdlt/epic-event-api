# Generated by Django 4.0.6 on 2022-08-08 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.CharField(blank=True, max_length=1000, null=True)),
                ('status', models.CharField(choices=[('REDACTION', 'Rédaction'), ('EN SIGNATURE', 'En cours de signature'), ('SIGNE', 'Signé'), ('TERMINE', 'Terminé')], default=('REDACTION', 'Rédaction'), max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_client', to='clients.client')),
            ],
        ),
    ]
