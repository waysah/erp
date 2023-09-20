from django.urls import path,include

from . import mathViews, views, payslipViews, balancesheetViews, employeesViews, expensesViews
from . import overtimeViews, dailyrecordViews, departmentViews, awardViews, settingsViews
from . import uploadViews
from . mathViews import calculate_salary


urlpatterns = [
    # global system urls
    path('', views.index, name='index'),
    path('needhelp/', views.needHelp, name="needHelp"),
    path('settings/', settingsViews.settings, name= "settings"),
    path('logout/', views.logout, name='logout'),
    path('search/', views.search_bar, name = "search_bar"),
    path('balanceSheet/', balancesheetViews.balance_sheet,name='balanceSheet'),
    
    # employees urls 
    path('addemployee/', employeesViews.addEmployee, name='addEmployee'),
    path('deleteAllemployees', employeesViews.deleteAllEmployees, name='deleteAllEmployees'),
    path('removeemployee/', employeesViews.employeeList , name='removeEmployee'),
    path('employees/create/', employeesViews.addEmployee, name='employee_create'),
    path('employees/<int:pk>/', employeesViews.employee_detail, name='employee_detail'),
    path('employees/<int:pk>/update/',employeesViews. employee_update, name='employee_update'),
    path('employees/<int:pk>/employee_delete/', employeesViews.employee_delete, name='employee_delete'),
    path('employeeList/', employeesViews.employeeList, name='employeeList'),
    
    #fixed amount salary url
    path('salarytemplates/',views.salaryTemplates, name='salaryTemplates'),
    
    # job types
    path('jobadd/', views.commisionTemplates, name='commisionTemplates' ),
    path('jobtypes', views.jobTypes, name='jobtypes'),
    path('jobtypes_delete/', views.jobtypes_delete, name  = 'jobtypes_delete'),
    path('jobtype_delete/', views.jobtype_delete, name='jobtype_delete'),
    path('jobtype_edit/', views.jobtype_edit, name='jobtype_edit'),
    
    # urls for salary
    path('managesalary/', views.manageSalary , name='manageSalary'),
    path('employeeSalaryList', views.employeeSalaryList, name='employeeSalaryList'),
    path('makepayment/', views.makePayment, name = 'makePayment'),
    
    # payslip
    path('generatePayslip', payslipViews.generatePayslip, name="generatePayslip"),
    path('payslip/<int:pk>/', payslipViews.generate_payslip, name='generate_payslip'),

    # advance salary
    path('advanceSalary/', views.advanceSalary, name='advanceSalary'),
    path('advancesalary_list/', views.advancesalary_list, name='advancesalary_list'),
    path('advancesalary_delete_all/', views.advancesalary_delete_all, name='advancesalary_delete_all'),
    
    #provident fund urls
    path('providentfund/', views.providentFund, name='providentFund'),
    
    # overtime urls
    path('overtime/', overtimeViews.overtime, name='overtime'),
    path('overtime_list/', overtimeViews.overtime_list, name='overtime_list'),
    path('create/', overtimeViews.overtime_create, name='overtime_create'),
    path('update/<int:pk>/', overtimeViews.overtime_update, name='overtime_update'),
    path('delete/<int:pk>/', overtimeViews.overtime_delete, name='overtime_delete'),
    
    #awards url
    path('employeeaward/', awardViews.employeeCreateAward, name='employeeAward'),
    path('award_list/', awardViews.award_list, name='award_list'),
    path('create/', awardViews.award_create, name='award_create'),
    path('update/<int:pk>/', awardViews.award_update, name='award_update'),
    path('delete/<int:pk>/', awardViews.award_delete, name='award_delete'),
    
    # department urls
    path('addDepartment/', departmentViews.addDepartment, name='addDepartment'),
    path('removedepartment/<int:pk>/', departmentViews.removeDepartment, name='removeDepartment'),
    path('manageDepartments/', departmentViews.departmentList, name='manageDepartments'),
    path('departmentlist/', departmentViews.departmentList, name='departmentList'),
    path('department_view/', departmentViews.department_view, name='department_view'),
    path('departments_delete/', departmentViews.departments_delete, name='departments_delete'),
    path('department_detail/<int:department_id>/',departmentViews.department_detail, name='department_detail'),
    
    
    # urls for system reports
    path('dailyreports/', views.dailyReports, name='dailyReports'),
    path('monthlyReports/', views.monthlyReports, name='monthlyReports'),
    path('yearlyReport/', views.yearlyReports, name='yearlyReports'),
    path('financialreport/', views.financialreport, name='financialreport'),
    path('payrollsummary/', views.payrollSummary, name='payrollSummary'),
    

    
    # urls for system configurations
    path('profile/', views.profile, name='profile'),
    path('profileDelete/', views.profileDelete, name="profileDelete"),
    path('employeee_initializer/', views.employeee_initializer, name='employeee_initializer'),
 
    
    # expenses urls
    path('addExpenses/', expensesViews.addMoreExpenses, name='addExpenses'),
    path('expense_list/', expensesViews.expense_list, name='expense_list'),
    path('create/', expensesViews.expense_create, name='expense_create'),
    path('update/<int:pk>/', expensesViews.expense_update, name='expense_update'),
    path('delete/<int:pk>/', expensesViews.expense_delete, name='expense_delete'),
    path('deleteAllExpenses/', expensesViews.deleteAllExpenses, name='deleteAllExpenses'),
    
    # commision urls/salary view
    path('commisionList/', views.commisionList, name="commisionList"),
    path('makepaymentlist/', views.makePaymentList, name="makePaymentList"),
    path('manageSalaryList/', views.manageSalaryList, name="manageSalaryList"),
    
    # daily record urls
    path('dailyRecord/create/', dailyrecordViews.dailyRecord , name = "dailyRecord"),
    path('dailyRecordList/', dailyrecordViews.dailyRecordList, name='dailyRecordList'),
    path('dailyworks/create/', dailyrecordViews.dailyRecord , name='dailywork_create'),
    path('dailyworks/<int:pk>/', dailyrecordViews.dailywork_detail, name='dailywork_detail'),
    path('dailyworks/<int:pk>/update/', dailyrecordViews.dailywork_update, name='dailywork_update'),
    path('dailyworks/<int:pk>/delete/', dailyrecordViews.dailywork_delete, name='dailywork_delete'),
    path('dailyworks_delete/', dailyrecordViews.dailyworks_delete, name='dailyworks_delete'),

    # company account urls
    path('company_account/',settingsViews.company_account, name="company_account" ),
    path('company_account_deleteAll/', settingsViews.company_account_deleteAll, name='company_account_deleteAll'),
    path('math/', mathViews.calculate_income, name='calculate_income'),
    path('calculate_income/', views.calculate_income, name='calculate_income'),
    path('personalAccount/', views.personalAccount, name = "personalAccount"),
 
    # debit urls
    path('debit_create/', views.debit_create, name='debit_create'),
    path('debit_view/', views.debit_view, name='debit_view'),
    path('debit_delete_all/', views.debit_delete_all, name='debit_delete_all'),
    path('admin_create/', settingsViews.admin_create, name='admin_create'),
    
    # system urls
    path('system_info_update/', settingsViews.system_info_update, name='system_info_update'),
    path('renew_system_payment/', settingsViews.renew_system_payment, name='renew_system_payment'),
    path('system_info_update/', settingsViews.system_info_update, name='system_info_update'),
    path('system_view/', settingsViews.system_view, name='system_view'),
    path('system_info_delete/', settingsViews.system_info_delete, name='system_info_delete'),
    path('update_info', settingsViews.update_info, name='update_info'),
]

