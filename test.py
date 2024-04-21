from json import JSONDecodeError
import unittest
import verify

# Kilka podstawowych testów

class TestCommon(unittest.TestCase):
    def run_verify(self):
        return verify.verify_json(self.content)


class TestAsterisk(TestCommon):
    def setUp(self):
        with open("test_data/testcase1_False.json") as f:
            self.content = f.read()
    
    def test_case(self):
        self.assertEqual(self.run_verify(), False)


class TestAsteriskInList(TestCommon):
    def setUp(self):
        with open("test_data/testcase2_False.json") as f:
            self.content = f.read()
    
    def test_case(self):
        self.assertEqual(self.run_verify(), False)


class TestAsteriskTwoStatements(TestCommon):
    def setUp(self):
        with open("test_data/testcase3_False.json") as f:
            self.content = f.read()
    
    def test_case(self):
        self.assertEqual(self.run_verify(), False)


class TestAsteriskObjectStatement(TestCommon):
    def setUp(self):
        with open("test_data/testcase4_False.json") as f:
            self.content = f.read()
    
    def test_case(self):
        self.assertEqual(self.run_verify(), False)


class TestNoAsteriskObjectStatement(TestCommon):
    def setUp(self):
        with open("test_data/testcase1_True.json") as f:
            self.content = f.read()
    
    def test_case(self):
        self.assertEqual(self.run_verify(), True)


class TestNoAsterisk(TestCommon):
    def setUp(self):
        with open("test_data/testcase2_True.json") as f:
            self.content = f.read()
    
    def test_case(self):
        self.assertEqual(self.run_verify(), True)


class TestFailJson(TestCommon):
    def setUp(self):
        with open("test_data/testcase1_Fail.json") as f:
            self.content = f.read()
    
    def test_case(self):
        with self.assertRaises(JSONDecodeError):
            self.run_verify()


class TestFailFormat(TestCommon):
    def setUp(self):
        with open("test_data/testcase2_Fail.json") as f:
            self.content = f.read()
    
    def test_case(self):
        with self.assertRaises(ValueError):
            self.run_verify()


if __name__ == '__main__':
    unittest.main()