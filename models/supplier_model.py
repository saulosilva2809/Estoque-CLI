from dataclasses import dataclass
from datetime import datetime


@dataclass
class SupplierModel:
    id: int | None
    name: str
    email: str
    phone: str
    city: str
    created_at: datetime
