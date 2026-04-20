# Query Parameter
Query parameters are optional key-value pairs appended to the end of a URL to pass additonal data to the sercer in an HTTP request. They are typically employed for operations like filtering, sorting, searching, and pagination without altering the endpoint path itself.

/patient?city=Delhi&sort_by=age

- ? marks the start of query parameters
- each parameter is a key-value pair: key = value
- multiple parameters are seperated by &

Query() is a utility function provided by FastAPI to dedclare, validate, and document query parameters in your API endpoints.