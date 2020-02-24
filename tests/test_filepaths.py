from filepaths import Root
import unittest
import os


class TestFilepaths(unittest.TestCase):

    def test_bad_dir(self):
        with self.assertRaises(Exception):
            Root(__file__, 2).paths()

    def test_bad_depth(self):
        with self.assertRaises(Exception):
            Root(__file__, -1).paths()

    def test_two_paths(self):
        with self.assertRaises(Exception):
            Root(__file__, 0, alt_path='Jetsons/').paths()

    def test_no_paths(self):
        with self.assertRaises(Exception):
            Root(depth=1).paths()

    def test_dir_path(self):
        paths = Root(__file__).paths()
        testdir = paths.testdir.path
        truth = os.path.abspath(os.path.dirname(__file__)) + '/testdir/'
        self.assertEqual(testdir, truth)

    def test_files(self):
        paths = Root(__file__).paths()
        files = paths.testdir.Jetsons.files
        self.assertEqual(set(files), {'George', 'Jane'})

    def test_hidden(self):
        paths = Root(__file__, ignore_hidden=False).paths()
        hidden = paths.testdir.Turing.filepaths
        paths = Root(__file__, ignore_hidden=True).paths()
        not_hidden = paths.testdir.Turing.files

        self.assertEqual(len(hidden), 3)
        self.assertEqual(len(not_hidden), 2)


if __name__ == "__main__":
    unittest.main()
