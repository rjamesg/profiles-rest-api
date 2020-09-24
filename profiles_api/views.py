from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """
    Test API View.

    Define a URL (Endpoint)
    Addign it to this view, then Django handles it
    by calling the relevant function.
    """

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
