from src.channel import *


class Video:
    def __init__(self, video_id: str):
        self.video_id = video_id  # id видео
        video = youtube.videos().list(id=video_id, part="snippet, statistics").execute()

        self.title = video["items"][0]["snippet"]["title"]  # название видео
        self.url = f"https://www.youtube.com/watch?v={video_id}"  # ссылка на видео
        self.video_view_count = video["items"][0]["statistics"]["viewCount"]  # количество просмотров
        self.video_like_count = video["items"][0]["statistics"]["likeCount"]  # количество лайков

    def __str__(self):
        return f'{self.title}'


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
