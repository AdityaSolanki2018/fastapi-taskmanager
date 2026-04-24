# API Development: Query Parameters

## 1. Overview

**Query parameters** are optional key-value pairs appended to the end of a URL. They allow clients to pass additional data to the server during an HTTP request (typically `GET` requests) without changing the core endpoint path.

---

## 2. Syntax and Structure

A URL with query parameters follows a specific structure:

`https://api.example.com/patient?city=Delhi&sort_by=age`

- **The Separator (`?`):** The question mark signifies the end of the URL path and the beginning of the query string.
- **Key-Value Pairs:** Data is represented as `key=value`.
- **Multiple Parameters (`&`):** Individual parameters are separated by the ampersand symbol.

| Component | Description                  | Example    |
| :-------- | :--------------------------- | :--------- |
| **Path**  | The resource location        | `/patient` |
| **Key**   | The name of the parameter    | `city`     |
| **Value** | The data assigned to the key | `Delhi`    |

---

## 3. Common Use Cases

Query parameters are best used for non-hierarchical data processing, such as:

- **Filtering:** Narrowing down results (e.g., `?category=electronics`).
- **Sorting:** Ordering the data (e.g., `?sort=desc`).
- **Searching:** Providing keywords (e.g., `?q=fastapi_tutorial`).
- **Pagination:** Navigating through large datasets (e.g., `?limit=10&offset=20`).

---

## 4. Implementation in FastAPI

In **FastAPI**, query parameters are automatically detected when you define function parameters that are not part of the path.

### The `Query()` Utility

FastAPI provides the `Query()` class to add metadata, validation, and documentation to your parameters.

```python
from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        None,
        min_length=3,
        max_length=50,
        title="Search Query",
        description="Search for items by name"
    )
):
    return {"query": q}
```
