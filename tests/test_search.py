import unittest


# Simple mock note class for testing purposes
class MockNote:
    def __init__(self, text):
        self.text = text


class TestSearchNotes(unittest.TestCase):
    def setUp(self):
        self.notes = [
            MockNote("First Note"),
            MockNote("second note"),
            MockNote("Another Note"),
            MockNote("MiXeD CaSe Note"),
        ]

    def test_case_insensitive_match(self):
        # Query in different case should match appropriate notes
        result = search_notes(self.notes, "note")
        self.assertEqual(len(result), 4)

        result = search_notes(self.notes, "FIRST")
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], self.notes[0])

        result = search_notes(self.notes, "mixed case")
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], self.notes[3])

    def test_no_match(self):
        result = search_notes(self.notes, "nonexistent")
        self.assertEqual(len(result), 0)


if __name__ == "__main__":
    unittest.main()
