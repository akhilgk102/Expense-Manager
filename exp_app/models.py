from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    phone_number=models.CharField(max_length=12,unique=True)

    email=models.EmailField(unique=True)


class ExpenseManager(models.Model):

    title=models.CharField(max_length=200)

    category_options=(
    ('Housing', 'Housing'),
    ('Transportation', 'Transportation'),
    ('Food', 'Food'),
    ('Healthcare', 'Healthcare'),
    ('Education', 'Education'),
    ('Entertainment', 'Entertainment'),
    ('Personal Care', 'Personal Care'),
    ('Debt Payments', 'Debt Payments'),
    ('Savings & Investments', 'Savings & Investments'),
    ('Gifts & Donations', 'Gifts & Donations'),
    ('Insurance', 'Insurance'),
    ('Travel', 'Travel'),
    ('Miscellaneous', 'Miscellaneous'),

    )

    category=models.CharField(choices=category_options,max_length=200)

    amount=models.PositiveIntegerField()

    payment_options=(
        ("Cash","Cash"),
        ("Card","Card"),
        ("UPI","UPI"),
    )

    payment=models.CharField(max_length=200,choices=payment_options)

    owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True)




