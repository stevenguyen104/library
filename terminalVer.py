from song import Song
import songsSDK

# song = Song("Are You My Mother?", 72)
# print(songsSDK.add_song(song))

# print(songsSDK.get_songs())

# print(songsSDK.get_song_by_title("Are You My Mother?"))

def print_menu():
    print(""" Choose an option:
    1. print all songs
    2. add a song
    3. update a song
    4. delete a song
    """)

while True:
    print_menu()
    #store command
    response = int(input())

    if response == 1:
        print("Printing all songs")
        for song in songsSDK.get_songs():
            print(song)

    elif response == 2:
        print("What is the name of the song?")
        title = input()
        print ("Who is the artist of the song?")
        artist = input()

        song = Song(title, artist)
        songsSDK.add_song(song)
        print("Adding:" + song.__str__())

    elif response == 3:
        print("What is the current title?")
        title = input()
        print("Artist?")
        artist = input()

        song = Song(title,artist)

        print("What is the new title?")
        new_title = input()
        print("New artist?")
        new_artist = input()

        print(songsSDK.update_song(song, new_title, new_artist))

    elif response == 4:
        print("What is the title?")
        title = input()
        print("Artist?")
        artist = input()

        song = Song(title, artist)

        print(songsSDK.delete_song(song))
        
    else: 
        # assuming users are trying to terminate
        print("Thanks for using this app!")
        break
