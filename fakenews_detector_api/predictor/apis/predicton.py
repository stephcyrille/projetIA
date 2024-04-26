import os
import pickle
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from predictor.models import PostRequest
from predictor.serializer.PostRequestSerializer import PostRequestSerializer


class PostPredictionRequestGet(APIView):

    def get(self, request):
        queryset = PostRequest.objects.all()
        serializer = PostRequestSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostPredictionRequestPost(APIView):
    
    def post(self, request):
        res = {
            "statusCode": '00201',
            "message": 'Requête éffectuée avec succès',
            'status': 'success'
        }
        return Response(res, status=status.HTTP_200_OK)