import unittest
from project.gallery import Gallery
from unittest import TestCase, main


class TestGallery(TestCase):
    def setUp(self):
        self.gallery = Gallery("ValidName123", "ValidCity", 100.00 , True)

    def test_init(self):
        self.assertEqual("ValidName123", self.gallery.gallery_name)
        self.assertEqual("ValidCity", self.gallery.city)
        self.assertEqual(100.00, self.gallery.area_sq_m)
        self.assertTrue(self.gallery.open_to_public)
        self.assertDictEqual(self.gallery.exhibitions, {})
        self.assertEqual(len(self.gallery.exhibitions), 0)

    def test_property_name(self):
        # WRONG: assertion must be outside context
        with self.assertRaises(ValueError) as ex:
            self.gallery.gallery_name = " ! "
        self.assertEqual("Gallery name can contain letters and digits only!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.gallery.gallery_name = ""
        self.assertEqual("Gallery name can contain letters and digits only!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.gallery.gallery_name = "    "
        self.assertEqual("Gallery name can contain letters and digits only!", str(ex.exception))

    def test_property_city(self):
        self.gallery.city = 'Radnevo'
        self.assertEqual("Radnevo", self.gallery.city)

        with self.assertRaises(ValueError) as ex:
            self.gallery.city = None
        self.assertEqual("City name must start with a letter!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.gallery.city = ""
        self.assertEqual("City name must start with a letter!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.gallery.city = "1Radnevo"
        self.assertEqual("City name must start with a letter!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.gallery.city = "!Radnevo"
        self.assertEqual("City name must start with a letter!", str(ex.exception))

    def test_area_sq_m(self):
        with self.assertRaises(ValueError) as ex:
            self.gallery.area_sq_m = 0.0
        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.gallery.area_sq_m = -1
        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.gallery.area_sq_m = -0.9
        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))

    def test_add_new_exhibition(self):
        result = self.gallery.add_exhibition("name", 1234)
        self.assertEqual('Exhibition "name" added for the year 1234.', result)
        self.assertIn("name", self.gallery.exhibitions)
        self.assertEqual(self.gallery.exhibitions["name"], 1234)

    def test_add_existing_exhibition(self):
        self.gallery.add_exhibition("name", 1234)
        result = self.gallery.add_exhibition("name", 1234)
        self.assertEqual('Exhibition "name" already exists.', result)
        self.assertEqual(self.gallery.exhibitions["name"], 1234)

    def test_add_multiple_exhibitions(self):
        self.gallery.add_exhibition("EX1", 1111)
        self.gallery.add_exhibition("EX2", 2222)
        self.assertEqual(len(self.gallery.exhibitions), 2)
        self.assertIn("EX1", self.gallery.exhibitions)
        self.assertIn("EX2", self.gallery.exhibitions)

    def test_remove_exhibition(self):
        # FIX: must add first
        self.gallery.add_exhibition("EX", 2000)
        result = self.gallery.remove_exhibition("EX")

        # WRONG BEFORE: self.assertEqual(result, result)
        self.assertEqual(result, 'Exhibition "EX" removed.')
        self.assertNotIn("EX", self.gallery.exhibitions)

    def test_remove_non_existing_exhibition(self):
        self.gallery.exhibitions = {"EX1": 1111, "EX2": 2222}
        result = self.gallery.remove_exhibition("UNKNOWN")
        self.assertEqual(result, 'Exhibition "UNKNOWN" not found.')
        self.assertEqual(len(self.gallery.exhibitions), 2)

    def test_remove_second_exhibition(self):
        self.gallery.exhibitions = {"EX1": 1111, "EX2": 2222}
        result = self.gallery.remove_exhibition("EX2")
        self.assertEqual(result, 'Exhibition "EX2" removed.')
        self.assertNotIn("EX2", self.gallery.exhibitions)
        self.assertEqual(len(self.gallery.exhibitions), 1)

    def test_list_when_open_with_exhibitions(self):
        self.gallery.exhibitions = {"EX1": 1111, "EX2": 2222}
        result = self.gallery.list_exhibitions()
        expected = "EX1: 1111\nEX2: 2222"
        self.assertEqual(result, expected)

    def test_list_when_open_no_exhibitions(self):
        self.gallery.exhibitions = {}
        result = self.gallery.list_exhibitions()
        self.assertEqual(result, "")

    def test_list_when_closed(self):
        self.gallery.open_to_public = False
        result = self.gallery.list_exhibitions()
        expected = 'Gallery ValidName123 is currently closed for public! Check for updates later on.'
        self.assertEqual(result, expected)

    def test_list_closed_with_exhibitions(self):
        self.gallery.exhibitions = {"EX1": 1111}
        self.gallery.open_to_public = False
        result = self.gallery.list_exhibitions()
        expected = 'Gallery ValidName123 is currently closed for public! Check for updates later on.'
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
