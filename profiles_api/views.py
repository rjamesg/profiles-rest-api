from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
