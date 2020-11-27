import unittest
import xmlrunner


def runner(output='python_tests_xml'):
    return xmlrunner.XMLTestRunner(
        output=output
        )

def find_tests():
    print("FInding the test")
    return unittest.TestLoader().discover('/home/labsuser/jenkins/workspace/PyJ', 'test_*.py')
if __name__ == '__main__':
    print("Starting the test")
    runner().run(find_tests())
    print("completed")
