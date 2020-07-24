import click


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
@click.option('--owner', default='vkhramov', help='script owner')
def hello(count, name, owner):
    """Simple program that greets NAME for total of COUNT times"""
    for x in range(count):
        click.echo("Hello %s!" % name)
    click.echo("Owner is %s!" % owner)
if __name__ == '__main__':
    hello()
