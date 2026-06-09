import typer

from services import ProductService


app = typer.Typer()

@app.command('add')
def add_product():
    name = typer.prompt('Name')
    description = typer.prompt('Description')
    price = typer.prompt('Price', type=float)
    stock_min = typer.prompt('Stock Min', type=int)
    category_id = typer.prompt('Category ID', type=int)
    supplier_id = typer.prompt('Supplier ID', type=int)

    ProductService.register(
        name,
        description,
        price,
        stock_min,
        category_id,
        supplier_id
    )

    typer.echo('✅ Product created successfully!')


@app.command('list')
def list_products():
    products = ProductService.get_all()

    if not products:
        typer.echo('No products found')
        return
    
    for product in products:
        typer.echo(
            f"""
ID: {product.id}
NAME: {product.name}
DESCRIPTION: {product.description}
PRICE: {product.price}
QUANTITY: {product.quantity}
            """
        )
