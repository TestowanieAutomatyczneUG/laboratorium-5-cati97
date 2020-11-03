class Song:
    def __init__(self, file):
        with open(file, "r") as song_file:
            lines = song_file.read().split("\n")
            lines = [line for line in lines if line != '']
            self.lines = lines

    def get_nth_line(self, n):
        if n == 1:
            return self.lines[0]
        elif n == 3:
            return self.lines[2]

    def get_start_end_lines(self, start, end):
        """
        both ends included
        """
        pass

    def get_whole_song(self):
        pass


# song = Song("song.txt")
# print(len(song.lines))