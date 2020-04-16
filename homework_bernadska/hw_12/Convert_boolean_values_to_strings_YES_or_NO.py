#Convert boolean values to strings 'Yes' or 'No'.
#Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
#Test.assert_equals(bool_to_word(True), 'Yes')
#Test.assert_equals(bool_to_word(False), 'No')

def bool_to_word(boolean):    
   return 'Yes' if boolean==True else 'No'