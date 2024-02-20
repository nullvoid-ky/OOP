from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

# Serve static files from the "static" directory
app.mount("/static", StaticFiles(directory="static"), name="static")

todo_list = [
    {"id": 1, "activity": "Buy groceries"},
    {"id": 2, "activity": "Clean the house"},
    {"id": 3, "activity": "Finish homework"}
]

# Endpoint to return the todo list
@app.get("/todo")
def get_todo_list():
    return todo_list

# Post -- > Create Todo
@app.post("/todo", tags=["Todos"])
async def add_todo(todo: dict) -> dict: 
    todo_list.append(todo)
    return todo_list

# Endpoint to edit an existing Activity in the todo list
@app.put("/todo/{id}")
def edit_activity(id: int, activity: dict):
    for item in todo_list:
        if item["id"] == id:
            item["activity"] = activity["activity"]
            return {"message": "Activity updated successfully"}
    raise HTTPException(status_code=404, detail="Activity not found")

# Endpoint to delete a activity from the todo list
@app.delete("/todo/{id}")
def delete_activity(id: int):
    for index, item in enumerate(todo_list):
        if item["id"] == id:
            del todo_list[index]
            return {"message": "Activity deleted successfully"}
    raise HTTPException(status_code=404, detail="Activity not found")