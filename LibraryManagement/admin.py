from django.contrib import admin
from LibraryManagement.models import *


to_register = [Loan, PermLoan, TempLoan, Author, LoanSubject, Book, Material, Device, Container]

for model in to_register:
    admin.site.register(model)
