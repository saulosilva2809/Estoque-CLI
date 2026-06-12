import typer

from DTOs.category_dtos import CreateCategoryDTO
from enums.category_enum import CategoryOrderBy
from exceptions.category_exceptions import (
    CategoryAlreadyExists,
    CategoryNotFound
)
from services import CategoryService


app = typer.Typer()

@app.command('add')
def add_category():
    name = typer.prompt('Name')
    description = typer.prompt('Description (optional)', default='')

    try:
        data = CreateCategoryDTO(name, description or None)
        CategoryService().register(data)

        typer.echo('✅ Category created successfully!')

    except CategoryAlreadyExists:
        typer.echo(f'❌ Category "{name}" already exists.')


@app.command('list')
def list_categories(order_by: CategoryOrderBy = typer.Option(
    CategoryOrderBy.id
)):
    categories = CategoryService().get_all(order_by)

    if not categories:
        typer.echo('No categories found.')
        return
    
    for category in categories:
        typer.echo(f'ID: {category.id}')
        typer.echo(f'Name: {category.name}')
        typer.echo(f'Description: {category.description}')
        typer.echo('-------------------------------------')


@app.command('get')
def get_category(category_id: int):
    try:
        category = CategoryService().get(category_id)

        typer.echo(f'ID: {category.id}')
        typer.echo(f'Name: {category.name}')
        typer.echo(f'Description: {category.description}')
    
    except CategoryNotFound:
        typer.echo(f'❌ Category not found.')

@app.command('update')
def update_category(category_id: int):
    service = CategoryService()

    try:
        category = service.get(category_id)

        name = typer.prompt('Name', default=category.name)
        description = typer.prompt('Description (optional)', default=category.description or '')

        data = CreateCategoryDTO(name, description or None)
        service.update(category_id, data)

        typer.echo('✅ Category updated successfully!')

    except CategoryNotFound:
        typer.echo(f'❌ Category not found.')


@app.command('delete')
def delete_category(category_id: int):
    confirm = typer.confirm(f'Delete category {category_id}?')

    if not confirm:
        typer.echo('Operation cancelled.')
        return

    try:
        CategoryService().delete(category_id)
        typer.echo('✅ Category deleted successfully!')
    
    except CategoryNotFound:
        typer.echo(f'❌ Category not found.')
