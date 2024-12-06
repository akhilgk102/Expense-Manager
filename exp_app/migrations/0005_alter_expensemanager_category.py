# Generated by Django 4.2.16 on 2024-12-06 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp_app', '0004_alter_expensemanager_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensemanager',
            name='category',
            field=models.CharField(choices=[('Housing', 'Housing'), ('Transportation', 'Transportation'), ('Food', 'Food'), ('Healthcare', 'Healthcare'), ('Education', 'Education'), ('Entertainment', 'Entertainment'), ('Personal Care', 'Personal Care'), ('Debt Payments', 'Debt Payments'), ('Savings & Investments', 'Savings & Investments'), ('Gifts & Donations', 'Gifts & Donations'), ('Insurance', 'Insurance'), ('Travel', 'Travel'), ('Miscellaneous', 'Miscellaneous')], max_length=200),
        ),
    ]
