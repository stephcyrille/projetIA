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
        serializer=PostRequestSerializer(data=request.data)
        if serializer.is_valid():
            predictor_request = serializer.save()
            print('\n\n')
            print(predictor_request)
            print('\n\n')

            predictor_request.prediction = "vrai"
            predictor_request.save()
            res = {
                "prediction": predictor_request.prediction,
            }
            return Response(res, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Exposer uniquement le champ "prediction" pour les requêtes POST a partir du serializer