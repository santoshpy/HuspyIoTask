from django.db import models


class Node(models.Model):
    """
    A graph is a way of specifying relationship among a set of objects,
    called nodes connected by links called edges.

    Two types graph:

    1. an undirected graph (a <-> b <-> c <-> D)
    2. a directed graph    (a -> b -> c -> D)

    """

    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Edge(models.Model):
    """
    we say that two nodes are neighbors if the are connected by an edge.

    """

    start_node = models.ForeignKey(
        Node,
        verbose_name="From",
        related_name="as_start_edge",
        on_delete=models.CASCADE,
        null=True,
    )
    target_node = models.ForeignKey(
        Node,
        verbose_name="To",
        related_name="as_target_edge",
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        indexes = [
            models.Index(fields=["start_node", "target_node"], name="forward"),
            models.Index(fields=["target_node", "start_node"], name="reverse"),
        ]

        constraints = [
            models.UniqueConstraint(
                fields=["start_node", "target_node"], name="edge_unique"
            )
        ]

    def __str__(self):
        return f"{self.start_node} <-> {self.target_node}"
