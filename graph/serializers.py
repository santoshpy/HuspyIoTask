from rest_framework import serializers

from graph.models import Edge, Node


class ConnectNodeSerializer(serializers.Serializer):
    From = serializers.CharField(source='start_node', max_length=200)
    To = serializers.CharField(source='target_node', max_length=200)

    def create(self, validated_data):
        start_node = validated_data.pop("start_node")
        target_node = validated_data.pop("target_node")

        start_node_obj, _ = Node.objects.get_or_create(name=start_node)
        target_node_obj, _ = Node.objects.get_or_create(name=target_node)

        edge, _ = Edge.objects.get_or_create(
            start_node=start_node_obj, target_node=target_node_obj
        )
        return edge