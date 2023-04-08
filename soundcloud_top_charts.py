import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_html_content(url):
    """Send a GET request to the website and return the HTML content."""
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while sending the GET request: {e}")
        return None
    else:
        return response.content

def parse_html_content(html_content):
    """Parse the HTML content using BeautifulSoup and return the parsed object."""
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
    except Exception as e:
        print(f"An error occurred while parsing the HTML content: {e}")
        return None
    else:
        return soup

def get_songs(soup):
    """Extract the list of songs from the parsed HTML object."""
    # Find the section with class "sounds"
    sounds = soup.find('section', class_='sounds')
    if not sounds:
        print("Could not find the section with class 'sounds'.")
        return []

    # Find the list of songs using the "ol" tag
    songs = sounds.find('ol')
    if not songs:
        print("Could not find the list of songs using the 'ol' tag.")
        return []

    # Create an empty list to store the song information
    song_list = []

    # Iterate through the songs
    for song in songs.find_all('li'):
        # Find the title and singer name
        title_element = song.find('a', href=True)
        if title_element:
            title = title_element.text.strip()
        else:
            print("Could not find the title element.")
            continue

        singer_element = song.find('h2', itemprop='name')
        if singer_element:
            singer = (singer_element.text.strip()).split("by")[1]
        else:
            print("Could not find the singer element.")
            continue

        # Find the publish date and time
        time_element = song.find('time')
        if time_element:
            date_time = time_element.text.strip()
            date, time = date_time.split('T')
            time = time[:-1]
        else:
            print("Could not find the time element.")
            continue

        # Find the song link
        link_element = song.find('a', href=True)
        if link_element:
            link = "https://soundcloud.com" + link_element['href']
        else:
            print("Could not find the link element.")
            continue

        # Append the song information to the list
        song_list.append([title, singer, date, time, link])

    return song_list

def create_dataframe(song_list):
    """Create a pandas DataFrame with the song information."""
    df = pd.DataFrame(song_list, columns=['Top_Charts', 'Artist', 'Published_On', 'Publish_Time', 'Source'], index=range(1, len(song_list) + 1))
    return df

def main():
    url = "https://soundcloud.com/charts/top?genre=house&country=all-countries"
    html_content = get_html_content(url)
    if html_content:
        soup = parse_html_content(html_content)
        if soup:
            song_list = get_songs(soup)
            df = create_dataframe(song_list)
            df.to_csv("output.csv", index=False)

if __name__ == '__main__':
    main()