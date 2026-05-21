
class Artist:
    def __init__(self, artistName=None, song_id=None, songName=None, releaseDate=None, video_id=None):
        self.artistName = artistName
        self.song_id = song_id
        self.songName = songName
        self.releaseDate = releaseDate
        self.video_id = video_id

    def __str__(self): #formatting
        return f"Name of Artist: {self.artistName}\nName of Song: {self.songName}\nRelease Date: {self.releaseDate}\nYoutube Music Video URL: {self.video_id}\n "
    
    def __repr__(self): #representation: formatting to print list
        return self.__str__() 



