"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""


from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Competitive soccer training and inter-school matches",
        "schedule": "Mondays, Wednesdays, 4:00 PM - 6:00 PM",
        "max_participants": 22,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Skill development, scrimmages, and league play",
        "schedule": "Tuesdays, Thursdays, 4:30 PM - 6:00 PM",
        "max_participants": 15,
        "participants": ["ava@mergington.edu", "isabella@mergington.edu"]
    },
    "Drama Club": {
        "description": "Acting workshops, stage production, and school plays",
        "schedule": "Wednesdays, 3:30 PM - 5:30 PM",
        "max_participants": 25,
        "participants": ["charlotte@mergington.edu", "amelia@mergington.edu"]
    },
    "Choir": {
        "description": "Vocal training and performances for school events",
        "schedule": "Fridays, 3:00 PM - 4:30 PM",
        "max_participants": 40,
        "participants": ["evelyn@mergington.edu", "harper@mergington.edu"]
    },
    "Science Club": {
        "description": "Hands-on experiments, research projects, and science fairs",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["logan@mergington.edu", "lucas@mergington.edu"]
    },
    "Debate Team": {
        "description": "Competitive debating, public speaking, and tournament prep",
        "schedule": "Mondays, Thursdays, 5:00 PM - 6:30 PM",
        "max_participants": 20,
        "participants": ["mia@mergington.edu", "sophia.r@mergington.edu"]
    }
}

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(current_dir, "static")), name="static")

# Route definitions
@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")

@app.get("/activities")
def get_activities():
    return activities

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")
    activity = activities[activity_name]
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up for this activity")
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}

@app.post("/activities/{activity_name}/unregister")
def unregister_from_activity(activity_name: str, email: str):
    """Remove a student from an activity"""
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")
    activity = activities[activity_name]
    if email not in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student not registered for this activity")
    activity["participants"].remove(email)
    return {"message": f"Removed {email} from {activity_name}"}
"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Competitive soccer training and inter-school matches",
        "schedule": "Mondays, Wednesdays, 4:00 PM - 6:00 PM",
        "max_participants": 22,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Skill development, scrimmages, and league play",
        "schedule": "Tuesdays, Thursdays, 4:30 PM - 6:00 PM",
        "max_participants": 15,
        "participants": ["ava@mergington.edu", "isabella@mergington.edu"]
    },
    "Drama Club": {
        "description": "Acting workshops, stage production, and school plays",
        "schedule": "Wednesdays, 3:30 PM - 5:30 PM",
        "max_participants": 25,
        "participants": ["charlotte@mergington.edu", "amelia@mergington.edu"]
    },
    "Choir": {
        "description": "Vocal training and performances for school events",
        "schedule": "Fridays, 3:00 PM - 4:30 PM",
        "max_participants": 40,
        "participants": ["evelyn@mergington.edu", "harper@mergington.edu"]
    },
    "Science Club": {
        "description": "Hands-on experiments, research projects, and science fairs",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["logan@mergington.edu", "lucas@mergington.edu"]
    },
    "Debate Team": {
        "description": "Competitive debating, public speaking, and tournament prep",
        "schedule": "Mondays, Thursdays, 5:00 PM - 6:30 PM",
        "max_participants": 20,
        "participants": ["mia@mergington.edu", "sophia.r@mergington.edu"]
    }
}



# Route definitions must come after app is defined
@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")

@app.get("/activities")
def get_activities():
    return activities

# Health check endpoint for testing
@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")
    # Get the specific activity
    activity = activities[activity_name]
    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up for this activity")
    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}


# Move unregister_from_activity route here, after app is defined
@app.post("/activities/{activity_name}/unregister")
def unregister_from_activity(activity_name: str, email: str):
    """Remove a student from an activity"""
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")
    activity = activities[activity_name]
    if email not in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student not registered for this activity")
    activity["participants"].remove(email)
    return {"message": f"Removed {email} from {activity_name}"}
