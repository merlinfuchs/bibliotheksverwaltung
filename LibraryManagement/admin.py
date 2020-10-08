from django.contrib import admin
from LibraryManagement.models import *

# Register your models here.
admin.site.register(Loan)
admin.site.register(PermLoan)
admin.site.register(TempLoan)
admin.site.register(Author)
admin.site.register(LoanSubject)
admin.site.register(Book)
admin.site.register(Material)
admin.site.register(Device)
admin.site.register(Container)


