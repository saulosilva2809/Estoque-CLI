import typer

from commands.category_commands import app as category_app
from commands.product_commands import app as product_app


app = typer.Typer()

app.add_typer(product_app, name='product')
app.add_typer(category_app, name='category')

if __name__ == '__main__':
    app()
