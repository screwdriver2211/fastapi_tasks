from typing import Optional

from pydantic import BaseModel


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


tasks = []


class STask(STaskAdd):
    id: int
