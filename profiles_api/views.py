from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):
    """
    Test API View.

    Define a URL (Endpoint)
    Addign it to this view, then Django handles it
    by calling the relevant function.
    """

    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """
        Returns a list of APIView features.
        """
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'gives you the most control over your appliation logic',
            'is mapped manually to URLS',
        ]

        return Response({'message': 'hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """
        Create a hello message with our name
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello {}'.format(name)

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """
        Handle Updating an object

        usually you'd do a PUT to a specific ID.
        """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """
        Handle a partial update of an object

        usually you'd do a PUT to a specific ID.
        """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """
        Delete an object

        usually you'd do a PUT to a specific ID.
        """
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """
    Test API ViewSet
    """
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """
        Return a hello message in list format.
        """
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code!',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """
        Create a new Hello message.
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """
        handle getting an object by it's ID.
        """
        return Response({'http_method': 'GET'})


    def update(self, request, pk=None):
        """
        handle updating an object by it's ID.
        """
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """
        handle partially updating an object by it's ID.
        """
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """
        Remove an object by it's ID.
        """
        return Response({'http_method': 'DELETE'})
