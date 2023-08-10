from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from branch.models import Branch
from branch.serializer import BranchSerializer,BranchListSerializer
from rest_framework import status
from rest_framework.exceptions import NotFound



@api_view(["GET","POST"])
def get_branch_list(request):
    if request.method=="Get":
        queryset = Branch.objects.all()
        serializer = BranchListSerializer(queryset,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    else:
        serializer = BranchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)


class BranchListView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        queryset = Branch.objects.all()
        serializer = BranchListSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        serializer = BranchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)


class BranchDetailView(APIView):
    def get_object(self,pk):
        try:
            instance = Branch.objects.get(pk=pk)
            return instance
        except Branch.DoesNotExist as e:
            raise NotFound(e)

    def get(self,request,*args,**kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        serializer = BranchSerializer(instance)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self,request,*args,**kwargs):
        instance = self.get_object(pk=kwargs.get("pk")),
        serializer = BranchSerializer(instance,request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)

    def delete(self,request,*args,**kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


