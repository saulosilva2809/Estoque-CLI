from enum import Enum


class CategoryOrderBy(str, Enum):
    id = 'id'
    name = 'name'
    created_at = 'created_at'
