from atomicwrites import atomic_write
import unittest

def auto_writing(func):
    def wrapTheFunction(something):
        with atomic_write('test.txt', overwrite = True) as f:
            f.write(something)
        return func
    return wrapTheFunction

@auto_writing
def writing(something):
    print("writing {}!".format(something))

#test
class TestWriting(unittest.TestCase):
    def test_writing_correct(self):
        content = input("Please enter:")
        writing(content)
        result = open("test.txt","r").read()
        expected_result = open("test.txt","r").read()
        self.assertTrue(expected_result == result)

if __name__ = = "__main__":
   TestWriting().test_writing_correct()