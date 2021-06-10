-- Check unique_edge as undirected graph
-- i.e Edge: A <-> B is use to join Node From: A To: B  or Node From: B To: A
CREATE
	OR REPLACE FUNCTION cheeck_unique_edge (IN id1 BIGINT, IN id2 BIGINT) RETURNS BIGINT AS $body$ DECLARE
	retval BIGINT DEFAULT 0;
BEGIN
	SELECT COUNT
		( * ) INTO retval
	FROM
		( SELECT * FROM graph_edge WHERE start_node_id = id1 AND target_node_id = id2 UNION ALL SELECT * FROM graph_edge WHERE start_node_id = id2 AND target_node_id = id1 ) AS pairs;
	RETURN retval;

END $body$ LANGUAGE'plpgsql';