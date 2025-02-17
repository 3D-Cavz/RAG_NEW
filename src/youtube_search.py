import requests
from config import YOUTUBE_API_KEY

def search_youtube(query):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "maxResults": 1,  # Get only the top result
        "type": "video",
        "key": YOUTUBE_API_KEY,
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "items" in data and len(data["items"]) > 0:
        video = data["items"][0]
        video_id = video["id"]["videoId"]
        video_title = video["snippet"]["title"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        return {"title": video_title, "url": video_url}

    return {"error": "No video found"}
