pip install -r requirements.txt

run : 
uvicorn app:app --reload --port 9120


route : 
http://localhost:9120/get-json