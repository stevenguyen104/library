import sqlite3
from song import Song

#creates cursor obj
def cursor():
    return sqlite3.connect('songs.db').cursor()

#create connection
c = cursor()
#create table named songs if it doesnt exist
c.execute('CREATE TABLE IF NOT EXISTS songs (title TEXT, artist TEXT)')
#close connection
c.connection.close()

def add_song(song):
    c = cursor()

    # with will auto commit but doenst close connection
    with c.connection:
        #insert into table with values, use tuple after command for val
        c.execute('INSERT INTO songs VALUES (?, ?)', (song.title, song.artist))
    c.connection.close()

    #returns id of inserted
    return c.lastrowid

#get all
def get_songs():
    c = cursor()
    songs = []

    with c.connection:
        #select all columns by using c.execute('SELECT * FROM songs')
        for song in c.execute('SELECT * FROM songs'):
            #append new Song obj using first elem, title and second elem, artist
            songs.append(Song(song[0], song[1]))

    c.connection.close()

    #c.fetchall returns all 
    return songs

def get_song_by_title(title):
    c = cursor()

    with c.connection:
        # use tuple instead of str concatenation with + bc of injection risk
        c.execute('SELECT * FROM songs WHERE title =?', (title,))

    # return c.fetchone() (as tuple)

    data = c.fetchone()

    c.connection.close()

    # if not found
    if not data:
        return None
    
    # else return new Song obj with title, auth, as first and second elem
    return Song(data[0], data[1])

def update_song(song, new_title, new_artist):
    c = cursor()

    with c.connection:
        c.execute('UPDATE songs SET title =?, pages =? WHERE title =? and artist =?', 
        (new_title, new_artist, song.title, song.artist))
    song = get_song_by_title(new_title)

    c.connection.close()

    return song

#if want to delete only one, use id
def delete_song(song):
    c = cursor()

    with c.connection:
        c.execute('DELETE FROM songs WHERE title =? and artist =?', (song.title, song.artist))
    #store num of deleted rows
    rows = c.rowcount

    c.connection.close

    return rows
