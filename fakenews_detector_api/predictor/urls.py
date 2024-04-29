from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from predictor.apis.predicton import PostPredictionRequestGet, PostPredictionRequestPost

urlpatterns = [
  path('all_requests/', PostPredictionRequestGet.as_view()),
  path('post/', PostPredictionRequestPost.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)