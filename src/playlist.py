from src.channel import youtube
import datetime
import isodate


class PlayList:
    def __init__(self, playlist_id: str):
        self.playlist_id = playlist_id # id плейлиста
        self.url = f"https://www.youtube.com/playlist?list={playlist_id}"
        playlist_videos = youtube.playlistItems().list(playlistId=playlist_id, part="contentDetails", maxResults=50).execute()

        self.title = youtube.playlists().list(id=playlist_id, part="snippet").execute()["items"][0]["snippet"]["title"]
        self.video_ids_list = [video["contentDetails"]["videoId"] for video in playlist_videos["items"]]

    @property
    def total_duration(self):
        total_duration = datetime.timedelta(minutes=0)
        response = youtube.videos().list(part="contentDetails, statistics", id=",".join(self.video_ids_list)).execute()

        for video in response["items"]:
            format_convert = video["contentDetails"]["duration"]
            video_duration = isodate.parse_duration(format_convert)
            total_duration += video_duration

        return total_duration

    def show_best_video(self):
        best_video_url = ""
        max_like = 0

        for video_id in self.video_ids_list:
            video_response = youtube.videos().list(part="snippet, statistics, contentDetails, topicDetails", id=video_id).execute()
            video_likes = video_response["items"][0]["statistics"]["likeCount"]

            if int(max_like) < int(video_likes):
                best_video_url = f"https://youtu.be/{video_id}"
                max_like = video_likes
                continue
            else:
                continue

        return best_video_url
