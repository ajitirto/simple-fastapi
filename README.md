# simple fastapi using python


# requirement:

python3 -m venv venv

pip install fastapi
pip install "uvicorn[standard]"


curl 127.0.0.1:8000

# interactive API docs (provided by Swagger UI)

go to http://127.0.0.1:8000/docs

# alternatife

go to http://127.0.0.1:8000/redoc.


note: FastAPI generates a "schema" with all your API using the OpenAPI standard for defining APIs.


uvicorn main:app --reload