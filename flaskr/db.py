import sqlite3
import click
from flask import current_app, g


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as file:
        db.executescript(file.read().decode('utf8'))


def fill_db():
    db = get_db()
    with current_app.open_resource('data_for_database.sql') as file:
        db.executescript(file.read().decode('utf8'))
    db.commit()


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Initialized the database.')


@click.command('fill-db')
def fill_db_command():
    fill_db()
    click.echo('The database is filled.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(fill_db_command)
