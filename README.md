# EpicBooks backend

## Run with Docker
Don't forget to create `.env` file before. Use `.env.example` as an example.

Build the app:
```
make docker-build
```
Run the app:
```
make docker-run
```

## Python launch
Create virtual environment:
```
python3 -m venv venv
```
Activate virtual environment:
```
source venv/bin/activate
```
Install dependencies with `pip`:
```
pip install -r requirements.txt
```
Run database migrations with `alembic`:
```
alembic upgrade head
```
Run the app with `uvicorn`:
```
make run-uvicorn
```
Run the app with `gunicorn`:
```
make run-gunicorn
```
