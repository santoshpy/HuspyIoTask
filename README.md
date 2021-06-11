# HuspyIoTask

Please create the following REST endpoints in Django:

```json

Endpoint: /connectNode
Method: POST

payload = {
  "From": "<from_node in string format>",
  "To": "<to_node in string format>"
}
```

> This endpoint connects two nodes in a graph. We should persist these connections to a db.

```json
Endpoint: /path
Method: GET

query_params: ?from=<from_node in string format>&to=<to_node in string format>

This endpoint will get the shortest path from from_node to to_node

Response

{
 "Path": "A, B, C"
}
```

## Example

```json
Endpoint: /connectNode
Method: POST

payload = {
 "From": "A",
 "To": "B"
}
```

> Now a node called A is created and is connected to node B. So now it looks like this A <-> B

```json
Endpoint: /connectNode
Method: POST

payload = {
 "From" :"B",
 "To": "C"
}
```

> Now B is connected to node C. So now it looks like this: A <-> B <-> C

```json
Endpoint: /path
Method: GET

query_params: ?from=A&to=C

Response
{
 "Path": "A, B, C"
}
```

## Model Relationship Daigram

![Graph](images/graph_relationship.png)

## TestCase Graph

![Graph](images/graph.png)

