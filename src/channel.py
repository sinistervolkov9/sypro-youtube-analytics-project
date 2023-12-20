import os
import json
from googleapiclient.discovery import build

API_KEY: str = os.getenv("YOUTUBE_API_KEY")
youtube = build("youtube", "v3", developerKey=API_KEY)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id  # id канала
        channel = youtube.channels().list(id=self.channel_id, part="snippet, statistics").execute()  # название канала

        self.title = channel["items"][0]["snippet"]["title"]
        self.description = channel["items"][0]["snippet"]["description"]  # описание канала
        self.url = f"https://www.youtube.com/channel/{channel_id}]"  # ссылка на канал
        self.sub_count = channel["items"][0]["statistics"]["subscriberCount"]  # количество подписчиков
        self.video_count = channel["items"][0]["statistics"]["videoCount"]  # количество видео
        self.view_count = channel["items"][0]["statistics"]["viewCount"]  # общее количество просмотров

    def __add__(self, other_channel):
        return int(self.sub_count) + int(other_channel.sub_count)

    def __sub__(self, other_channel):
        return int(self.sub_count) - int(other_channel.sub_count)

    def __eq__(self, other_channel):
        """
        Сравнение на равенство ==
        """
        return self.sub_count == other_channel.sub_count

    def __lt__(self, other_channel):
        """
        Сравнение на меньше <
        """
        return self.sub_count < other_channel.sub_count

    def __gt__(self, other_channel):
        """
        Сравнение на больше >
        """
        return self.sub_count > other_channel.sub_count

    def __le__(self, other_channel):
        """
        Сравнение на меньше или равно <=
        """
        return self.sub_count <= other_channel.sub_count

    def __ge__(self, other_channel):
        """
        Сравнение на больше или равно >=
        """
        return self.sub_count >= other_channel.sub_count

    def __ne__(self, other_channel):
        """
        Сравнение на неравенство !=
        """
        return self.sub_count != other_channel.sub_count

    def __str__(self):
        return f"{self.title} ({self.url})"

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(f"Channel ID: {self.channel_id}")
        print(f"Title: {self.title}")
        print(f"Descripstion: {self.description}")
        print(f"Channel url: {self.url}")
        print(f"Subscriber count: {self.sub_count}")
        print(f"Video count: {self.video_count}")
        print(f"View count: {self.view_count}")
        return

    @classmethod
    def get_service(cls):
        return youtube

    def to_json(self, file):
        with open(file, "w") as file:
            data = {"ID": self.channel_id,
                    "Title": self.title,
                    "Descripstion": self.description,
                    "Channel url": self.url,
                    "Subscriber count": self.sub_count,
                    "Video count": self.video_count,
                    "View count": self.view_count}
            json.dump(data, file, ensure_ascii=False)
