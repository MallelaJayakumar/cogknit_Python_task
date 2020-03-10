from rest_framework import serializers
from emp.employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'firstName', 'lastName', 'email', 'phone', 'title', 'department', 'birthdate')