from functions.run_python_file import run_python_file
from functions.write_file import write_file
def test():
   res = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
   return res
if __name__ == "__main__":
    test()