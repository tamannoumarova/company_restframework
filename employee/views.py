from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from employee.models import Employee
from employee.serializer import EmployeeSerializer,EmployeeListSerializer
from rest_framework import status
from rest_framework.exceptions import NotFound

@api_view(["GET","POST"])
def get_employee_list(request):
    if request.method=="Get":
        queryset = Employee.objects.all()
        serializer = EmployeeListSerializer(queryset,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    else:
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)


class EmployeeListView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        queryset = Employee.objects.all()
        serializer = EmployeeListSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)


class EmployeeDetailView(APIView):
    def get_object(self,pk):
        try:
            instance = Employee.objects.get(pk=pk)
            return instance
        except Employee.DoesNotExist as e:
            raise NotFound(e)

    def get(self,request,*args,**kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        serializer = EmployeeSerializer(instance)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self,request,*args,**kwargs):
        instance = self.get_object(pk=kwargs.get("pk")),
        serializer = EmployeeSerializer(instance,request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)

    def delete(self,request,*args,**kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


