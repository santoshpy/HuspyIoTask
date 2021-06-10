from django.contrib import admin

from graph.models import Edge, Node


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    pass


@admin.register(Edge)
class EdgeAdmin(admin.ModelAdmin):
    pass
