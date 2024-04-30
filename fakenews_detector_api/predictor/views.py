from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Fonction de détection de fausses nouvelles (exemple trivial)
def detect_fake_news(title, author, text):
    # Ici, vous pourriez implémenter votre propre logique de détection de fausses nouvelles
    # Pour l'exemple, je vais simplement retourner "Oui" si le texte n'est pas vide
    if text:
        return "Oui"
    else:
        return "Non"

@csrf_exempt
def detect_fake_news_api(request):
    if request.method == 'POST':
        # Récupérer les données JSON de la requête POST
        data = json.loads(request.body)
        title = data.get('title', '')
        author = data.get('author', '')
        text = data.get('text', '')

        # Appeler la fonction de détection de fausses nouvelles
        result = detect_fake_news(title, author, text)

        # Renvoyer la réponse JSON
        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Seules les requêtes POST sont autorisées'})

