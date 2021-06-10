from django.db import connection
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from graph.models import Node
from graph.serializers import ConnectNodeSerializer
from graph.utils import read_sql


class ConnectNodeAPIView(CreateAPIView):
    serializer_class = ConnectNodeSerializer


class PathAPIView(APIView):

    def get_queryset(self, request, *args, **kwargs):
        query_params = self.request.query_params
        from_ = query_params.get("from")
        to = query_params.get("to")
        start_node = Node.objects.get(name=from_)
        target_node = Node.objects.get(name=to)
        q = read_sql('search.sql')
        with connection.cursor() as cursor:
            cursor.execute(
                q.format(start_node_id=start_node.id, target_node_id=target_node.id)
            )
            row = cursor.fetchone()
            return row

    def get(self, request, *args, **kwargs):
        path_ids, *_ = self.get_queryset(request, *args, **kwargs)
        path_ids = list(map(int, path_ids.strip().strip(",").split(",")))
        path_nodes = Node.objects.filter(id__in=path_ids)
        sorted_values = sorted(
            path_nodes.values("id", "name"),
            key=lambda obj: path_ids.index(obj.get("id")),
        )
        return Response({"Path": ", ".join([obj.get("name") for obj in sorted_values])})
