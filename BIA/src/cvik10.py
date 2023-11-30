from functions.functions import Functions
from cvik10.sclass import SClass

if __name__ == "__main__":

    function, intervals = Functions.michalewicz(m = 10)

    sclass: SClass = SClass(function, intervals)
    sclass.search(max_iter = 100,
                  students_count = 20)