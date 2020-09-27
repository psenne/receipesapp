import click
from datetime import datetime
from server import app, db


###### Application options #######

@click.group()
def cli():
    pass


@cli.command()
@click.option('--debug', is_flag=True, help='start in debug mode')
@click.argument('port', default=3000)
def serve(port, debug):
    app.run(debug=debug, port=port)


@cli.command()
def initdb():
    click.echo('Creating the database')
    click.echo(db)
    # db.create_all()
    # db.init_app(app)


def main():
    cli()


if __name__ == "__main__":
    main()
