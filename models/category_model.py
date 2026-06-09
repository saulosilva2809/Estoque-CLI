from dataclasses import dataclass
from datetime import datetime


@dataclass
class CategoryModel:
    id: int | None
    name: str
    description: str
    created_at: datetime
