# Generated by Django 3.2.6 on 2024-10-09 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='m_data',
            fields=[
                ('id', models.IntegerField(max_length=11, primary_key=True, serialize=False)),
                ('ekspor', models.IntegerField(blank=True, max_length=5, null=True)),
                ('jumlah', models.IntegerField(blank=True, max_length=5, null=True)),
                ('periode', models.CharField(blank=True, max_length=7, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'data_history',
            },
        ),
    ]