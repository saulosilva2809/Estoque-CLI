from datetime import datetime

from DTOs.category_dtos import (
    CreateCategoryDTO,
    UpdateCategoryDTO
)
from enums.category_enum import CategoryOrderBy
from exceptions.category_exceptions import (
    CategoryAlreadyExists,
    CategoryNotFound
)
from models import CategoryModel
from repositories import CategoryRepository


class CategoryService():
    def register(self, data: CreateCategoryDTO):
        repo = CategoryRepository()

        if repo._find_by_name(data.name):
            raise CategoryAlreadyExists()

        category = CategoryModel(
            id=id,
            name=data.name,
            description=data.description,
            created_at=datetime.now()
        )

        repo.create(category)

    def get(self, category_id: int):
        category = CategoryRepository().find_by_id(category_id)

        if not category:
            raise CategoryNotFound()
        
        return category
    
    def get_all(self, order_by: CategoryOrderBy = CategoryOrderBy.id):
        return CategoryRepository().find_all(order_by)
    
    def update(self, category_id: int, data: UpdateCategoryDTO):
        repo = CategoryRepository()
        category = repo.find_by_id(category_id)
    
        if category is None:
            raise CategoryNotFound()
        
        if data.name is not None:
            category.name = data.name
        
        if data.description is not None:
            category.description = data.description

        repo.update(category)

    def delete(self, category_id: int):
        category = self.get(category_id)

        if category is None:
            raise CategoryNotFound()
        
        CategoryRepository().delete(category.id)
