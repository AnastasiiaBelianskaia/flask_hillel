from flask import Blueprint, render_template
from flaskr.db import get_db, close_db


bp = Blueprint('tracks_database', __name__)


@bp.route("/names/")
def names():
    db = get_db()
    unique_names = db.execute('SELECT DISTINCT artist FROM tracks').fetchall()
    count = len(unique_names)
    close_db()
    return render_template('tracks_db_html/names.html', names=unique_names, count_of_unique_names=count)


@bp.route("/tracks/")
def tracks():
    db = get_db()
    all_tracks = db.execute('SELECT title FROM tracks').fetchall()
    print(all_tracks, '+++')
    count = len(all_tracks)
    close_db()
    return render_template('tracks_db_html/tracks.html', tracks=all_tracks, count_of_tracks=count)


@bp.route("/tracks/<genre>/")
def tracks_genre(genre):
    db = get_db()
    name_of_genre = genre
    tracks_of_genre = db.execute(f'SELECT tracks.title, genre.title FROM tracks INNER JOIN genre ON tracks.genre_id=genre.id WHERE genre.title="{genre}"').fetchall()
    count = len(tracks_of_genre)
    close_db()
    return render_template('tracks_db_html/tracks_genre.html', titles=tracks_of_genre, count_of_tracks=count,
                           genre=name_of_genre)


@bp.route("/tracks-sec/")
def tracks_sec():
    db = get_db()
    tracks_and_sec = db.execute('SELECT title, length FROM tracks').fetchall()
    close_db()
    return render_template('tracks_db_html/tracks_sec.html', track_plus_length=tracks_and_sec)


@bp.route("/tracks-sec/statistics/")
def tracks_sec_statistics():
    db = get_db()
    average_value = db.execute('SELECT AVG(length) FROM tracks').fetchone()
    sum_value = db.execute('SELECT SUM(length) FROM tracks').fetchone()
    close_db()
    return render_template('tracks_db_html/tracks_statistics.html', average=average_value, sum_of_sec=sum_value)
