import os
import pickle
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from predictor.models import PostRequest
from predictor.serializer.PostRequestSerializer import PostRequestSerializer
import tensorflow as tf
from tensorflow.keras.models import load_model
import tensorflow_hub as hub


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
            # predictor_request = serializer.save()
            
            # Check first if we've already a saved model
            try:
                content_to_predict = serializer.data['contenu']
                # Pour recharger le modèle sauvegardé
                custom_objects = {"KerasLayer": hub.KerasLayer}
                # Charger le modèle en spécifiant les objets personnalisés
                loaded_model = tf.keras.models.load_model(MODEL_PATH, custom_objects=custom_objects)
                # TODO Inférence ICI
                # Suivre les etapes de la predicion 
                # ===============================================
                # TODO en principe la variable {content_to_predict} déclarée plus haut va a la place de X_text, peut etre en array?? Faudrait tester voir d'abord
                # y_predicted_re = model_resample.predict(X_test)
                # y_predicted_re = y_predicted_re.flatten() # Pourquoi flatten??
                # Quel est le type de valeur de y_predicted_re?? un array? si c'est le cas retourner juste 1 ou 0, bref la prediction
                res = {
                    "statusCode": "1111",
                    "prediction": ""  # Ici le retour de y_predicted, soit 1 ou 0 
                }
                return Response(res, status=status.HTTP_201_CREATED)
            except Exception as e:
                res = {
                    "statusCode": '0000',
                    "message": e.__str__(),
                }
                return Response(res, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Exposer uniquement le champ "prediction" pour les requêtes POST a partir du serializer
