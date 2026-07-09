from ytmusicapi import YTMusic

ytmusic = YTMusic()
print(ytmusic)
# from bs4 import BeautifulSoup
# import requests

# user_input = input("which year do you wamt to travel to? Provide date in this format YYYY-MM-DD: ")
# header = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
#     "Accept": "text/plain",
#     "Content-Type": "text/plain"
# }
# user_input = "2026-04-18"
# url = f"https://appbrewery.github.io/bakeboard-hot-100/{user_input}"
# response = requests.get(url, headers=header)
# response.raise_for_status()
# web_data = response.text

# soup = BeautifulSoup(web_data, "html.parser")
# all_songs = soup.find_all('div',class_="chart-entry__info")
# song_list=[]
# songs_dict = {}

# for song in all_songs:
#     title = song.find('h3', class_='chart-entry__title').text
#     artist = song.find('span', class_='chart-entry__artist').text
    
#     if title and artist:
#         song_title = title.strip()
#         song_artist = artist.strip()
    
#         songs_dict = {
#             "title":song_title,
#             "artist":song_artist,
#         }
        
#         song_list.append(songs_dict)
# print(song_list)