from django.urls import path

from graph.views import ConnectNodeAPIView, PathAPIView

urlpatterns = [
    path("connectNode", ConnectNodeAPIView.as_view()),
    path("path", PathAPIView.as_view()),
]
