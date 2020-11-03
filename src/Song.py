class Song:
    def __init__(self, file):
        with open(file, "r") as song_file:
            lines = song_file.read().split("\n")
            lines = [line for line in lines if line != '']
            self.lines = lines

    def get_nth_line(self, n):
        pass

    def get_start_end_lines(self, start, end):
        """
        both ends included
        """
        pass

    def get_whole_song(self):
        pass


