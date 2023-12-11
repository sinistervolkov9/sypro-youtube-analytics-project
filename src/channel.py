import os
import json
import requests
from googleapiclient.discovery import build

API_KEY: str = os.getenv('YOUTUBE_API_KEY')

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.url = f"https://www.youtube.com/cannel/{self.channel_id}"
        self.response = requests.get(self.url)

        # Спец. объект для работы с API
        self.youtube = build('youtube', 'v3', developerKey=API_KEY)
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.response, indent=4, ensure_ascii=False))
