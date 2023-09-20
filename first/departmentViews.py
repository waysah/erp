from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
import csv
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import ManagerForm, EmployeesForm,DailyWorkForm, CommisionSalaryForm, FixedSalaryForm, AllowancesForm, DeductionsForm, SalaryDetailsForm, JobTypeForm, CommissionTemplatesForm, ManageSalaryForm, SelectDepartmentForm, PayrollSummaryForm, AdvanceSalaryForm, OvertimeForm, EmployeeAwardForm, AddExpensesForm, DepartmentForm , first_departmentForm
from .models import Manager, Employees, Commision_saraly, Fixed_saraly, allowances, deductions, salary_details, job_type, commission_templates, ManageSalary, SelectDepartment, PayrollSummary, AdvanceSalary,  overtime, employeeAward, addExpenses, Department,DailyWork,first_department
from fpdf import FPDF
from .models import Transaction



def removeDepartment(request,id):
    if request.method == 'POST':
        department = Department.objects.get(id=id)
        department.delete()
        return redirect('/home')
    return render(request,'Dashboard/manageDepartments.html')

def addDepartment(request):
    if request.method == 'POST':
        form =  DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    form = DepartmentForm(request.POST)
    return render(request,'Dashboard/addDepartment.html', {'form' : form})


def departmentList(request):
    departments = Department.objects.all()
    context = {'departments' : departments}
    return render(request,'Dashboard/manageDepartments.html', context)

def update_department(request, pk):
    department = Department.objects.get(pk=pk)
    if request.method == 'POST':
          department.delete()
          return redirect('/home')
    return render(request,'Dashboard/department_update.html')

def manageDepartments(request):
    return render(request, 'Dashboard/ManageDepartments.html')

def department_view(request, id):
    department = get_object_or_404(Department,id=id)
    context = {
        'department' : department
    }
    return render(request, 'Dashboard/department_view.html', context)


def departments_delete(request):
    if request.method == 'POST':
        departments_delete = Department.objects.all().delete()
        return redirect('/home')
    else:
        return render(request, 'Dashboard/ManageDepartments.html')

def department_detail(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    employees = department.employees.all()
    return render(request, 'Dashboard/department_detail.html', {'department': department, 'employees':employees})
