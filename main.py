import json

playlist = {}

# add a song to the playlist
def add_song_to_playlist():
    title = input("Enter the title of the song: ")
    artist = input("Enter the artist of the song: ")
    playlist[title] = artist
    print(f"{title} by {artist} has been added to the playlist.")

# remove a song from the playlist
def remove_song_from_playlist():
    title = input("Enter the title of the song you want to remove: ")
    if title in playlist:
        del playlist[title]
        print(f"{title} has been removed from the playlist.")
    else:
        print("Song not found in playlist.")

# display the current playlist
def display_playlist():
    if not playlist:
        print("Playlist is empty.")
    else:
        print("Current Playlist:")
        for title, artist in playlist.items():
            print(f"{title} - {artist}")

# save the playlist to a JSON file
def save_playlist_to_file():
    with open("playlist.json", "w") as f:
        json.dump(playlist, f)
    print("Playlist has been saved to playlist.json.")

# user prompts for managing the playlist
while True:
    print("Select an option:")
    print("1. Add song to playlist")
    print("2. Remove song from playlist")
    print("3. Display playlist")
    print("4. Save playlist")
    print("5. Exit")
    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        add_song_to_playlist()
    elif choice == "2":
        remove_song_from_playlist()
    elif choice == "3":
        remove_song_from_playlist()
    elif choice == "4":
        save_playlist_to_file()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
