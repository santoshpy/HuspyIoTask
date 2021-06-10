WITH RECURSIVE search_path ( start_node_id, target_node_id, distance, path_str ) AS (
    SELECT
        start_node_id,
        target_node_id,
        1 AS distance,
        start_node_id || ', ' || target_node_id || ', ' AS path_str
    FROM
        all_path
    WHERE
        start_node_id = {start_node_id}

    UNION

    SELECT
        sp.start_node_id,
        ap.target_node_id,
        sp.distance + 1,
        sp.path_str || ap.target_node_id || ', ' AS path_str
    FROM
        all_path AS ap
        JOIN search_path AS sp ON ap.start_node_id = sp.target_node_id
    WHERE
        sp.path_str NOT LIKE'%' || ap.target_node_id || ', %'
    ) SELECT
    path_str
FROM
    search_path
WHERE
    target_node_id = {target_node_id}
ORDER BY
    start_node_id,
    target_node_id,
    distance
    LIMIT 1;