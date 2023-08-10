from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from profession.models import Profession
from profession.serializer import ProfessionSerializer,ProfessionListSerializer
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

@api_view(["GET","POST"])
def get_profession_list(request):
    if request.method=="Get":
        queryset = Profession.objects.all()
        serializer = ProfessionListSerializer(queryset,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    else:
        serializer = ProfessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)


class ProfessionListView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        queryset = Profession.objects.all()
        serializer = ProfessionListSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        serializer = ProfessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)


class ProfessionDetailView(APIView):
    def get_object(self,pk):
        try:
            instance = Profession.objects.get(pk=pk)
            return instance
        except Profession.DoesNotExist as e:
            raise NotFound(e)

    def get(self,request,*args,**kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        serializer = ProfessionSerializer(instance)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self,request,*args,**kwargs):
        instance = self.get_object(pk=kwargs.get("pk")),
        serializer = ProfessionSerializer(instance,request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)

    def delete(self,request,*args,**kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


