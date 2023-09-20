from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.db.models import Count,Sum,Max,Min,Avg
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
import csv
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import ManagerForm, EmployeesForm,DailyWorkForm, CommisionSalaryForm, FixedSalaryForm, AllowancesForm, DeductionsForm, SalaryDetailsForm, JobTypeForm, CommissionTemplatesForm, ManageSalaryForm, SelectDepartmentForm, PayrollSummaryForm, AdvanceSalaryForm, OvertimeForm, EmployeeAwardForm, AddExpensesForm, DepartmentForm , first_departmentForm,EmployeeForm,employee_initializerForm
from .models import Manager, Employees, Commision_saraly, Fixed_saraly, allowances, deductions, salary_details, job_type, commission_templates, ManageSalary, SelectDepartment, PayrollSummary, AdvanceSalary,  overtime, employeeAward, addExpenses, Department,DailyWork,first_department,Employee
from fpdf import FPDF
from .models import Transaction, employee_initializer, debit
from django.urls import path,include
from django.db.models import Count,Sum,Max,Min,Avg
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models.functions import TruncDate
from .forms import debitForm



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
dailyworks = DailyWork.objects.all()
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
        'dailyworks ' :  dailyworks,
        'first_departments' :  first_departments
        }
# Create your views here.

def index(request):
    employees = Employees.objects.all()
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
    dailywork_sum = DailyWork.objects.all()
    first_departments = first_department.objects.all()
    employees_number = Employees.objects.count()
    departments_count = Department.objects.count()
    job_count = Commision_saraly.objects.count()
    employee_initializer_income = employee_initializer.objects.all()
    employees = Employees.objects.all()
    time = datetime.now()
    all_amount = DailyWork.objects.aggregate(all_amount = Sum('total_amount'))['all_amount']
    mpesa_income = DailyWork.objects.filter(Payement_method__startswith='M-PESA').aggregate(mpesa_income=Sum('Payement_method'))['mpesa_income']
    total_company_income = Employees.objects.aggregate(total_company_income = Sum('total_income'))['total_company_income']
    net_income = all_amount-total_company_income
    cash_income = DailyWork.objects.filter(Payement_method__startswith='cash').aggregate(cash_income=Sum('Payement_method'))['cash_income']
    context = {
        'employee_initializer_income' : employee_initializer_income,
        'job_count' : job_count,
        'departments_count' : departments_count,
        'employees_number' : employees_number,
        'employees' : employees,
        'departments' : departments,
        'managers' : managers,
        'commision_saralies' : commision_saralies,
        'fixed_salaries' :  fixed_salaries,
        'allowanceses' :  allowanceses,
        'deductions' :  deduction,
        'salary_details' : salary_detail,
        'job_types' : job_types,
        'commission_templates' : commission_template,
        'manageSalaries ' :  manageSalaries,
        'SelectDepartments' :  SelectDepartments,
        'PayrollSummaries' : PayrollSummaries,
        'advanceSalaries' : advanceSalaries,
        'dailywork_sum ' :  dailywork_sum,
        'first_departments' :  first_departments,
        'employees': employees,
        'time' : time,
        'all_amount' : all_amount,
        'net_income' : net_income,
        'mpesa_income' : mpesa_income,
        'total_company_income' : total_company_income,
        'cash_income' : cash_income
    #    'total_income': total_income
    }
    return render(request, 'Dashboard/index.html', context)


def calculate_income(request, dailywork_id):
    dailywork = DailyWork.objects.get(pk=dailywork_id)
    total_income = dailywork.calculate_employee_income()
    context = {'total_income': total_income}
    return render(request, 'Dashboard/personalAccount.html', context)

def personalAccount(request):
    return render(request,'Dashboard/personalAccount.html')

def salaryTemplates(request):
    return render(request, 'Dashboard/salaryTemplates.html' , context)

#job type form post
def commisionTemplates(request):
    if request.method == 'POST':
        form = CommisionSalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/jobtypes')
    else:
        form = CommisionSalaryForm()
        context = {
            'form' : form
        }
    return render(request, 'Dashboard/commisionTemplates.html', {'form' : form})

def jobTypes(request):
    jobs = Commision_saraly.objects.all()
    context = {
        'jobs' : jobs
    }
    return render(request, 'Dashboard/jobtypes.html',{'jobs' : jobs})

def jobtypes_delete(request):
    if request.method == 'POST':
        Commision_saraly.objects.all().delete()
        return redirect('/home/jobtypes')
    else:
        return render(request, 'Dashboard/jobtypes.html')


def jobtype_delete(request,pk):
    if request.method == 'POST':
        jobtype = get_object_or_404('Commision_salary', pk=pk)
        jobtype.delete()
    else:
        return render(request, 'Dashboard/jobtype.html')

def jobtype_edit(request, pk):
    pass

def manageSalary(request):
    form = ManageSalaryForm()
    if request.method == 'POST':
        form=ManageSalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
        else:
            form=ManageSalaryForm()

    return render(request,'Dashboard/manageSalary.html', {'form' : form})

def employeeSalaryList(request):
    employees = Employees.objects.all()
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
    return render(request, 'Dashboard/employeeSalaryList.html', context)

def makePayment(request):
    return render(request, 'Dashboard/makePayment.html', context)

def search_bar(request):
    return render(request, 'Dashboard/index.html')

def payrollSummary(request):
    employees = Employees.objects.all()
    context = {
        'employees' : employees
    }
    return render (request, 'Dashboard/payrollSummary.html', context)

def advanceSalary(request):
    if request.method == 'POST':
        form = AdvanceSalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/advancesalary_list')
    else:
        form = AdvanceSalaryForm()
        context={
            'form' : form
        }
    return render(request, 'Dashboard/advanceSalary.html',context)

def advancesalary_list(request):
    advancesalary_lists = AdvanceSalary.objects.all()
    return render(request,'Dashboard/advancesalary_list.html', {'advancesalary_lists' : advancesalary_lists})

def advancesalary_delete_all(request):
    advancesalary_delete_all = AdvanceSalary.objects.delete()
    return redirect('/home/advancesalary_list')

def providentFund(request):
    return render(request, 'Dashboard/providentFund.html', context)


def commisionList(request):
    return render(request,'Dashboard/commisionList.html')

def makePaymentList(request):
    employees = Employees.object.all()
    context = {
        'employees' : employees
    }
    return render(request, 'Dashboard/makePayementList.html', context)

def manageSalaryList(request):
    employees = Employees.objects.all()
    persentage_commision = Commision_saraly.objects.all()
    context = {
        'employees' : employees,
        'persentage_commisions' : persentage_commision
        }
    return render(request, 'Dashboard/manageSalaryList.html', context)

def set_tax(request):
    return render(request,'Dashboard/commisionTemplates.html', context)


#end of daily record


def salary_report(request, period):
    employees = Employees.objects.all()
    context = {
        'employees': employees,
        'period': period,
    }
    return render(request, 'Dashboard/salary_report.html', context)


def dailyReports(request):
    return render(request, 'Dashboard/dailyReports.html', context)


def monthlyReports(request):
    employees = Employees.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'Dashboard/monthlyReports.html', context)


def yearlyReports(request):
    time = datetime.now()
    employees = Employees.objects.all()
    context = {
        'employees': employees,
        'time' : time,
    }
    return render(request , 'Dashboard/yearlyReports.html', context)


def needHelp(request):
    return render(request,'Dashboard/needHelp.html')



def profile(request):
    managers =  Manager.objects.all()
    context = {
        'managers' : managers
    }
    return render(request, 'Dashboard/profile.html', context)



def profileDelete(request):
    if request.method == 'POST':
        managers = Manager.objects.all().delete()
        return redirect('/home')
    return render(request, 'Dashboard/settings.html')



def logout(request):
   return redirect('/')



def employeee_initializer(request):
    if request.method == 'POST':
        form = employee_initializerForm(request.POST)  # Instantiate the form with request.POST data
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = employee_initializerForm()
    return render(request, 'Dashboard/employeee_initializer.html', {'form': form})

def financialreport(request):
    employees = Employees.objects.all()
    time = datetime.now()
    all_amount = DailyWork.objects.aggregate(all_amount = Sum('total_amount'))['all_amount']
    mpesa_income = DailyWork.objects.filter(Payement_method__startswith='M-PESA').aggregate(mpesa_income=Sum('Payement_method'))['mpesa_income']
    total_company_income = Employees.objects.aggregate(total_company_income = Sum('total_income'))['total_company_income']
    net_income = all_amount-total_company_income
    cash_income = DailyWork.objects.filter(Payement_method__startswith='cash').aggregate(cash_income=Sum('Payement_method'))['cash_income']

    context = {
        'employees': employees,
        'time' : time,
        'all_amount' : all_amount,
        'net_income' : net_income,
        'mpesa_income' : mpesa_income,
        'total_company_income' : total_company_income,
        'cash_income' : cash_income,

    }
    return render(request, 'Dashboard/financialreport.html', context)

def debit_create(request):
    form = debitForm(request.POST)
    if request.method == 'POST':
        form = debitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        form = debitForm(request.POST)
    context = {
            'form': form
            }
    return render(request, 'Dashboard/debit_create.html', context)

def debit_view(request):
    debits = debit.objects.all()
    context = {
        'debits' : debits
        }
    return render(request, 'Dashboard/debit_view.html', context)

def debit_delete_all(request):
    if request.method == 'POST':
        debit.objects.all().delete()
        return redirect('/')
