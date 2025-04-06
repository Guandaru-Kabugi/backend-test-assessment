from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
# Create your views here.

# POST
@permission_classes([IsAuthenticated])
class CreateNewEmployee(CreateAPIView):
    serializer_class = EmployeeSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try: #we try to see if the serializer saves successfully.
                serializer.save()
            except Exception as e: #we check the error if it fails to save.
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"Employee": serializer.data}, status=status.HTTP_201_CREATED)
    

# GET All Employees
class Get_All_Employees(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
# PUT or update an employee who exists
@permission_classes([IsAuthenticated])
class Update_Employee(UpdateAPIView):
    serializer_class = EmployeeSerializer
    def put(self, request, id):
        try:
            employee = Employee.objects.get(id=id) # we get the employee by id
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(employee, data=request.data)
        if serializer.is_valid(raise_exception=True):
            try: # we try to see if the serializer saves successfully.
                serializer.save()
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"Employee": serializer.data}, status=status.HTTP_200_OK)
# GET a single employee
@permission_classes([IsAuthenticated])
class Get_Employee(RetrieveAPIView):
    serializer_class = EmployeeSerializer
    def get(self, request, id):
        try:
            employee = Employee.objects.get(id=id) # we get the employee by id
        except Employee.DoesNotExist: # if the employee does not exist we return a 404 error.
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(employee) # we serialize the employee data
        return Response(serializer.data, status=status.HTTP_200_OK)
# DELETE an Employee
@permission_classes([IsAuthenticated])
class Delete_Employee(DestroyAPIView):
    serializer_class = EmployeeSerializer
    def delete(self, request, id):
        try:
            employee = Employee.objects.get(id=id) # we get the employee by id
        except Employee.DoesNotExist: # if the employee does not exist we return a 404 error.
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        employee.delete() # we delete the employee
        return Response({"Message":"Successfully deleted"},status=status.HTTP_204_NO_CONTENT) # we return a 204 no content response.