CREATE TABLE tracks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100),
    artist VARCHAR(100),
    length INTEGER,
    genre_id INTEGER NOT NULL,
    FOREIGN KEY (genre_id) REFERENCES genre(id)
);

CREATE TABLE genre(
    id INTEGER PRIMARY KEY,
    title VARCHAR(100)
);

