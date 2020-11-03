import unittest
from src.Song import Song


class SongTest(unittest.TestCase):
    def setUp(self) -> None:
        self.song = Song("../src/song.txt")

    def test_get_nth_line(self):
        self.assertEqual(self.song.get_nth_line(1), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")


if __name__ == '__main__':
    unittest.main()