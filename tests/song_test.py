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

    def test_line_number_is_a_str(self):
        with self.assertRaisesWithMessage(ValueError):
            self.song.get_nth_line("second")

    def test_line_number_is_a_float(self):
        with self.assertRaisesWithMessage(ValueError):
            self.song.get_nth_line(2.5)

    def test_get_start_end_lines_1_to_3(self):

        one_to_three = """On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.

On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.

On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."""

        self.assertEqual(self.song.get_start_end_lines(1, 3), one_to_three)

    def test_get_start_end_lines_6_to_9(self):

        six_to_nine = """On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."""

        self.assertEqual(self.song.get_start_end_lines(6, 9), six_to_nine)

    def test_get_start_end_lines_first_number_out_of_range(self):
        with self.assertRaisesWithMessage(ValueError):
            self.song.get_start_end_lines(-2, 5)

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

    def tearDown(self):
        self.song = None


if __name__ == '__main__':
    unittest.main()