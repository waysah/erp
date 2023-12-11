from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from rest_framework import generics
from first.models import *
from .serializers import *

# Create your views here.

def api_index(request):
    return HttpResponse("hello api")


class ManagerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset  = Manager.objects.all()
    serializer_class = ManagerSerializer

class ManagerListCreateView(generics.ListCreateAPIView):
    queryset  = Manager.objects.all()
    serializer_class = ManagerSerializer

class EmployeesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

class EmployeesListCreateView(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

class employee_initializerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = employee_initializer.objects.all()
    serializer_class = employee_initializerSerializer

class employee_initializerListCreateView(generics.ListCreateAPIView):
    queryset = employee_initializer.objects.all()
    serializer_class = employee_initializerSerializer

class commision_salaryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commision_saraly.objects.all()
    serializer_class = Commision_saralySerializer

class commision_salaryListCreateView(generics.ListCreateAPIView):
    queryset  = Commision_saraly.objects.all()
    serializer_class = Commision_saralySerializer

class Fixed_saralyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fixed_saraly.objects.all()
    serializer_class = Fixed_saralySerializer

class Fixed_saralyListCreateView(generics.ListCreateAPIView):
    queryset = Fixed_saraly.objects.all()
    serializer_class = Fixed_saralySerializer

class allowancesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = allowances.objects.all()
    serializer_class = allowancesSerializer

class allowancesListCreateView(generics.ListCreateAPIView):
    queryset = allowances.objects.all()
    serializer_class = allowancesSerializer

class deductionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = deductions.objects.all()
    serializer_class = deductionsSerializer

class deductionListCreateView(generics.ListCreateAPIView):
    queryset = deductions.objects.all()
    serializer_class = deductionsSerializer

class salary_detailsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset  = salary_details.objects.all()
    serializer_class = salary_detailsSerializer

class salary_detailsListCreateView(generics.ListCreateAPIView):
    queryset = salary_details.objects.all()
    serializer_class = salary_detailsSerializer

class job_typeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset  = job_type.objects.all()
    serializer_class = job_typeSerializer

class job_typeListCreateView(generics.ListCreateAPIView):
    queryset = job_type.objects.all()
    serializer_class = job_typeSerializer

class SelectDepartmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SelectDepartment.objects.all()
    serializer_class = SelectDepartmentSerializer

class SelectDepartmentListCreateView(generics.ListCreateAPIView):
    queryset = SelectDepartment.objects.all()
    serializer_class = SelectDepartmentSerializer

class PayrollSummaryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PayrollSummary.objects.all()
    serializer_class = PayrollSummarySerializer

class PayrollSummaryListCreateView(generics.ListCreateAPIView):
    queryset = PayrollSummary.objects.all()
    serializer_class = PayrollSummarySerializer

class AdvanceSalaryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdvanceSalary.objects.all()
    serializer_class = AdvanceSalarySerializer

class AdvanceSalaryListCreateView(generics.ListCreateAPIView):
    queryset = AdvanceSalary.objects.all()
    serializer_class = AdvanceSalarySerializer

class overtimeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = overtime.objects.all()
    serializer_class = overtimeSerializer

class overtimeListCreateView(generics.ListCreateAPIView):
    queryset = overtime.objects.all()
    serializer_class = overtimeSerializer

class employeeAwardRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = employeeAward.objects.all()
    serializer_class = employeeAwardSerializer

class employeeAwardListCreateView(generics.ListCreateAPIView):
    queryset = employeeAward.objects.all()
    serializer_class = employeeAwardSerializer

class addExpensesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = addExpenses.objects.all()
    serializer_class = addExpensesSerializer

class addExpensesListCreateView(generics.ListCreateAPIView):
    queryset = addExpenses.objects.all()
    serializer_class = addExpensesSerializer

class DepartmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class first_departmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = first_department.objects.all()
    serializer_class = first_departmentSerializer

class first_departmentListCreateView(generics.ListCreateAPIView):
    queryset = first_department.objects.all()
    serializer_class = first_departmentSerializer

class DailyWorkRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyWork.objects.all()
    serializer_class = DailyWorkSerializer

class DailyWorkListCreateView(generics.ListCreateAPIView):
    queryset = DailyWork.objects.all()
    serializer_class = DailyWorkSerializer

class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class commision_rateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = commision_rate.objects.all()
    serializer_class = commision_rateSerializer

class commision_rateListCreateView(generics.ListCreateAPIView):
    queryset = commision_rate.objects.all()
    serializer_class = commision_rateSerializer

class commission_templatesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = commission_templates.objects.all()
    serializer_class = commission_templatesSerializer

class commission_templatesListCreateView(generics.ListCreateAPIView):
    queryset = commission_templates.objects.all()
    serializer_class = commission_templatesSerializer

class nextofkinRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = nextofkin.objects.all()
    serializer_class = nextofkinSerializer

class nextofkinListCreateView(generics.ListCreateAPIView):
    queryset = nextofkin.objects.all()
    serializer_class = nextofkinSerializer

class first_employeesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = first_employees.objects.all()
    serializer_class = first_employeesSerializer

class first_employeesListCreateView(generics.ListCreateAPIView):
    query = first_employees.objects.all()
    serializer_class = first_employeesSerializer

class payslipRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = payslip.objects.all()
    serializer_class = payslipSerializer

class payslipListCreateView(generics.ListCreateAPIView):
    queryset = payslip.objects.all()
    serializer_class = payslipSerializer

class financialreportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = financialreport.objects.all()
    serializer_class = financialreportSerializer

class financialreportListCreateView(generics.ListCreateAPIView):
    queryset = financialreport.objects.all()
    serializer_class = financialreportSerializer

class daily_resultsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = daily_results.objects.all()
    serializer_class = daily_resultsSerializer

class daily_resultsListCreateView(generics.ListCreateAPIView):
    queryset = daily_results.objects.all()
    serializer_class = daily_resultsSerializer

class department_employee_viewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = department_employee_view.objects.all()
    serializer_class = department_employee_viewSerializer

class department_employee_viewListCreateView(generics.ListCreateAPIView):
    queryset = department_employee_view.objects.all()
    serializer_class = department_employee_viewSerializer

class debitRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = debit.objects.all()
    serializer_class = debitSerializer

class debitListCreateView(generics.ListCreateAPIView):
    queryset = debit.objects.all()
    serializer_class = debitSerializer

class system_updateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset  = system_update.objects.all()
    serializer_class = system_updateSerializer

class system_updateListCreateView(generics.ListCreateAPIView):
    queryset = system_update.objects.all()
    serializer_class = system_updateSerializer

class payement_gatewayRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = payement_gateway.objects.all()
    serializer_class = payement_gatewaySerializer

class payement_gatewayListCreateView(generics.ListCreateAPIView):
    queryset = payement_gateway.objects.all()
    serializer_class = payement_gatewaySerializer

class system_paymentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = system_payment.objects.all()
    serializer_class = system_paymentSerializer

class system_paymentListCreateView(generics.ListCreateAPIView):
    queryset = system_payment.objects.all()
    serializer_class = system_paymentSerializer

