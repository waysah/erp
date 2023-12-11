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
    
]