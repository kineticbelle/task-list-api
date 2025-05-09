from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from datetime import datetime
from typing import Optional, Dict, Any

class Task(db.Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    completed_at: Mapped[Optional[datetime]]
    
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        title = data.get("title", "")
        description = data.get("description", "")
        completed_at = data.get("completed_at", None)

        if isinstance(completed_at, str):
            try:
                completed_at = datetime.fromisoformat(completed_at)
            except ValueError:
                completed_at = None

        return cls(
            title=title, 
            description=description, 
            completed_at=completed_at
        )
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "is_complete": self.completed_at is not None
        }