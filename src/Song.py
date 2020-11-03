class Song:
    def __init__(self, file):
        with open(file, "r") as song_file:
            lines = song_file.read().split("\n")
            lines = [line for line in lines if line != '']
            self.lines = lines

    def get_nth_line(self, n):
        if n in range(0, len(self.lines)+1):
            return self.lines[n-1]
        else:
            raise ValueError("Line number not in range!")

    def get_start_end_lines(self, start, end): # np. 1, 3
        """
        both ends included
        # """
        return "\n\n".join(self.lines[start-1:end])

    def get_whole_song(self):
        pass

#
# song = Song("song.txt")
# print(len(song.lines))
#
# one_to_three = """On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.
#
# On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.
#
# On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."""
#
# # one_to_three = [
# #     "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",
# #     "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.",
# #     "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
# # ]
# # one_to_three_str = "\n\n".join(one_to_three)
#
# print(one_to_three)