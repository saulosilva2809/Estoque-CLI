from dataclasses import dataclass
from datetime import datetime


@dataclass
class ProductModel:
    id: int | None
    name: str
    description: str | None
    price: float
    quantity: int
    stock_min: int
    category_id: int
    supplier_id: int
    created_at: datetime
