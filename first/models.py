from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db.models import Count, Avg, Max, Min, Sum
from django.db.models.signals import post_save
from django.dispatch import receiver

Employees = get_user_model()
Department = get_user_model()
job_type = get_user_model()

class Manager(models.Model):
    MANAGER_STATUS = (
        ('ACTIVE','Active'),

        ('DORMANT','Dormant'),
    )
    EMPLOYEE_LEVER = (
        ('CEO', 'CEO'),
        ('MANAGER', 'Manager'),
    )
    employee_id = models.IntegerField()
    first_name = models.CharField(max_length=255,blank=True)
    middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255,blank=True)
    username = models.CharField(max_length=128,blank=True)
    password = models.IntegerField()
    confirm_password = models.IntegerField()
    status = models.CharField(max_length=50, choices=MANAGER_STATUS)
    employee_level = models.CharField(max_length=100, choices=EMPLOYEE_LEVER)
    profile_image = models.ImageField(upload_to='upload/',  default = 'a.png',  blank=True, null=True)
    bio_descrption = models.TextField(blank=True)

class Employees(models.Model):
    SALARY_TYPE_CHOICES = (
        ('COMMISION', 'Commision'),
        ('FIXED', 'Fixed'),
    )
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    Employement_id = models.IntegerField()
    Email = models.EmailField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    kra_pin = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='upload/', default = 'a.png', blank=True, null=True)
    front_id_image = models.ImageField(upload_to='upload/',  default = 'a.png' ,  blank=True, null=True)
    back_id_image = models.ImageField(upload_to='upload/',  default = 'a.png',  blank=True, null=True)
    salary_type=models.CharField(max_length=255,blank=True, choices=SALARY_TYPE_CHOICES)
    department = models.ForeignKey("Department", on_delete=models.CASCADE, related_name='employees')
    next_of_kin_first_name = models.CharField(max_length=255, blank=True, null=True)
    next_of_kin_middle_name =models.CharField(max_length=255, blank=True, null=True)
    next_of_kin_last_name = models.CharField(max_length=255, blank=True, null=True)
    next_of_kin_national_id = models.IntegerField( blank=True, null=True)
    next_of_kin_relationship = models.CharField(max_length=255, blank=True, null=True)
    next_of_kin_phone_number = models.IntegerField(blank=True, null=True)
    next_of_kin_email = models.EmailField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    total_income = models.IntegerField(default=0, blank=True)


    def __str__(self):
        return self.first_name

    def calculate_total_income(self):
        total_company_income=0;
        total_company_income = self.total_income+total_company_income
        return total_company_income




class employee_initializer(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    consolidated_employee_income = models.IntegerField(default=0, blank=True)
    all_amount_income = models.IntegerField(default=0, blank=True)
    company_amount_income = models.IntegerField(default=0, blank=True)

class Commision_saraly(models.Model):
    id = models.IntegerField(primary_key=True)
    job_type = models.CharField(max_length = 255, blank="True")
    department = models.ForeignKey("Department",on_delete = models.CASCADE)

    def __str__(self):
        return self.job_type

class Fixed_saraly(models.Model):
    pass

class allowances(models.Model):
    house_allowance = models.FloatField()
    medical_allowance = models.FloatField()

class deductions(models.Model):
    provident_fund = models.FloatField()
    tax_deduction = models.FloatField()

class salary_details(models.Model):
    gross_salary = models.FloatField()
    house_allowances = models.FloatField()
    medical_allowance = models.FloatField()
    provident_fund = models.FloatField()
    tax_deductions = models.FloatField()
    id = models.IntegerField(primary_key=True)

    #job type replaced with commision_salary model
class job_type(models.Model):
    pass

class ManageSalary(models.Model):
    employee= models.ForeignKey("Employees", on_delete=models.CASCADE)
    job_type = models.ForeignKey("job_type", on_delete=models.CASCADE)
    amount = models.FloatField()

class SelectDepartment(models.Model):
    department = models.ForeignKey("Department", on_delete=models.CASCADE)
    select_month = models.DateField()

class PayrollSummary(models.Model):
    employeeId= models.ForeignKey("Employees", on_delete=models.CASCADE)

class AdvanceSalary(models.Model):
    employee_name = models.ForeignKey("Employees", on_delete=models.CASCADE)
    amount = models.FloatField()
    month = models.DateTimeField(blank=True,auto_now_add=True)
    reason = models.TextField(blank=True)

class overtime(models.Model):
    employee_id =  models.ForeignKey("Employees", on_delete=models.CASCADE)
    date = models.DateTimeField()
    Hour = models.DurationField()
    Text = models.TextField()

class employeeAward(models.Model):
    employee_name =  models.ForeignKey("Employees", on_delete=models.CASCADE)
    gift_item = models.CharField(max_length=200)
    award_date = models.DateTimeField(auto_now_add=True)

class addExpenses(models.Model):
    expense_name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    text = models.TextField()

class Department(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class first_department(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)


class DailyWork(models.Model):
    PAYEMENT_CHOICES = (
        ('M-PESA', 'm-pesa'),
        ('CASH', 'cash'),
        )
    employee_ID =  models.ForeignKey("Employees", on_delete=models.CASCADE)
    total_amount = models.FloatField()
    job_type = models.ForeignKey("Commision_saraly", on_delete=models.CASCADE)
    department = models.ForeignKey("Department", on_delete=models.CASCADE, null=True, blank=True)
    commision_rate = models.IntegerField()
    date = models.DateTimeField(blank=True, null=True)
    Payement_method = models.CharField(max_length=255, choices=PAYEMENT_CHOICES, null=True, blank=True)
    paid = models.BooleanField(default=True)


    def calculate_employee_income(self):
        total_income = 0
        employee_income = self.commision_rate/100 * self.total_amount
        total_income += employee_income
        return total_income
    def calculate_total_amount(self):
        pass


    def __str__(self):
        return self.employee_income



class Employee(models.Model):
    name = models.CharField(max_length=255)
    total_amount = models.FloatField()

    def calculate_commission(self, period):
        if period == 'daily':
            commission_rate = 0.35
        elif period == 'weekly':
            commission_rate = 0.35 * 7
        elif period == 'monthly':
            commission_rate = 0.35 * 30


        commission = self.total_amount * commission_rate
        return commission

    def remaining_amount(self, period):
        commission = self.calculate_commission(period)
        remaining_amount = self.total_amount - commission
        return remaining_amount

class Transaction(models.Model):
    ACCOUNT_TYPES = (
        ('ASSETS', 'Assets'),
        ('LIABILITIES', 'Liabilities'),
        ('EQUITY', 'Equity'),
        ('REVENUE', 'Revenue'),
        ('EXPENSE', 'Expense'),
    )

    account = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=1000, choices=ACCOUNT_TYPES)

class commision_rate (models.Model):
  pass


#replaced with commission salary model
class commission_templates(models.Model):
   pass

class nextofkin(models.Model):
    national_id = models.CharField(max_length = 255)
    first_name = models.CharField(max_length = 255)
    middle_name= models.CharField(max_length = 255)
    last_name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.IntegerField()


class first_employees(models.Model):
    SALARY_TYPE_CHOICES = (
        ('COMMISION', 'Commision'),
        ('FIXED', 'Fixed'),
    )
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    Employement_id = models.IntegerField()
    Email = models.EmailField()
    phone_number = models.IntegerField()
    kra_pin = models.IntegerField()
    image = models.ImageField(upload_to='upload', default = 'a.png')
    front_id_image = models.ImageField(upload_to='upload',  default = 'a.png')
    back_id_image = models.ImageField(upload_to='upload',  default = 'a.png')
    salary_type=models.CharField(max_length=255,blank=True, choices=SALARY_TYPE_CHOICES)
    department = models.ForeignKey("Department", on_delete=models.CASCADE)
    date = models.DateField()

class payslip(models.Model):
    date = models.DateField()


class financialreport(models.Model):
    date = models.DateTimeField()
    total_income = models.IntegerField()
    employee_income = models.IntegerField()
    net_income = models.IntegerField()

class daily_results(models.Model):
    date = models.DateField("auto_now_add=True", null=True, blank=True)
    total_results = models.IntegerField(null=True, blank=True)

class department_employee_view(models.Model):
    date = models.DateTimeField()

class debit(models.Model):
    employee_name = models.ForeignKey("Employees", on_delete=models.CASCADE)
    amount = models.FloatField()
    month = models.DateTimeField(blank=True,auto_now_add=True)
    reason = models.TextField(blank=True)

class system_update(models.Model):
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_logo = models.ImageField(upload_to='upload/',  default = 'a.png',blank=True, null=True)
    
class payement_gateway(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(max_length=255, blank=True, null=True)
    
class system_payment(models.Model):
    Amount = models.CharField(max_length=255, blank=True, null=True)
    payment_method = models.ForeignKey("Employees", on_delete=models.CASCADE, blank=True, null=True)
    