import os
import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic
from pprint import pprint

# Optional Troubleshooting Step - Check for browser.json before doing anything else
if not os.path.exists("browser.json"):
    print("browser.json not found.")
    print("You need to authenticate with YouTube Music first.")
    print("Run one of these commands in your terminal from this project folder:\n")
    print("  Mac:     pbpaste | ytmusicapi browser")
    print("  Windows: ytmusicapi browser\n")
    print("Copy the request headers from Firefox first.")
    print("This will create browser.json.")
    exit()

def get_songs(): 
    # Scraping Bakeboard Hot 100
    date = input(
        "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "
    )
    url = f"https://appbrewery.github.io/bakeboard-hot-100/{date}"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    song_names = [tag.getText().strip() for tag in soup.select("h3.chart-entry__title")]
    return song_names[:10],date
# print(song_names)



def create_playlist(date):

    # Verify authentication works
    # pprint(playlists)
    # print(f"Found {len(playlists)} playlists in your library.")

    PLAYLIST_NAME = f"{date} Billboard 100"

    playlists = yt.get_library_playlists()

    playlist_id = None

    for p in playlists:
        if p["title"] == PLAYLIST_NAME:
            playlist_id = p["playlistId"]
            break

    if playlist_id:
        print(f"This playlist already exists: {playlist_id}.")
    else:
        playlist_id = yt.create_playlist(
            PLAYLIST_NAME,
            f"Playlist with the hottest songs from {date}",
            privacy_status="PRIVATE",
        )
        print("Playlist created.")
    
    return playlist_id

def add_songs(song_names,playlist_id):
    for song in song_names:
        try:
            search_results = yt.search(song,filter='songs',limit=1)
            yt.add_playlist_items(playlist_id, [search_results[0]["videoId"]])
            print(f"Added: {song}")
        except Exception as e:
            print(f"skipped: {song} | reason: {e}")

yt = YTMusic("browser.json")

song_list, date = get_songs()
if song_list:
    playlist = create_playlist(date)
    add_songs(song_list, playlist)
else:
    print(f"No Songs found on date {date}")