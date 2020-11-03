class Song:
    def __init__(self, file):
        with open(file, "r") as song_file:
            lines = song_file.read().split("\n")
            lines = [line for line in lines if line != '']
            self.lines = lines

    def get_nth_line(self, n):
        if n in range(1, len(self.lines)+1):
            return self.lines[n-1]
        else:
            raise ValueError("Line number not in range!")

    def get_start_end_lines(self, start, end):
        """
        both ends included
        """
        if start not in range(1, len(self.lines)+1):
            raise ValueError("Start value not in range")
        elif end not in range(1, len(self.lines)+1):
            raise ValueError("End value not in range")
        else:
            return "\n\n".join(self.lines[start-1:end])

    def get_whole_song(self):
        pass
