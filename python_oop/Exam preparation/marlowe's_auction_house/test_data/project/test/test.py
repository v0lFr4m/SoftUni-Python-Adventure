import unittest
from project.senior_student import SeniorStudent

class TestSeniorStudent(unittest.TestCase):

    def setUp(self):

        self.student = SeniorStudent(student_id="1234", name="Valid Name", student_gpa=3.5)

    def test_init_data(self):
        self.assertEqual(self.student.student_id, "1234")
        self.assertEqual(self.student.name, "Valid Name")
        self.assertEqual(self.student.student_gpa, 3.5)
        self.assertEqual(len(self.student.colleges), 0)

    def test_student_id_too_short(self):
        with self.assertRaises(ValueError) as context:
            self.student.student_id = "123"
        self.assertEqual(str(context.exception), "Student ID must be at least 4 digits long!")

        with self.assertRaises(ValueError) as context:
            self.student.student_id = " 123 "
        self.assertEqual(str(context.exception), "Student ID must be at least 4 digits long!")

    def test_student_id_strip(self):
        self.student.student_id = " 1234 "
        self.assertEqual(self.student.student_id, "1234")

    def test_name_valid(self):
        self.student.name = "Jane Sue"
        self.assertEqual(self.student.name, "Jane Sue")
        self.student.name = "Jane   Sue"
        self.assertEqual(self.student.name, "Jane   Sue")

    def test_name_empty(self):
        with self.assertRaises(ValueError) as context:
            self.student.name = ""
        self.assertEqual(str(context.exception), "Student name cannot be null or empty!")

        with self.assertRaises(ValueError) as context:
            self.student.name = "  "
        self.assertEqual(str(context.exception), "Student name cannot be null or empty!")

    def test_gpa_valid(self):
        self.student.student_gpa = 1.001
        self.assertEqual(self.student.student_gpa, 1.001)

    def test_gpa_exact_boundary(self):
        with self.assertRaises(ValueError) as context:
            self.student.student_gpa = 1.0
        self.assertEqual(str(context.exception), "Student GPA must be more than 1.0!")

    def test_gpa_below_boundary(self):
        with self.assertRaises(ValueError) as context:
            self.student.student_gpa = 0.99
        self.assertEqual(str(context.exception), "Student GPA must be more than 1.0!")

    def test_gpa_valid_above_boundary(self):
        self.student.student_gpa = 1.11
        self.assertEqual(self.student.student_gpa, 1.11)

    def test_apply_to_college_success(self):
        result = self.student.apply_to_college(3.0, "Harvard")
        self.assertEqual(result, "Valid Name successfully applied to Harvard.")
        self.assertIn("HARVARD", self.student.colleges)
        self.assertEqual(len(self.student.colleges), 1)

    def test_apply_to_college_failure(self):
        result = self.student.apply_to_college(3.51, "MIT")
        self.assertEqual(result, "Application failed!")
        self.assertNotIn("MIT", self.student.colleges)
        self.assertEqual(len(self.student.colleges), 0)

    def test_apply_to_college_exact_gpa(self):
        result = self.student.apply_to_college(3.5, "Stanford")
        self.assertEqual(result, "Valid Name successfully applied to Stanford.")
        self.assertIn("STANFORD", self.student.colleges)
        self.assertEqual(len(self.student.colleges), 1)

    def test_apply_to_college_duplicates_case_insensitive(self):
        self.student.apply_to_college(3.0, "Harvard")
        self.student.apply_to_college(3.0, "harvarD")
        self.assertEqual(len(self.student.colleges), 1)

    def test_apply_to_college_multiple(self):
        self.student.apply_to_college(3.0, "Harvard")
        self.student.apply_to_college(3.0, "MIT")
        self.assertEqual(len(self.student.colleges), 2)
        self.assertIn("HARVARD", self.student.colleges)
        self.assertIn("MIT", self.student.colleges)


    def test_update_gpa_success(self):
        result = self.student.update_gpa(3.51)
        self.assertEqual(result, "Student GPA was successfully updated.")
        self.assertEqual(self.student.student_gpa, 3.51)

    def test_update_gpa_failure(self):
        result = self.student.update_gpa(1.0)
        self.assertEqual(result, "The GPA has not been changed!")
        self.assertEqual(self.student.student_gpa, 3.5)

        result = self.student.update_gpa(0.0)
        self.assertEqual(result, "The GPA has not been changed!")
        self.assertEqual(self.student.student_gpa, 3.5)

    def test_update_gpa_boundary(self):
        result = self.student.update_gpa(1.01)
        self.assertEqual(result, "Student GPA was successfully updated.")
        self.assertEqual(self.student.student_gpa, 1.01)

    def test_update_gpa_no_change(self):
        result = self.student.update_gpa(3.5)
        self.assertEqual(result, "Student GPA was successfully updated.")
        self.assertEqual(self.student.student_gpa, 3.5)


    def test_equality_same_gpa(self):
        student2 = SeniorStudent("5678", "Jane Smith", 3.5)
        self.assertTrue(self.student == student2)

    def test_equality_gpa_greater(self):
        student2 = SeniorStudent("5678", "Jane Smith", 3.8)
        self.assertFalse(self.student == student2)

    def test_equality_gpa_smaller(self):
        student2 = SeniorStudent("5678", "Jane Smith", 1.001)
        self.assertFalse(self.student == student2)

if __name__ == "__main__":
    unittest.main()
