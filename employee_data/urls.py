from django.urls import path
from .views import CreateNewEmployee, Get_All_Employees, Get_Employee, Delete_Employee,Update_Employee


urlpatterns = [
    path('employees/create/', CreateNewEmployee.as_view(), name='create-employee'),
    path('employees/all/', Get_All_Employees.as_view(), name='get-all-employees'),
    path('employees/<int:id>/', Get_Employee.as_view(), name='get-employee'), # GET a single employee by ID
    path('employees/delete/<int:id>/', Delete_Employee.as_view(), name='delete-employee'), # DELETE an employee by ID
    path('employees/update/<int:id>/', Update_Employee.as_view(), name='update-employee'), # PUT or update an employee by ID
]