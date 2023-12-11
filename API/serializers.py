from rest_framework import serializers
from first.models import *

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        models = Manager 
        fields = "__all__"

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        models = Employees
        fields = "__all__"

class employee_initializerSerializer(serializers.ModelSerializer):
    class Meta:
        models = employee_initializer
        fields = "__all__"

class Commision_saralySerializer(serializers.ModelSerializer):
    class Meta:
        models = Commision_saraly
        fields = "__all__"

class Fixed_saralySerializer(serializers.ModelSerializer):
    class Meta:
        models = Fixed_saraly
        fields = "__all__"

class allowancesSerializer(serializers.ModelSerializer):
    class Meta:
        models = allowances
        fields = "__all__"

class deductionsSerializer(serializers.ModelSerializer):
    class Meta:
        models  = deductions
        fields = "__all__"

class salary_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        models = salary_details
        fields = "__all__"

class job_typeSerializer(serializers.ModelSerializer):
    class Meta:
        models = salary_details
        fields = "__all__"

class SelectDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        models = SelectDepartment
        fields = "__all__"

class PayrollSummarySerializer(serializers.ModelSerializer):
    class Meta:
        models = PayrollSummary
        fields  = "__all__"

class AdvanceSalarySerializer(serializers.ModelSerializer):
    class Meta:
        models = AdvanceSalary
        fields = "__all__"

class overtimeSerializer(serializers.ModelSerializer):
    class Meta:
        models = overtime
        fields = "__all__"

class employeeAwardSerializer(serializers.ModelSerializer):
    class Meta:
        models = employeeAward
        fields = "__all__"

class addExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        models = addExpenses
        fields = "__all__"

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Department
        fields  = "__all__"

class first_departmentSerializer(serializers.ModelSerializer):
    class Meta:
        models = first_department
        fields = "__all__"

class DailyWorkSerializer(serializers.ModelSerializer):
    class Meta:
        models = DailyWork
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        models = Employee
        fields = "__all__"

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        models = Transaction
        fields = "__all__"

class  commision_rateSerializer(serializers.ModelSerializer):
    class Meta:
        models =  commision_rate 
        fields = "__all__"

class commission_templatesSerializer(serializers.ModelSerializer):
    class Meta:
        models = commission_templates
        fields = "__all__"

class nextofkinSerializer(serializers.ModelSerializer):
    class Meta:
        models = nextofkin
        fields = "__all__"

class first_employeesSerializer(serializers.ModelSerializer):
    class Meta:
        models = first_employees
        fields = "__all__"

class payslipSerializer(serializers.ModelSerializer):
    class Meta:
        models = payslip
        fields = "__all__"

class financialreportSerializer(serializers.ModelSerializer):
    class Meta:
        models = financialreport
        fields = "__all__"

class daily_resultsSerializer(serializers.ModelSerializer):
    class Meta:
        models = daily_results
        fields = "__all__"

class department_employee_viewSerializer(serializers.ModelSerializer):
    class Meta:
        models = department_employee_view
        fields = "__all__"

class debitSerializer(serializers.ModelSerializer):
    class Meta:
        models = debit
        fields = "__all__"

class system_updateSerializer(serializers.ModelSerializer):
    class Meta:
        models = system_update
        fields = "__all__"

class payement_gatewaySerializer(serializers.ModelSerializer):
    class Meta:
        models = payement_gateway
        fields = "__all__"

class system_paymentSerializer(serializers.ModelSerializer):
    class Meta:
        models = system_payment
        fields = "__all__"