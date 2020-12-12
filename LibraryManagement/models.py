from django.db import models
from django.contrib.auth.models import User


class Loan(models.Model):
    date_of_issue = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)

    borrower = models.ForeignKey(User, on_delete=models.CASCADE)


# Dauerleihgabe
class PermLoan(Loan):
    pass


# Ausleihe
class TempLoan(Loan):
    expected_return_date = models.DateField()



# Author
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class LoanSubject(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    loan_object = models.ManyToManyField(Loan)


# Bücher
class Book(LoanSubject):
    isbn = models.CharField(max_length=13)  # an isbn should be 13 chars long
    subject = models.CharField(max_length=50)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)


# Material
class Material(LoanSubject):
    pass


# Geräte
class Device(LoanSubject):
    device_type = models.CharField(max_length=50)


# Container
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
