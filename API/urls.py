from django.urls import path
from . import views
from . views import ManagerListCreateView, ManagerRetrieveUpdateDestroyView, EmployeeListCreateView, EmployeeRetrieveUpdateDestroyView
from . views import employee_initializerListCreateView, employee_initializerRetrieveUpdateDestroyView
from . views import commision_salaryListCreateView, commision_salaryRetrieveUpdateDestroyView, Fixed_saralyListCreateView, Fixed_saralyRetrieveUpdateDestroyView
from . views import allowancesListCreateView, allowancesRetrieveUpdateDestroyView, deductionListCreateView, deductionRetrieveUpdateDestroyView
from . views import salary_detailsListCreateView, salary_detailsRetrieveUpdateDestroyView, job_typeListCreateView, job_typeRetrieveUpdateDestroyView
from . views import SelectDepartmentListCreateView, SelectDepartmentRetrieveUpdateDestroyView, PayrollSummaryListCreateView, PayrollSummaryRetrieveUpdateDestroyView
from . views import AdvanceSalaryListCreateView, AdvanceSalaryRetrieveUpdateDestroyView, overtimeListCreateView, overtimeRetrieveUpdateDestroyView
from . views import employeeAwardListCreateView, employeeAwardRetrieveUpdateDestroyView, addExpensesListCreateView, addExpensesRetrieveUpdateDestroyView
from . views import DepartmentListCreateView, DepartmentRetrieveUpdateDestroyView, first_departmentListCreateView, first_departmentRetrieveUpdateDestroyView
from . views import DailyWorkListCreateView, DailyWorkRetrieveUpdateDestroyView, EmployeeListCreateView, EmployeeRetrieveUpdateDestroyView
from . views import TransactionListCreateView, TransactionRetrieveUpdateDestroyView, commision_rateListCreateView, commision_rateRetrieveUpdateDestroyView
from . views import commission_templatesListCreateView, commission_templatesRetrieveUpdateDestroyView, nextofkinListCreateView, nextofkinRetrieveUpdateDestroyView
from . views import first_employeesListCreateView, first_employeesRetrieveUpdateDestroyView, payslipListCreateView, payslipRetrieveUpdateDestroyView
from . views import financialreportListCreateView, financialreportRetrieveUpdateDestroyView, daily_resultsListCreateView, daily_resultsRetrieveUpdateDestroyView
from . views import department_employee_viewListCreateView, department_employee_viewRetrieveUpdateDestroyView, debitListCreateView, debitRetrieveUpdateDestroyView
from . views import system_updateListCreateView, system_updateRetrieveUpdateDestroyView, payement_gatewayListCreateView, payement_gatewayRetrieveUpdateDestroyView
from . views import system_paymentListCreateView, system_paymentRetrieveUpdateDestroyView

urlpatterns = [
    path('', views.api_index, name='api_index'),

    # urls for managers
    path('managers/', ManagerListCreateView.as_view(), name='managers'),
    path('manager/<int:pk>/', ManagerRetrieveUpdateDestroyView.as_view(), name='manager'),

    # Urls for employee
    path('employees/', EmployeeListCreateView.as_view(), name='employees'),
    path('employee/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee'),

    # Urls for employee initializer
    path('employee_initializers/', employee_initializerListCreateView.as_view(), name='employee_intializer'),
    path('employee_initializer/<int:pk>/', employee_initializerRetrieveUpdateDestroyView.as_view(), name='employee_intializer'),

    # Urls for commision salary
    path('commision_salaries/', commision_salaryListCreateView.as_view(), name='commision_salaries'),
    path('commision_salary/<int:pk>/', commision_salaryRetrieveUpdateDestroyView.as_view(), name='commision_salary'),

    # Urls for fixed salary
    path('fixed_salaries/', Fixed_saralyListCreateView.as_view(), name='fixed_salaries'),
    path('fixed_salary/<int:pk>/', Fixed_saralyRetrieveUpdateDestroyView.as_view(), name='fixed_salary'),

    path('allowances/', allowancesListCreateView.as_view(), name='allowances'),
     path('allowance/<int:pk>/', allowancesRetrieveUpdateDestroyView.as_view(), name='allowance'),

    # Urls for deductions
    path('deductions/', deductionListCreateView.as_view(), name='deductions'),
    path('deduction/<int:pk>/', deductionRetrieveUpdateDestroyView.as_view(), name='deduction'),

    # Urls for salary details
    path('salary_details/', salary_detailsListCreateView.as_view(), name='salary_details'),
    path('salary_detail/<int:pk>/', salary_detailsRetrieveUpdateDestroyView.as_view(), name='salary_detail'),

    # Urls for job types
    path('job_types/', job_typeListCreateView.as_view(), name='job_types'),
    path('job_type/<int:pk>/', job_typeRetrieveUpdateDestroyView.as_view(), name='job_type'),

    # Urls for SelectDepartment
    path('select_departments/', SelectDepartmentListCreateView.as_view(), name='select_departments'),
    path('select_department/<int:pk>/', SelectDepartmentRetrieveUpdateDestroyView.as_view(), name='select_department'),

    # Urls for PayrollSummary
    path('payroll_summaries/', PayrollSummaryListCreateView.as_view(), name='payroll_summaries'),
    path('payroll_summary/<int:pk>/', PayrollSummaryRetrieveUpdateDestroyView.as_view(), name='payroll_summary'),

    # Urls for AdvanceSalary
    path('advance_salaries/', AdvanceSalaryListCreateView.as_view(), name='advance_salaries'),
    path('advance_salary/<int:pk>/', AdvanceSalaryRetrieveUpdateDestroyView.as_view(), name='advance_salary'),

    # Urls for overtime
    path('overtimes/', overtimeListCreateView.as_view(), name='overtimes'),
    path('overtime/<int:pk>/', overtimeRetrieveUpdateDestroyView.as_view(), name='overtime'),

    # Urls for employee awards
    path('employee_awards/', employeeAwardListCreateView.as_view(), name='employee_awards'),
    path('employee_award/<int:pk>/', employeeAwardRetrieveUpdateDestroyView.as_view(), name='employee_award'),

    # Urls for add expenses
    path('add_expenses/', addExpensesListCreateView.as_view(), name='add_expenses'),
    path('add_expense/<int:pk>/', addExpensesRetrieveUpdateDestroyView.as_view(), name='add_expense'),

    # Urls for departments
    path('departments/', DepartmentListCreateView.as_view(), name='departments'),
    path('department/<int:pk>/', DepartmentRetrieveUpdateDestroyView.as_view(), name='department'),

    # Urls for first departments
    path('first_departments/', first_departmentListCreateView.as_view(), name='first_departments'),
    path('first_department/<int:pk>/', first_departmentRetrieveUpdateDestroyView.as_view(), name='first_department'),

    # Urls for daily work
    path('daily_works/', DailyWorkListCreateView.as_view(), name='daily_works'),
    path('daily_work/<int:pk>/', DailyWorkRetrieveUpdateDestroyView.as_view(), name='daily_work'),

    # Urls for employees
    path('employees/', EmployeeListCreateView.as_view(), name='employees'),
    path('employee/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee'),

    # Urls for transactions
    path('transactions/', TransactionListCreateView.as_view(), name='transactions'),
    path('transaction/<int:pk>/', TransactionRetrieveUpdateDestroyView.as_view(), name='transaction'),

    # Urls for commission rates
    path('commission_rates/', commision_rateListCreateView.as_view(), name='commission_rates'),
    path('commission_rate/<int:pk>/', commision_rateRetrieveUpdateDestroyView.as_view(), name='commission_rate'),

    # Urls for commission templates
    path('commission_templates/', commission_templatesListCreateView.as_view(), name='commission_templates'),
    path('commission_template/<int:pk>/', commission_templatesRetrieveUpdateDestroyView.as_view(), name='commission_template'),

    # Urls for next of kin
    path('nextofkins/', nextofkinListCreateView.as_view(), name='nextofkins'),
    path('nextofkin/<int:pk>/', nextofkinRetrieveUpdateDestroyView.as_view(), name='nextofkin'),

    # Urls for first employees
    path('first_employees/', first_employeesListCreateView.as_view(), name='first_employees'),
    path('first_employee/<int:pk>/', first_employeesRetrieveUpdateDestroyView.as_view(), name='first_employee'),

    # Urls for payslips
    path('payslips/', payslipListCreateView.as_view(), name='payslips'),
    path('payslip/<int:pk>/', payslipRetrieveUpdateDestroyView.as_view(), name='payslip'),

    # Urls for financial reports
    path('financialreports/', financialreportListCreateView.as_view(), name='financialreports'),
    path('financialreport/<int:pk>/', financialreportRetrieveUpdateDestroyView.as_view(), name='financialreport'),

        # Urls for daily results
    path('daily_results/', daily_resultsListCreateView.as_view(), name='daily_results'),
    path('daily_result/<int:pk>/', daily_resultsRetrieveUpdateDestroyView.as_view(), name='daily_result'),

    # Urls for department employee view
    path('department_employee_views/', department_employee_viewListCreateView.as_view(), name='department_employee_views'),
    path('department_employee_view/<int:pk>/', department_employee_viewRetrieveUpdateDestroyView.as_view(), name='department_employee_view'),

    # Urls for debits
    path('debits/', debitListCreateView.as_view(), name='debits'),
    path('debit/<int:pk>/', debitRetrieveUpdateDestroyView.as_view(), name='debit'),

    # Urls for system updates
    path('system_updates/', system_updateListCreateView.as_view(), name='system_updates'),
    path('system_update/<int:pk>/', system_updateRetrieveUpdateDestroyView.as_view(), name='system_update'),

    # Urls for payment gateways
    path('payment_gateways/', payement_gatewayListCreateView.as_view(), name='payment_gateways'),
    path('payment_gateway/<int:pk>/', payement_gatewayRetrieveUpdateDestroyView.as_view(), name='payment_gateway'),

    # Urls for system payments
    path('system_payments/', system_paymentListCreateView.as_view(), name='system_payments'),
    path('system_payment/<int:pk>/', system_paymentRetrieveUpdateDestroyView.as_view(), name='system_payment'),
]


