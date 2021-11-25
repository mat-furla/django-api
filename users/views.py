from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class UserViews(APIView):

    def get(self, req, id=None):
        if id:
            try:
                user = User.objects.get(id=id)
                serializer = UserSerializer(user)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            except:
                return Response({"status": "failed", "data": "user not found"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.all()
            serializer = UserSerializer(user, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({"status": "failed", "data": "users not found"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, req):
        serializer = UserSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
