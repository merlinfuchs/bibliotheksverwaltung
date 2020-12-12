from django.contrib import admin
from django import forms
from LibraryManagement.models import *
from django.http import HttpResponseRedirect
from datetime import datetime


to_register = [PermLoan, TempLoan, Author, Book, Material, Device, Container]


class LoanSubjectForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = LoanSubject
        exclude = ["loans"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


def print_code(modeladmin, request, queryset):
    selected = queryset.values_list("pk", flat=True)
    return HttpResponseRedirect(f"/print?ids={','.join([str(pk) for pk in selected])}")


class AuthorFilter(admin.SimpleListFilter):
    title = "author"
    parameter_name = 'author'

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(author__id__exact=self.value())
        else:
            return queryset

    def lookups(self, request, model_admin):
        authors = set([b.author for b in model_admin.model.objects.all()])
        return [(a.id, f"{a.first_name} {a.last_name}") for a in authors]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    form = LoanSubjectForm
    list_display = ("name", "author")
    list_filter = (AuthorFilter,)
    search_fields = ("name",)
    actions = (print_code,)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    form = LoanSubjectForm
    list_display = ("name", "device_type")
    list_filter = ("device_type",)
    actions = (print_code,)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    form = LoanSubjectForm
    list_display = ("name",)
    actions = (print_code,)


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    form = LoanSubjectForm
    list_display = ("name",)
    actions = (print_code,)


class LoanSubjectInline(admin.TabularInline):
    model = LoanSubject.loans.through
    extra = 1


class ReturnedFilter(admin.SimpleListFilter):
    title = "status"
    parameter_name = 'status'

    def queryset(self, request, queryset):
        if self.value() == 'open':
            return queryset.filter(return_date__isnull=True)
        elif self.value() == 'returned':
            return queryset.filter(return_date__isnull=False)
        elif self.value() == 'overdue':
            try:
                return queryset.filter(return_date__isnull=True, expected_return_date__lt=datetime.now())
            except:
                return None
        else:
            return queryset

    def lookups(self, request, model_admin):
        return [('open', 'Open'), ('returned', 'Returned'), ('overdue', 'Overdue')]


@admin.register(TempLoan)
class TempLoanAdmin(admin.ModelAdmin):
    inlines = (LoanSubjectInline,)
    list_filter = (ReturnedFilter,)
    list_display = ('borrower', 'date_of_issue', 'expected_return_date', 'return_date')


@admin.register(PermLoan)
class PermLoanAdmin(admin.ModelAdmin):
    inlines = (LoanSubjectInline,)
    list_filter = (ReturnedFilter,)
    list_display = ('borrower', 'date_of_issue', 'return_date')
