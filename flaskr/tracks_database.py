from flask import Blueprint, render_template
from flaskr.db import get_db

bp = Blueprint('tracks_database', __name__)


@bp.route("/names/")
def names():
    db = get_db()
    unique_names = db.execute('SELECT DISTINCT artist FROM tracks').fetchall()
    count = len(unique_names)
    return render_template('tracks_db_html/names.html', names=unique_names, count_of_unique_names=count)


@bp.route("/tracks/")
@bp.route("/tracks/<genre>/")
def tracks_genre(genre=None):
    db = get_db()
    if genre is None:
        tracks = db.execute('SELECT title FROM tracks').fetchall()
    else:
        tracks = db.execute(f'SELECT tracks.title, genre.title FROM tracks INNER JOIN genre ON tracks.genre_id=genre.id WHERE genre.title=?', (genre, )).fetchall()
    count = len(tracks)
    return render_template('tracks_db_html/tracks_genre.html', titles=tracks, count_of_tracks=count, genre=genre)


@bp.route("/tracks-sec/")
def tracks_sec():
    db = get_db()
    tracks_and_sec = db.execute('SELECT title, length FROM tracks').fetchall()
    return render_template('tracks_db_html/tracks_sec.html', track_plus_length=tracks_and_sec)


@bp.route("/tracks-sec/statistics/")
def tracks_sec_statistics():
    db = get_db()
    average_and_sum_value = db.execute('SELECT AVG(length), SUM(length) FROM tracks').fetchall()
    return render_template('tracks_db_html/tracks_statistics.html', value=average_and_sum_value)
