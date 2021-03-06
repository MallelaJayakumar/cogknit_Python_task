from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from emp.employees.models import Employee
from emp.employees.serializers import EmployeeSerializer


@csrf_exempt
def employee_list(request):
    """
    List all code Employees, or create a new snippet.
    """
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def employee_detail(request, pk):
    """
    Retrieve, update or delete a code employee.
    """
    try:
        employee = Employee.objects.get(pk=pk)
    except employee.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Employee(employee)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(employee, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        employee.delete()
        return HttpResponse(status=204)