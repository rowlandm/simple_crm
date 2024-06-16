from fastapi import FastAPI

app = FastAPI()

@app.get("/")  
async def hello_world():  
    return {"success": True, "message": "Hello World"}

@app.get('/users')
async def get_users():
    return {"success": True, "users": ["John", "Jane", "Sling Academy"]}
