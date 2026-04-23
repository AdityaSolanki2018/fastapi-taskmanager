# FastAPI Path Parameters & Validation

## 1. Understanding Path Parameters
Path parameters are **dynamic segments** of a URL used to identify a specific resource. They act as variables within the endpoint's path.

* **Primary Use Case:** When you need to target a unique resource (e.g., a specific user, order, or patient).
* **Common Actions (CRUD):** * **Retrieve:** `GET /patients/{id}`
    * **Update:** `PUT /patients/{id}`
    * **Delete:** `DELETE /patients/{id}`

### Example Scenario
To view data for a specific patient by their ID, the endpoint structure would look like this:
* `localhost:8000/view/3` → Fetches Patient #3
* `localhost:8000/view/4` → Fetches Patient #4

---

## 2. Implementing with the `Path()` Function
FastAPI provides the `Path` class to add **metadata** and **validations** to your parameters. This ensures that the API only processes valid data (e.g., no negative IDs).

### Basic Syntax
```python
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/view/{patient_id}")
async def get_patient(
    patient_id: int = Path(..., title="The ID of the patient to get", gt=0)
):
    return {"patient_id": patient_id}
```

---

## 3. Advanced Validation & Metadata
The `Path()` function accepts several arguments to refine how the parameter is handled:

### Metadata (For Documentation)
* **`title`**: A short name for the parameter in the generated OpenAPI/Swagger docs.
* **`description`**: A detailed explanation of what the parameter does.
* **`example`**: Provides a sample value for users in the UI.

### Numeric Validations
Use these to restrict integer or float inputs:
| Parameter | Description | Example |
| :--- | :--- | :--- |
| `gt` | Greater Than | `gt=0` (must be 1 or higher) |
| `ge` | Greater than or Equal to | `ge=1` |
| `lt` | Less Than | `lt=100` |
| `le` | Less than or Equal to | `le=100` |

### String Validations
If your path parameter is a string (e.g., a username or code):
* **`min_length` / `max_length`**: Constraints on the string size.
* **`regex`**: A Regular Expression pattern the string must match (e.g., `^[a-z]+$` for lowercase only).

---

## 4. Why use Path()?
1.  **Data Integrity:** Your code won't even execute if the input doesn't meet the requirements (FastAPI returns a `422 Unprocessable Entity` error automatically).
2.  **Auto-Documentation:** All constraints (like "must be greater than 0") are automatically added to your `/docs` page.
3.  **Security:** Prevents unexpected input types from reaching your logic or database queries.

---

> **Pro Tip:** In FastAPI, the `...` (Ellipsis) used as the first argument in `Path(..., ...)` marks the parameter as **required**.
