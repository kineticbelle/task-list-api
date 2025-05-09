from flask import Blueprint, request, make_response
from app.models.task import Task
from app import db

tasks_bp = Blueprint("tasks_bp", __name__, url_prefix="/tasks")

@tasks_bp.post("")
def create_task():
    request_body = request.get_json()
    new_task = Task.from_dict(request_body)

    db.session.add(new_task)
    db.session.commit()

    message = {
        "id": new_task.id,
        "title": new_task.title,
        "description": new_task.description, 
        "completed at": new_task.completed_at,
    }

    return message, 201


@tasks_bp.get("/<tasks>")
def get_saved_tasks(task_id):
    query = db.select(Task)

    query = query.order_by(Task.id)
    tasks = db.session.scalars(query)

    message = [
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "completed at": task.completed_at,

        }
    for task in tasks]

    return message, 200

@tasks_bp.get("")
def no_saved_tasks():
    tasks_response = []
    for task in tasks:
        tasks_response.append(
            {
                "id": task.id,
            "title": task.title,
            "description": task.description,
            "completed at": task.completed_at
            }
        )
    return tasks_response
