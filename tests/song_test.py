import unittest
from src.Song import Song


class SongTest(unittest.TestCase):
    def setUp(self) -> None:
        self.song = Song("../src/song.txt")

    def test_get_nth_line(self):
        self.assertEqual(self.song.get_nth_line(1), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")

    def test_get_nth_line_third_line(self):
        self.assertEqual(self.song.get_nth_line(3), "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_get_last_line(self):
        self.assertEqual(self.song.get_nth_line(12), "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_line_number_out_in_range(self):
        with self.assertRaisesWithMessage(ValueError):
            self.song.get_nth_line(14)

    def test_line_number_out_in_range_negative_num(self):
        with self.assertRaisesWithMessage(ValueError):
            self.song.get_nth_line(-2)

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

    def tearDown(self):
        self.song = None


if __name__ == '__main__':
    unittest.main()