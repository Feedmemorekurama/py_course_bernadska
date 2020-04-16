#Write function isPalindrome that checks if a given string (case insensitive) is a palindrome.
#In Racket, the function is called palindrome?

#@test.describe('sample tests')
#def sample_tests():
    #test.assert_equals(is_palindrome('a'), True)
    #test.assert_equals(is_palindrome('aba'), True)
    #test.assert_equals(is_palindrome('Abba'), True)
    #test.assert_equals(is_palindrome('malam'), True)
    #test.assert_equals(is_palindrome('walter'), False)
    #test.assert_equals(is_palindrome('kodok'), True)
    #test.assert_equals(is_palindrome('Kasue'), False)


def is_palindrome(string,):
    return string[::-1].lower().replace(" ","") == string.lower().replace(" ","")