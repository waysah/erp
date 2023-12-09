from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
import csv
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import ManagerForm, EmployeesForm,DailyWorkForm, CommisionSalaryForm, FixedSalaryForm, AllowancesForm, DeductionsForm, SalaryDetailsForm, JobTypeForm, CommissionTemplatesForm, ManageSalaryForm, SelectDepartmentForm, PayrollSummaryForm, AdvanceSalaryForm, OvertimeForm, EmployeeAwardForm, AddExpensesForm, DepartmentForm , first_departmentForm
from .models import Manager, Employees, Commision_saraly, Fixed_saraly, allowances, deductions, salary_details, job_type, commission_templates, ManageSalary, SelectDepartment, PayrollSummary, AdvanceSalary,  overtime, employeeAward, addExpenses, Department,DailyWork,first_department
from .models import Transaction
from django.db.models import Count,Sum,Max,Min,Avg

departments = Employees.objects.all()
managers = Manager.objects.all()
commision_saralies =  Commision_saraly.objects.all()
fixed_salaries = Fixed_saraly.objects.all()
allowanceses = allowances.objects.all()
deduction = deductions.objects.all()
salary_detail = salary_details.objects.all()
job_types = job_type.objects.all()
commission_template = commission_templates.objects.all()
manageSalaries =  ManageSalary.objects.all()
SelectDepartments = SelectDepartment.objects.all()
PayrollSummaries =  PayrollSummary.objects.all()
advanceSalaries =  AdvanceSalary.objects.all()
departments = Department.objects.all()
dailyWorks = DailyWork.objects.all()
first_departments = first_department.objects.all()
employees = Employees.objects.all()
context = {
        'employees' : employees,
        'departments' : departments,
        'managers' : managers,
        'commision_saralies' : commision_saralies,
        'fixed_salaries' :  fixed_salaries,
        'allowanceses' :  allowanceses,
        ' deductions' :  deduction,
        'salary_details' : salary_detail,
        'job_types' : job_types,
        'commission_templates' : commission_template,
        'manageSalaries ' :  manageSalaries,
        'SelectDepartments' :  SelectDepartments,
        'PayrollSummaries' : PayrollSummaries,
        'advanceSalaries' : advanceSalaries,
        'dailyWorks ' :  dailyWorks,
        'first_departments' :  first_departments
        }


def addEmployee(request):
    if request.method == 'POST':
        form = EmployeesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = EmployeesForm()
        context = {
                'form' : form
             }
    return render(request, 'Dashboard/addEmployee.html',context)

def employeeList(request):
    employees = Employees.objects.all()
    employees_number = Employees.objects.count()
    context = {
        'employees' : employees,
        'employees_number' : employees_number
    }
    return render(request, 'Dashboard/employeeList.html', context)

def removeEmployee(request):
    employees = Employees.objects.all()
    employees_number = Employees.objects.count()
    context = {
        'employees' : employees,
        'employees_number' : employees_number
    }
    return render(request,'Dashboard/employeeList.html',context)


def employee_detail(request, pk):
    employee = get_object_or_404(Employees, pk=pk)
    return render(request, 'Dashboard/employee_detail.html',  {'employee': employee})

def employee_update(request, pk):
    employee = get_object_or_404(Employees,  pk=pk)
    if request.method == 'POST':
        form = EmployeesForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = EmployeesForm(instance=employee)
    return render(request, 'Dashboard/addEmployee.html',{'form': form})

def employee_delete(request,pk):
        employee = get_object_or_404(Employees, pk=pk)
        employee.delete()
        return redirect('/home')


def deleteAllEmployees(request):
    delete_employees = Employees.objects.all().delete()
    return redirect('/home/employeeList')


def create_employees():
    pass

