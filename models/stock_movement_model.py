from dataclasses import dataclass
from datetime import datetime


@dataclass
class StockMovimentModel:
    id: int | None
    product_id: int
    movement_type: str
    quantity: int
    created_at: datetime
