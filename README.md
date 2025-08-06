
---

# 🚀 FastAPI Hello World Project

Welcome to the **FastAPI Hello World** project — a lightweight and blazing-fast web API built using the powerful **FastAPI** framework. This API serves as a minimal yet expressive introduction to FastAPI, showcasing how simple it is to build and expose endpoints.

---

## 📁 Project Structure



├── app.py             # Main application file

├── README.md          # You're reading it :)

└── requirements.txt   # Required Python packages



---

## 🌐 Endpoints

### `GET /`
Returns a cheerful greeting.

**Response**
```json
{
  "message": "Hello, World!"
}
````

---

### `GET /owner`

Meet the creator.

**Response**

```json
{
  "message": "This API Belong to Master Aryan.....😀"
}
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fastapi-hello-world.git
cd fastapi-hello-world
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI server

```bash
uvicorn app:app --reload
```

---

## 📖 Interactive API Docs

Once running, open your browser:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🛠️ Tech Stack

* 🌟 [FastAPI](https://fastapi.tiangolo.com/) – Modern, fast (high-performance) web framework for APIs
* ⚡ [Uvicorn](https://www.uvicorn.org/) – Lightning-fast ASGI server implementation

---

## 👑 Author

Built with 💻 and 😄 by **Master Aryan**

---

## 📄 License

This project is open source and free to use for learning and experimentation.

````

---

✅ `requirements.txt` (for completeness):
annotated-types==0.7.0
anyio==4.10.0
click==8.1.8
colorama==0.4.6
exceptiongroup==1.3.0
fastapi==0.116.1
h11==0.16.0
idna==3.10
pydantic==2.11.7
pydantic_core==2.33.2
sniffio==1.3.1
starlette==0.47.2
typing-inspection==0.4.1
typing_extensions==4.14.1
uvicorn==0.35.0
