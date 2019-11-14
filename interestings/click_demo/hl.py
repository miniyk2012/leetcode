import click


@click.command()
@click.argument('x')
@click.argument('y')
def hello(x, y):
    print(x, y)


