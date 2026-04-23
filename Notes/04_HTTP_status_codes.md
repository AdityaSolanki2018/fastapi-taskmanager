#  HTTP Status Codes & Error Handling

## 1. Introduction to HTTP Status Codes
HTTP status codes are **3-digit numbers** returned by a web server (like FastAPI) to communicate the result of a client's request. They allow the frontend, mobile app, or API consumer to understand the outcome without parsing the entire response body.

### Status Code Categories
| Category | Meaning | Description |
| :--- | :--- | :--- |
| **2xx** | **Success** | The request was successfully received, understood, and processed. |
| **3xx** | **Redirection** | Further action needs to be taken (e.g., the resource moved to a new URL). |
| **4xx** | **Client Error** | The request contains bad syntax or cannot be fulfilled (the client's fault). |
| **5xx** | **Server Error** | The server failed to fulfill an apparently valid request (the server's fault). |

---

## 2. Common Status Codes in FastAPI
* **200 OK:** The standard success response.
* **201 Created:** Confirms a new resource (like a patient record) was successfully created.
* **204 No Content:** The request succeeded, but there is no data to send back (often used after a successful `DELETE`).
* **400 Bad Request:** The server cannot process the request due to client error (e.g., malformed syntax or missing fields).
* **404 Not Found:** The specific resource requested (e.g., `patient_id=99`) does not exist.

---

## 3. FastAPI `HTTPException`
The `HTTPException` is a built-in tool used to return custom error responses gracefully. Instead of the server crashing or returning a generic error, you can provide the client with specific context.

### Why use it?
1.  **Custom Messages:** Explain exactly why the request failed.
2.  **Proper Status Codes:** Ensure the client receives the correct 4xx or 5xx code.
3.  **Clean Exit:** It stops the execution of the current path operation and sends the error immediately.

### Practical Example: Patient Lookup
Here is how you combine **Path Parameters**, **Validation**, and **HTTP Exceptions**:

```python
from fastapi import FastAPI, Path, HTTPException, status

app = FastAPI()

# Mock Database
patients = {1: {"name": "John Doe"}, 2: {"name": "Jane Smith"}}

@app.get("/view/{patient_id}")
async def get_patient(
    patient_id: int = Path(..., gt=0, title="The ID of the patient")
):
    if patient_id not in patients:
        # Raising a 404 error if the patient isn't found
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Patient with ID {patient_id} not found."
        )
    
    return patients[patient_id]
```

---

## 4. Key Takeaways for API Design
* **Be Specific:** Don't just return a `400` for everything; use `404` for missing items and `403` for permission issues.
* **Use `status` module:** Instead of typing `404` manually, use `status.HTTP_404_NOT_FOUND`. It prevents typos and makes code more readable.
* **Validation First:** Let FastAPI's `Path()` and `Query()` handle data types and ranges before your logic even hits the `HTTPException` check.
