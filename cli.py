import typer

from commands import app as product_app


app = typer.Typer()

app.add_typer(product_app, name='product')

if __name__ == '__main__':
    app()
