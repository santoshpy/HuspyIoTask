-- Create all_path view for undirected graph search

CREATE OR REPLACE VIEW all_path (start_node_id, target_node_id) AS
    SELECT start_node_id, target_node_id
    FROM graph_edge
    UNION
    SELECT target_node_id, start_node_id
    FROM graph_edge;