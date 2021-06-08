# HuspyIoTask

Please create the following REST endpoints in Django:

POST /connectNode

{

“From”: <from_node in string format>

“To”: <to_node in string format>

}

This endpoint connects two nodes in a graph. We should persist these connections to a db.

GET /path?from=<from_node in string format>&to=<to_node in string format>

This endpoint will get the shortest path from from_node to to_node

    {

“Path”: “A, B, C”

    }

Example:

POST /connectNode

{

“From”: “A”,

“To”: “B”

}

Now a node called A is created and is connected to node B. So now it looks like this A <-> B

POST /connectNode

{

“From” :”B”,

“To”: “C”

}

Now B is connected to node C. So now it looks like this: A <-> B <-> C

GET /path?from=A&to=C

{

“Path”: “A, B, C”

}

Please include unit tests.

Please send the github repository once the task is finalized.