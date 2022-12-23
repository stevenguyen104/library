import customtkinter
import tkinter
from tkinter import END
from tkinter import *
from PIL import ImageTk, Image
from song import Song
import songsSDK
from youtube_search import YoutubeSearch
import webbrowser

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# keep track of songs for delete func
songs = []

def add_to_list():

    song = Song(title_entry.get(), artist_entry.get())

    # if added and returns rowid
    if(songsSDK.add_song(song)):
        songs.append(song)

        #insert at end of listbox, using values obtained from entry box
        # first arg is where to insert (either index or END)
        listbox.insert(END, song)

        #clear entry boxes after
        title_entry.delete(0, END)
        artist_entry.delete(0, END)

# doesnt remove all copies graphically if duplicates until updated
def remove_from_list():
    #returns tuple with index of current selection
    song_tuple = listbox.curselection()
    #use first elem which is index to pop and store song
    song = songs.pop(song_tuple[0])

    #delete in db using SDK
    if (songsSDK.delete_song(song)):

        #delete graphically using index of current selection
        listbox.delete(song_tuple)

def search_song():
    #grab song
    song_tuple = listbox.curselection()
    song = songs[song_tuple[0]]

    search_keyword = song.title.strip().replace(" ","+") + "+" + song.artist.strip().replace(" ","+")
    results = YoutubeSearch(search_keyword, max_results=1).to_dict()
    id = results[0]['url_suffix']
    callback("https://www.youtube.com" + id)

def callback(url):
   webbrowser.open_new_tab(url)

tk = customtkinter.CTk()
tk.title("Library")
tk.geometry("400x700")

#scrollbar
frame = customtkinter.CTkFrame(master=tk)
frame.pack(pady="10")
my_scrollbar = Scrollbar(frame, orient = VERTICAL)


#create LISTBOX
listbox  = tkinter.Listbox(frame, width = "50", height = "15", yscrollcommand = my_scrollbar.set)

#scrollbar config
my_scrollbar.config(command=listbox.yview)
my_scrollbar.pack(side=RIGHT, fill= BOTH)

#add to interface
listbox.pack()

# insert all songs from database
for song in songsSDK.get_songs():
    songs.append(song)
    listbox.insert(END, song)


entry_frame = customtkinter.CTkFrame(master=tk)
entry_frame.pack(pady="10")

title = tkinter.Label(entry_frame, text="Song Title:", padx="5", pady ="5")
title.pack(pady = "10")

title_entry = tkinter.Entry(entry_frame)
title_entry.pack()

artist = tkinter.Label(entry_frame, text="Artist:", padx="5", pady ="5")
artist.pack(pady = "10")

artist_entry = tkinter.Entry(entry_frame)
artist_entry.pack()

button_frame = customtkinter.CTkFrame(master=tk)
button_frame.pack(pady="10")

button = customtkinter.CTkButton(button_frame, text="Add Song", command = add_to_list)
button.pack(pady="5")

button = customtkinter.CTkButton(button_frame, text="Remove Selected Song", command = remove_from_list)
button.pack(pady="5")

pic = Image.open("wheel.png")
re_pic = pic.resize((50,50))
img = customtkinter.CTkImage(re_pic)
button = customtkinter.CTkButton(master = tk, image = img, text = "Play Selected Song", width = 70, height = 70, command = search_song)
button.pack(pady="10")

tk.mainloop()