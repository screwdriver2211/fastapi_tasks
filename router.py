from typing import Annotated
from fastapi import Depends, APIRouter
from repository import TaskRepository
from schemas import STaskAdd, STask

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"]
)


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()])->STask:
    task_id = await TaskRepository.add_one(task)
    return {"message": "success", "taskId": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks
