print("Hello to my calculator")
first_number = int(input("please input the first number"))
operation = input("please type .sum for addition or .sub for subtraction or .multiply for multiplication or "
                  ".div for divide")
second_number = int(input("please input the second number"))
if operation == ".sum":
    final_result = first_number + second_number
    print("the result from your addition is " + str(final_result))
elif operation == ".sub":
    final_result = first_number - second_number
    print("the result from your subtraction is " + str(final_result))
elif operation == ".multiply":
    final_result = first_number * second_number
    print("the result from your multiplication is " + str(final_result))
elif operation == ".div":
    final_result = first_number / second_number
    print("the result from your dividing is " + str(final_result))
else:
    raise ValueError("you have given me invalid information, please start over")