Here’s a **clear documentation** for your GitHub project **[cuad GitHub repository documentation (Hassandav0319/cuad)](https://github.com/Hassandav0319/cuad)** — based on the code in `Main.py` and the typical structure of similar FastAPI projects.

---

# 📘 **Project Documentation: cuad**

**Project:** CUAD (FastAPI CRUD + Review Analyzer)

**Repository:** `Hassandav0319/cuad` ([GitHub][1])

This project implements a simple **FastAPI**-based REST API that stores user reviews with basic analysis (word count, uppercase count, special character count). Data is stored in a local `data.json` file.

---

## 🧠 **Features**

✔ Get list of all users
✔ Add a new user with review text
✔ Delete a user
✔ Analyze a user’s review (count words, uppercase letters, special characters)

---

## 🚀 **Getting Started**

### 🛠 Prerequisites

Install the tools you need:

```bash
pip install fastapi uvicorn
```

(You may also need `pydantic` and `json` — but these come with FastAPI by default.)

---

## 🧱 **Project Structure**

```
cuad/
├── Main.py
├── data.json
├── .vscode/
└── __pycache__/
```

* **Main.py** — FastAPI application
* **data.json** — Stores user objects (created automatically)
* **.vscode / **pycache**** — IDE and Python artifacts

---

## 📌 **API Endpoints**

### 🔹 `GET /`

Returns all users stored in `data.json`.

**Example Response**

```json
[
  {
    "id": 1,
    "name": "Alice",
    "age": 25,
    "city": "Lahore",
    "email": "alice@example.com",
    "review": "This is great!",
    "analysis": {...}
  }
]
```

---

### 🔹 `POST /users`

Add a new user with review text.

**Body (JSON)**

| Field  | Type           | Required | Notes                         |
| ------ | -------------- | -------- | ----------------------------- |
| name   | string         | yes      | User’s name                   |
| age    | int            | yes      | User’s age                    |
| city   | string         | yes      | User’s city                   |
| email  | string (email) | yes      | Valid email                   |
| review | string         | yes      | At least 1 character, max 200 |

**Example Request**

```json
{
  "name": "Bob",
  "age": 30,
  "city": "Karachi",
  "email": "bob@domain.com",
  "review": "Nice API!"
}
```

**Success Response**

```json
{
  "id": 2,
  "name": "Bob",
  "age": 30,
  "city": "Karachi",
  "email": "bob@domain.com",
  "review": "Nice API!",
  "analysis": {
    "analysis_uuid": 2,
    "word_count": 2,
    "uppercase_letters": 1,
    "special_characters": 1
  }
}
```

**Validation Errors**

* `review` cannot be empty
* `review` must be ≤ 200 characters

---

### 🔹 `DELETE /users/{user_id}`

Delete a user by ID.

**Path parameter**

| Parameter | Type | Description          |
| --------- | ---- | -------------------- |
| user_id   | int  | ID of user to delete |

**Response**

```json
{ "message": "User deleted successfully" }
```

If not found, returns 404.

---

### 🔹 `GET /Analyze/{user_id}`

Re-computes the review analysis metrics if missing.

**Response**

```json
{
  "user_id": 1,
  "word_count": 5,
  "uppercase_letters": 2,
  "special_characters": 1,
  "analyze_UUID": 2
}
```

Returns 404 if user not found.

---

## 📊 **Internal Logic Explained**

When a user is added:

1. The API reads all existing users from `data.json`.
2. Performs validation on the review text.
3. Builds an **analysis object**:

   * `analysis_uuid`: new unique analysis identifier
   * `word_count`: number of words in review
   * `uppercase_letters`: count of uppercase letters
   * `special_characters`: count of non-alphanumeric non-space characters
     (e.g., punctuation)
4. Saves the user back to `data.json` ([GitHub][2])

---

## 🧪 **Example Workflow**

1. Run API:

```bash
uvicorn Main:app --reload
```

2. Visit:

   * `http://127.0.0.1:8000/` — list users
   * `http://127.0.0.1:8000/docs` — interactive API docs

---

## 🧩 **Validation Rules**

| Rule                     | Reason                                    |
| ------------------------ | ----------------------------------------- |
| `review` cannot be empty | Needs content for meaningful analysis     |
| `review` ≤ 200 chars     | Prevent overly long text                  |
| `email` must be valid    | Uses Pydantic’s `EmailStr` for validation |

---

## 📝 **Future Improvements (optional ideas)**

✔ Add updates (`PUT /users/{id}`)
✔ Return pagination for large lists
✔ Add timestamps → created/updated
✔ Move from JSON file to database (SQLite/PostgreSQL)
✔ Add authentication

---

If you want, I can also generate a **swagger/OpenAPI spec** or write a **markdown version** of this documentation for your GitHub README too.

[1]: https://github.com/Hassandav0319/cuad "GitHub - Hassandav0319/cuad"
[2]: https://raw.githubusercontent.com/Hassandav0319/cuad/main/Main.py "raw.githubusercontent.com"
