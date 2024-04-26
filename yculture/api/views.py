from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Api
from .serializers import ApiSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class ApiListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
     
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Api items for given requested user
        '''
        Apis = Api.objects.filter(user = request.user.id)
        serializer = ApiSerializer(Apis, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Api with given Api data
        '''
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = ApiSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ApiDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self, api_id, user_id):
        '''
        Helper method to get the object with given api_id and user_id
        '''
        try:
            return Api.objects.get(id=api_id, user=user_id)
        except Api.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, api_id, *args, **kwargs):
        '''
        Retrieves the Api with given api_id
        '''
        api_instance = self.get_object(api_id, request.user.id)
        if not api_instance:
            return Response(
                {"res": "Object with api id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ApiSerializer(api_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, api_id, *args, **kwargs):
        '''
        Updates the api item with given api_id if exists
        '''
        api_instance = self.get_object(api_id, request.user.id)
        if not api_instance:
            return Response(
                {"res": "Object with api id does not exist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = ApiSerializer(instance=api_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, api_id, *args, **kwargs):
        '''
        Deletes the api item with given api_id if exists
        '''
        api_instance = self.get_object(api_id, request.user.id)
        if not api_instance:
            return Response(
                {"res": "Object with api id does not exist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        api_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

class UserLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
