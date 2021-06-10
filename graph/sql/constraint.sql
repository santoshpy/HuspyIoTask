-- Check unique pair constraint for edges

ALTER TABLE graph_edge ADD CONSTRAINT unique_pair CHECK (cheeck_unique_edge (graph_edge.start_node_id, graph_edge.target_node_id) < 1);

-- Prevent to add same node as source and destination

ALTER TABLE graph_edge ADD CONSTRAINT no_self_loop CHECK (graph_edge.start_node_id <> graph_edge.target_node_id);