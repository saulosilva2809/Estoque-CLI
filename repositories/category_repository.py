from datetime import datetime

from database.connection import get_connection
from enums.category_enum import CategoryOrderBy
from models import CategoryModel


class CategoryRepository():
    def _row_to_category(self, row) -> CategoryModel:
        return CategoryModel(
            id=row['id'],
            name=row['name'],
            description=row['description'],
            created_at=datetime.fromisoformat(row['created_at'])
        )
    
    def create(self, category: CategoryModel):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO categories (
                name,
                description,
                created_at
            )
            VALUES (?, ?, ?)
            """,
            (
                category.name,
                category.description,
                category.created_at
            )
        )

        connection.commit()
        connection.close()

    def find_by_id(self, category_id: int) -> CategoryModel | None:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM categories
            WHERE id = ?
            """,
            (category_id,)
        )

        row = cursor.fetchone()
        connection.close()

        if row is None:
            return None
        
        return self._row_to_category(row)
    
    def _find_by_name(self, category_name: str) -> CategoryModel | None:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM categories
            WHERE name = ?
            """,
            (category_name,)
        )

        row = cursor.fetchone()
        connection.close()

        if row is None:
            return None
        
        return self._row_to_category(row)
    
    def find_all(self, order_by: CategoryOrderBy = CategoryOrderBy.id) -> list[CategoryModel]:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            f"""
            SELECT *
            FROM categories
            ORDER BY {order_by.value}
            """
        )

        rows = cursor.fetchall()
        connection.close()

        return [
            self._row_to_category(row)
            for row in rows
        ]
    
    def update(self, category: CategoryModel):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE categories
            SET
                name = ?,
                description = ?
            
            WHERE id = ?
            """,
            (
                category.name,
                category.description,
                category.id
            )
        )

        connection.commit()
        connection.close()

    def delete(self, category_id: int):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM categories
            WHERE id = ?
            """,
            (category_id,)
        )

        connection.commit()
        connection.close()
