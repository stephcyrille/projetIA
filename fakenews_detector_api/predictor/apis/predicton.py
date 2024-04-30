import os
import pickle
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from predictor.models import PostRequest
from predictor.serializer.PostRequestSerializer import PostRequestSerializer
from keras.models import load_model


settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
MODEL_PATH = os.path.join(PROJECT_ROOT, 'models/model_final.h5')

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
            
            # Check first if we've already a saved model
            if os.path.exists(MODEL_PATH):
                # Open the file and read its contents
                with open(MODEL_PATH, "rb") as f:
                    loaded_model = load_model(f)
                    loaded_model.summary()
                predictor_request.prediction = "vrai"
                predictor_request.save()
                res = {
                    "prediction": predictor_request.prediction,
                }
                return Response(res, status=status.HTTP_201_CREATED)
            else:
                res = {
                    "statusCode": '0000',
                    "message": "We doesn't find the model",
                }
                return Response(res, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Exposer uniquement le champ "prediction" pour les requêtes POST a partir du serializer
