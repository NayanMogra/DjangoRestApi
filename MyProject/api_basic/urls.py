from django.urls import path
from .views import *
urlpatterns = [
    # path('article/', artical_list),
    path('article/', ArticleAPIView.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
    path('detail/<int:id>', ArticleDetails.as_view()),
]
