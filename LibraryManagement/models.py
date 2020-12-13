from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Loan(models.Model):
    date_of_issue = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    borrower = models.ForeignKey(User, on_delete=models.CASCADE)


class PermLoan(Loan):
    def __str__(self):
        return "{0.borrower.first_name} {0.borrower.last_name} - {0.date_of_issue}".format(self)


class TempLoan(Loan):
    expected_return_date = models.DateField()

    def is_overdue(self):
        return self.expected_return_date < date.today()

    def __str__(self):
        return "{0.borrower.first_name} {0.borrower.last_name} - {0.date_of_issue}".format(self)


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return "{0.first_name} {0.last_name}".format(self)


class LoanSubject(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    image = models.ImageField(upload_to="static/uploads/", default=None, null=True)

    loans = models.ManyToManyField(Loan, blank=True)

    def active_loan(self):
        return self.loans.get(return_date__isnull=True)

    def is_available(self):
        try:
            self.active_loan()
            return False
        except Loan.DoesNotExist:
            return True

    def __str__(self):
        return self.name


class Book(LoanSubject):
    isbn = models.CharField(max_length=13)  # an isbn should be 13 chars long
    subject = models.CharField(max_length=50)
    release_date = models.DateField()

    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Material(LoanSubject):
    pass


class Device(LoanSubject):
    device_type = models.CharField(max_length=50)


class Container(LoanSubject):
    pass


"""
To create a loan object with a loan subject:

from LibraryManagement.models import *
from django.utils import timezone

loan = TempLoan(date_of_issue=timezone.now(), borrower=User.objects.get(pk={the pk of the desired user}))
loan.save()

mat = Material(name="Material", description="Description")
mat.save()
mat.loan_object.add(loan)    # creates the n:m relation ship


Note: 
'TempLoan' can be substitued with any 'Loan' model.
'Material' can be substituted with any of the 'LoanSubject' model.


Queries:
Get all loans for the material: mat.loan_object.all()
Get all subjects for the loan: loan.loansubject_set.all()
"""
