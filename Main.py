from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field
import json


app = FastAPI()

with open("data.json", "r") as a:
    users = json.load(a)

@app.get("/")
def get_users():
    return users

class UserCreate(BaseModel):
    name: str
    age: int
    city: str
    email: EmailStr
    review: str=Field(min_length=1,max_length=200)

@app.post("/users")
def create_user(user: UserCreate):
    if not user.review or not user.review.strip():
        raise HTTPException(status_code=400, detail="Review cannot be empty")
    
    if len(user.review) > 200:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Review cannot exceed 200 characters")

    analysis = {
        "analysis_uuid": len(users) + 1,
        "word_count": len(user.review.split()),
        "uppercase_letters": sum(1 for letter in user.review if letter.isupper()),
        "special_characters": sum(1 for c in user.review if not c.isalnum() and not c.isspace())
    }

    user_data = {
        "id": len(users) + 1,
        "name": user.name,
        "age": user.age,
        "city": user.city,
        "email": user.email,
        "review": user.review,
        "analysis": analysis
    }
    users.append(user_data)
    with open("data.json", "w") as b:
        json.dump(users, b, indent=4) 
    return user_data

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            with open("data.json", "w") as b:
                json.dump(users, b) 
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@app.get("/Analyze/{user_id}")
def analyze_users(user_id: int):
    for user in users:
        if user["id"] == user_id:
            if "analysis" not in user or "analysis_uuid" not in user["analysis"]:
                review_text = user["review"]
                user["analysis"] = {
                    "word_count": len(review_text.split()),
                    "uppercase_letters": sum(1 for letter in review_text if letter.isupper()),
                    "special_characters": sum(1 for c in review_text if not c.isalnum() and not c.isspace())
                }
                with open("data.json", "w") as b:
                    json.dump(users, b, indent=4)
            
            return {
                "user_id": user_id,
                **user["analysis"],
                "analyze_UUID": len(users) + 1
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")