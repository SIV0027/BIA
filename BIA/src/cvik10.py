from functions.functions import Functions
from cvik10.sclass import SClass

if __name__ == "__main__":

    function, intervals = Functions.sphere()

    sclass: SClass = SClass(function, intervals)
    sclass.search(max_iter = 100,
                  students_count = 20)