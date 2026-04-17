# 🏥 Patient Management System (FastAPI)

Welcome to the **Patient Management API**. This project is a backend service designed for healthcare providers (Doctors) to manage patient electronic health records (EHR) through a structured, dynamic interface.

---

## 📌 Project Objectives
The goal of this project is to build a robust **RESTful API** that allows a Doctor to manage prescriptions and patient profiles using the following capabilities:
* **Data Persistence:** Securely saving patient records.
* **Data Retrieval:** Accessing full lists or specific patient profiles.
* **Data Manipulation:** Modifying or updating existing records as health statuses change.

---

## 🛣️ API Endpoints & Architecture
The API is designed around a **CRUD** (Create, Read, Update, Delete) pattern. Below are the registered routes:

| Action | Endpoint | HTTP Method | Description |
| :--- | :--- | :--- | :--- |
| **Create** | `/create` | `POST` | Register a new patient record. |
| **Read (All)** | `/view` | `GET` | Retrieve a list of all patients. |
| **Read (One)** | `/view/{patient_id}` | `GET` | Get details for a specific patient. |
| **Update** | `/update/{patient_id}` | `PUT` | Modify an existing patient's data. |
| **Delete** | `/delete/{patient_id}` | `DELETE` | Remove a record from the system. |

---

## 🧠 Core Concepts: How it Works

### 1. Static vs. Dynamic Software
* **Static Software:** Primarily used for information consumption (e.g., a simple Calendar or a Blog). The data rarely changes based on user input.
* **Dynamic Software:** High user interaction (e.g., Excel or Instagram). These systems rely on user-driven data changes, requiring a database backend.

### 2. The Client-Server Relationship
This application follows the **Client-Server Model**:
* **The Server:** Where our FastAPI application and database live.
* **The Client:** The Doctor’s browser or mobile app.
* **The Protocol:** All communication happens via **HTTP** (HyperText Transfer Protocol).

### 3. HTTP Verbs (The Language of the Web)
In a dynamic system, the server needs to know *exactly* what you want to do with the data. We use **HTTP Methods** to signal intent:

> **GET**: "Fetch this data for me." (Read)
> **POST**: "Here is new data; please save it." (Create)
> **PUT**: "Here is updated info; replace the old record." (Update)
> **DELETE**: "Remove this record permanently." (Delete)

---

## 🛠️ Tech Stack
* **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (High performance, easy to learn)
* **Language:** Python 3.x
* **Documentation:** Swagger UI (Automatically generated at `/docs`)

---

### 🚀 Getting Started
1. **Install FastAPI & Uvicorn:**
   ```bash
   pip install fastapi uvicorn
   ```
2. **Run the Server:**
   ```bash
   uvicorn main:app --reload
   ```
3. **Access the API:** Open your browser to `http://127.0.0.1:8000/docs` to test the endpoints interactively.

---

**Note:** This is a backend-only implementation. For a full production environment, this would be connected to a database like PostgreSQL or SQLite using an ORM like SQLAlchemy.

Does this structure work for your current project phase, or would you like me to add a section on **Pydantic Schemas** to show how the data is validated?