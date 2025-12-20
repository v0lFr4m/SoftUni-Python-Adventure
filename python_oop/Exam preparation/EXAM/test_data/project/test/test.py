from unittest import TestCase, main
from project.star_system import StarSystem

class TestStarSystem(TestCase):
    def setUp(self):
        self.s = StarSystem("Valid Name"
                       , "Red dwarf"
                       ,"Binary"
                       , 3
                       , (1.5, 2.00))
    def test_init_input(self):
        self.assertEqual(self.s.name, "Valid Name")
        self.assertEqual(self.s.star_type, "Red dwarf")
        self.assertEqual(self.s.system_type, "Binary")
        self.assertEqual(self.s.num_planets, 3)
        self.assertEqual(self.s.habitable_zone_range , (1.5 , 2.0))

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as ex:
            self.s.name = ""
        self.assertEqual(str(ex.exception), "Name must be a non-empty string.")

    def test_star_type(self):
        with self.assertRaises(ValueError) as ex:
            self.s.star_type = "Non valid"
        self.assertEqual(str(ex.exception), f"Star type must be one of {sorted(StarSystem._STAR_TYPES)}.")

    def test_system_type(self):
        with self.assertRaises(ValueError) as ex:
            self.s.system_type = "Non Valid"
        self.assertEqual(str(ex.exception) , f"System type must be one of {sorted(StarSystem._STAR_SYSTEM_TYPES)}.")

    def test_num_planets(self):
        with self.assertRaises(ValueError) as ex:
            self.s.num_planets = -5
        self.assertEqual(str(ex.exception), "Number of planets must be a non-negative integer.")

    def test_habitable_zone(self):
        with self.assertRaises(ValueError) as ex:
            self.s.habitable_zone_range = (5 , 2)
        self.assertEqual(str(ex.exception) ,"Habitable zone range must be a tuple of two numbers (start, end) where start < end.")

    def test_habitable_zone_non_tuple(self):
        with self.assertRaises(ValueError) as ex:
            self.s.habitable_zone_range = (1, 2 ,3)
        self.assertEqual(str(ex.exception) , "Habitable zone range must be a tuple of two numbers (start, end) where start < end.")
    def test_gt_habitable(self):
        s1 = StarSystem("Valid", "Red giant", "Single" , 1 , (0.1, 0.3))

        self.assertTrue(self.s > s1)
        self.assertFalse(s1 > self.s)

    def test_gt_non_habitable(self):
        s_dead = StarSystem("Dead Star", "Brown dwarf", "Single", 0, None)
        with self.assertRaises(ValueError) as ex:
            result = self.s > s_dead
        self.assertEqual(str(ex.exception), "Comparison not possible: One or both systems lack a defined habitable zone or planets.")

        with self.assertRaises(ValueError) as ex:
            result = s_dead > self.s
        self.assertEqual(str(ex.exception), "Comparison not possible: One or both systems lack a defined habitable zone or planets.")

    def test_compare_start_systems(self):
        s1 =StarSystem("Valid", "Red giant", "Single", 1, (0.1, 0.3))
        result = StarSystem.compare_star_systems(self.s, s1)
        self.assertEqual(result, "Valid Name has a wider habitable zone than Valid.")

if __name__ == "__main__":
    main()