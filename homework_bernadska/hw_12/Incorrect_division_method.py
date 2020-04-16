#Incorrect division method
#This method, which is supposed to return the result of dividing its first argument by its second, isn't always returning correct values. Fix it.
#test.describe("Basic tests")
#test.assert_equals(divide_numbers(4, 2), 2)
#test.assert_equals(divide_numbers(10, 2), 5)
#test.assert_equals(divide_numbers(9, 4), 2.25)
#test.assert_equals(divide_numbers(21, 5), 4.2)
#test.assert_equals(divide_numbers(9, 3), 3)
#test.assert_equals(divide_numbers(1, 100), 0.01)

def divide_numbers(x,y):
    return float (x) / (y)