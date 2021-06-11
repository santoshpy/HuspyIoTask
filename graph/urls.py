from django.urls import path

from graph.views import ConnectNodeAPIView, PathAPIView

urlpatterns = [
    path("connectNode", ConnectNodeAPIView.as_view(), name='connect-node'),
    path("path", PathAPIView.as_view(), name='get-path'),
]
