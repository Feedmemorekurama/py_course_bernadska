#Convert number to reversed array of digits
#Convert number to reversed array of digits
#Given a random number:
#C#: long;
#C++: unsigned long;
#You have to return the digits of this number within an array in reverse order.
#Test.assert_equals(digitize(35231),[1,3,2,5,3])

def digitize(n):
     return [int(s) for s in str(n)][::-1]