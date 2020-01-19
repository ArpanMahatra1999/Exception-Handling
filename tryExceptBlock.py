import sys

def linux_interaction():
    assert ('linux' in sys.platform),"Function will run only on Linux."

try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print("Linux function was not executed.")