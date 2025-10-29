from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserRegister
from .serializers import UserRegisterSerializer


class RegisterAPI(APIView):

    def post(self,request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# from rest_framework import generics
# from .models import UserRegister
# from loginapi.serializers import UserRegisterSerializer

# class RegisterAPI(generics.ListCreateAPIView):
#     queryset = UserRegister.objects.all()
#     serializer_class = UserRegisterSerializer

    def get(self, request):
        users = UserRegister.objects.all()
        serializer = UserRegisterSerializer(users, many=True)
        return Response(serializer.data)


