from datetime import datetime

from models import ProductModel
from repositories import ProductRepository


class ProductService:
    def register(
        name: str,
        description: str,
        price: float,
        stock_min: int,
        category_id: int,
        supplier_id: int
    ):
        if price < 0:
            raise ValueError('Price must be greater than zero')
        
        if stock_min < 0:
            raise ValueError('The minimum stock must be greater than zero')
        
        # TODO: criar validação para category_id e supplier_id
        
        product = ProductModel(
            id=id,
            name=name,
            description=description,
            price=price,
            quantity=0,
            stock_min=stock_min,
            category_id=category_id,
            supplier_id=supplier_id,
            created_at=datetime.now()
        )

        ProductRepository().create(product)

    def get(product_id: int):
        return ProductRepository().find_by_id(product_id)

    def get_all():
        return ProductRepository().find_all()
