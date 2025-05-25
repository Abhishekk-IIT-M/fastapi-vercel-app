from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks from q-cercel-python.json
file_path = os.path.join(os.path.dirname(__file__), 'q-cercel-python.json')
with open(file_path, 'r') as f:
    student_data = json.load(f)

@app.get("/api")
def get_marks(name: list[str] = []):
    return {"marks": [student_data.get(n, None) for n in name]}
