##
# 2WF90 Algebra for Security -- Software Assignment 2
# Polynomial and Finite Field Arithmetic
# solve.py
#
#
# Group number:
# group_number 
#
# Author names and student IDs:
# Oana Alexandra Anuta (2309025) 
# Diana Dumitrescu (2246767)
# Sara-Maria Dumitrescu (2310007)
# Alexandru Radu (2304554)
##

# Import built-in json library for handling input/output 
import json



def solve_exercise(exercise_location : str, answer_location : str):
    """
    solves an exercise specified in the file located at exercise_location and
    writes the answer to a file at answer_location. Note: the file at
    answer_location might not exist yet and, hence, might still need to be created.
    """
    
    # Open file at exercise_location for reading.
    with open(exercise_location, "r") as exercise_file:
        # Deserialize JSON exercise data present in exercise_file to corresponding Python exercise data 
        exercise = json.load(exercise_file)
        

    ### Parse and solve ###

    # Check type of exercise
    if exercise["type"] == "polynomial_arithmetic":
        # Check what task within the polynomial arithmetic tasks we need to perform
        if exercise["task"] == "addition":
            # Solve polynomial arithmetic addition exercise
            pass
        elif exercise["task"] == "subtraction":
            # Solve polynomial arithmetic subtraction exercise
            pass
        elif exercise["task"] == "multiplication":
            # Solve polynomial arithmetic multiplication exercise
            pass
        elif exercise["task"] == "long_division":
            # Solve polynomial arithmetic long divison exercise
            pass
        elif exercise["task"] == "extended_euclidean_algorithm":
            # Solve polynomial arithmetic EEA exercise
            pass
        elif exercise["task"] == "irreducibility_check":
            # Solve polynomial arithmetic irreducibility check exercise
            pass
        elif exercise["task"] == "irreducible_element_generation":
            # Solve polynomial arithmetic irreducible element generation exercise
            pass
    else: # exercise["type"] == "finite_field_arithmetic"
        # Check what task within the finite field arithmetic tasks we need to perform
        if exercise["task"] == "addition":
            # Solve finite field arithmetic addition exercise
            pass
        elif exercise["task"] == "subtraction":
            # Solve finite field arithmetic subtraction exercise
            pass
        elif exercise["task"] == "multiplication":
            # Solve finite field arithmetic multiplication exercise
            pass
        elif exercise["task"] == "division":
            # Solve finite field arithmetic division exercise
            pass
        elif exercise["task"] == "inversion":
            # Solve finite field arithmetic inversion exercise
            pass
        elif exercise["task"] == "primitivity_check":
            # Solve finite field arithmetic primitivity check exercise
            pass
        elif exercise["task"] == "primitive_element_generation":
            # Solve finite field arithmetic primitive element generation exercise
            pass


    # Open file at answer_location for writing, creating the file if it does not exist yet
    # (and overwriting it if it does already exist).
    with open(answer_location, "w") as answer_file:
        # Serialize Python answer data (stored in answer) to JSON answer data and write it to answer_file
        json.dump(answer, answer_file, indent=4)

# You can call your function from here
# Please do not *run* code outside this block
# You can however define other functions or constants
if __name__ == '__main__':
    solve_exercise('Simple/Exercises/exercise0.json', 'Simple/Answers/answer0.json')