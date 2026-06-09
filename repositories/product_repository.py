from datetime import datetime

from database.connection import get_connection
from models import ProductModel


class ProductRepository():
    def _row_to_product(self, row) -> ProductModel:
        return ProductModel(
            id=row['id'],
            name=row['name'],
            description=row['description'],
            price=row['price'],
            quantity=row['quantity'],
            stock_min=row['stock_min'],
            category_id=row['category_id'],
            supplier_id=row['supplier_id'],
            created_at=datetime.fromisoformat(row['created_at'])
        )

    def create(self, product: ProductModel):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERTO INTO products (
                name,
                description,
                price,
                quantity,
                stock_min,
                category_id,
                supplier_id,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                product.name,
                product.description,
                product.price,
                product.quantity,
                product.stock_min,
                product.category_id,
                product.supplier_id,
                product.created_at
            )
        )

        connection.commit()
        connection.close()

    def find_by_id(self, product_id: int) -> ProductModel | None:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT * 
            FROM products
            WHERE id = ?
            """,
            (product_id,)
        )

        row = cursor.fetchone()
        connection.close()

        if row is None:
            return None
        
        return self._row_to_product(row)
    
    def find_all(self) -> list[ProductModel]:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM products
            ORDER BY name
            """
        )

        rows = cursor.fetchall()
        connection.close()

        return [
            self._row_to_product(row)
            for row in rows
        ]
    
    def delete(self, product_id: int):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM products
            WHERE id = ?
            """,
            (product_id,)
        )

        connection.commit()
        connection.close()

    def update(self, product: ProductModel):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE products
            SET
                name = ?,
                description = ?,
                price = ?,
                quantity = ?,
                stock_min = ?,
                category_id = ?,
                supplier_id = ?
            WHERE id = ?
            """,
            (
                product.name,
                product.description,
                product.price,
                product.quantity,
                product.stock_min,
                product.category_id,
                product.supplier_id,
                product.id
            )
        )

        connection.commit()
        connection.close()

    def update_quantity(
            self,
            product_id: int,
            quantity: int
    ):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE products
            SET quantity = ?
            WHERE id = ?
            """,
            (
                quantity,
                product_id
            )
        )

        connection.commit()
        connection.close()
