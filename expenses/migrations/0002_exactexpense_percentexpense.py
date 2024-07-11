# Generated by Django 5.0.3 on 2024-03-13 18:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExactExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share', models.DecimalField(decimal_places=2, max_digits=10)),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenses.expense')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenses.user')),
            ],
        ),
        migrations.CreateModel(
            name='PercentExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenses.expense')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenses.user')),
            ],
        ),
    ]
