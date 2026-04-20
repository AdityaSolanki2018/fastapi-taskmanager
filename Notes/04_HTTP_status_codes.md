HTTP status codes are 3 digit numbers returned by a web server(like FastAPI) to indicate the result of a client's request(like from a browser or API consumer)

They help the client (browser, frontend, mobile app, etc) understand:
1. whether the request was successfull.
2. Whether somethind went wrong.
3. and what kind of issue occured (if any).

2xx - Success - The request was successfully recieved and processed

3xx - Redurection - Further action needs to be taken(eg. redirect)

4xx - Client Error - Something is weond with the request from the client.

5xx - Server Error - Something went wrong on the server side.

200 OK -  Srandard Success
201 Created - Resource created
204 No Content - Success but no data returned (After Create request)

400 Bad Request - Misformed or invalid request (Missind field or wrong data type)

## HTTP Exception
A special built in exception in FasrAPI used to return custom HTTP error responses wehn something goes weong in your API.

Insread of retuting a normal JSON or crashing the server, you can gracefully raise an error with: 
A proper HTTP status code (like 404. 400,403 etc)
a custom error message
extra headers(optional)