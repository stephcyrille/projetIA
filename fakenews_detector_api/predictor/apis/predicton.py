import os
import pickle
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PostPredictionRequest(APIView):
    def post(self, request):
        res = {
            "statusCode": '00201',
            "message": 'Requête éffectuée avec succès',
            'status': 'success'
        }
        return Response(res, status=status.HTTP_200_OK)