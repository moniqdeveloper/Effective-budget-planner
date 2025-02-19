from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Expense(models.Model):
    CATEGORIES = (
        ('Housing', 'Housing'),
        ('Transport', 'Transport'),
        ('Food', 'Food'),
        ('Utilities', 'Utilities'),
        ('Travel', 'Travel'),
        ('Medical', 'Medical & Healthcare'),
        ('Savings', 'Saving, Investing'),
        ('Clothes', 'Clothes'),
        ('Entertainment', 'Entertainment'),
        ('Other', 'Other'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=230, null=True, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField(default=now)
    category = models.CharField(max_length=30, choices=CATEGORIES)

    def __str__(self):
        return self.title

    class Meta:
        ordering: ['-date']
