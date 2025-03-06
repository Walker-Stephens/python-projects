# Instructions:  For each problem, fill in the function body with
#                your code.  To test your code, run the file.  An
#                AssertionError means that your code failed a test.
#                To receive any credit, your code must handle any
#                reasonable test case without being altered.  To
#                receive any credit, you must only use only the
#                material we have covered in class.  Do not use
#                material we have not yet covered.
#
#                DO NOT ALTER FUNCTION HEADERS OR TESTS! 

# Problem 1
# Modify and return the given dictionary as follows: if the key "a"
# has a value, set the key "b" to have that value, and set the key "a"
# to have the value "".
#
# prob_one({"a": "candy", "b": "dirt"}) → {"a": "", "b": "candy"}
# prob_one({"a": "candy"}) → {"a": "", "b": "candy"}
# prob_one({"a": "candy", "b": "carrot", "c": "meh"}) → {"a": "", "b": "candy", "c": "meh"}

def prob_one(dictionary):
    # Problem 1 code goes here:
    if 'a' in dictionary:
        dictionary['b'] = dictionary['a']
        dictionary['a'] = ''
       
    return dictionary

# Problem 2
# Modify and return the given dictionary as follows: if the key "a" has a
# value, set the key "b" to have that same value. In all cases remove the key
# "c", leaving the rest of the dictionary unchanged.
#
# problem_two({"a": "aaa", "b": "bbb", "c": "ccc"}) → {"a": "aaa", "b": "aaa"}
# problem_two({"b": "xyz", "c": "ccc"}) → {"b": "xyz"}
# problem_two({"a": "aaa", "c": "meh", "d": "hi"}) → {"a": "aaa", "b": "aaa", "d": "hi"}

def problem_two(dictionary):
    # Problem 2 code goes here:
    if 'a' in dictionary:
        dictionary['b'] = dictionary['a']
    del dictionary['c']
    
    return dictionary

# Problem 3
#
# Modify and return the given dictionary as follows: for this problem the dictionary
# may or may not contain the "a" and "b" keys. If both keys are present, append their
# 2 string values together and store the result under the key "ab".
#
# problem_three({"a": "Hi", "b": "There"}) → {"a": "Hi", "ab": "HiThere", "b": "There"}
# problem_three({"a": "Hi"}) → {"a": "Hi"}
# problem_three({"b": "There"}) → {"b": "There"}

def problem_three(dictionary):
    # Problem 3 code goes here:
    if 'a' in dictionary and 'b' in dictionary:
        dictionary['ab'] = dictionary['a'] + dictionary['b']
    return dictionary

# Problem 4
#
# Given a dictionary of food keys and topping values, modify and return
# the dictionary as follows: if the key "ice cream" is present, set its
# value to "cherry". In all cases, set the key "bread" to have the value
# "butter".
#
#
# problem_four({"ice cream": "peanuts"}) → {"bread": "butter", "ice cream": "cherry"}
# problem_four({}) → {"bread": "butter"}
# problem_four({"pancake": "syrup"}) → {"bread": "butter", "pancake": "syrup"}

def problem_four(dictionary):
    # Problem 4 code goes here:
    if 'ice cream' in dictionary:
        dictionary['ice cream'] = 'cherry'
    dictionary['bread'] = 'butter'
    
    return dictionary

# Problem 5
#
# Given a dictionary of food keys and their topping values, modify and return
# the dictionary as follows: if the key "ice cream" has a value, set that as the
# value for the key "yogurt" also. If the key "spinach" has a value, change that
# value to "nuts".
#
# problem_five({"ice cream": "cherry"}) → {"yogurt": "cherry", "ice cream": "cherry"}
# problem_five({"spinach": "dirt", "ice cream": "cherry"}) → {"yogurt": "cherry", "spinach": "nuts", "ice cream": "cherry"}
# problem_five({"yogurt": "salt"}) → {"yogurt": "salt"}

def problem_five(dictionary):
    # Problem 5 code goes here:
    if 'ice cream' in dictionary:
        dictionary['yogurt'] = dictionary['ice cream']
    if 'spinach' in dictionary:
        dictionary['spinach'] = 'nuts'
    
    return dictionary

# Problem 6
# Given a dictionary of food keys and topping values, modify and return the dictionary
# as follows: if the key "potato" has a value, set that as the value for the key "fries".
# If the key "salad" has a value, set that as the value for the key "spinach".
#
# problem_six({"potato": "ketchup"}) → {"potato": "ketchup", "fries": "ketchup"}
# problem_six({"potato": "butter"}) → {"potato": "butter", "fries": "butter"}
# problem_six({"salad": "oil", "potato": "ketchup"}) → {"spinach": "oil", "salad": "oil", "potato": "ketchup", "fries": "ketchup"}

def problem_six(dictionary):
    # Problem 6 code goes here:
    if 'potato' in dictionary:
        dictionary['fries'] = dictionary['potato']
    if 'salad' in dictionary:
        dictionary['spinach'] = dictionary['salad']
    
    return dictionary

# Problem 7
# Modify and return the given dictionary as follows: if the keys "a" and "b" are both in
# the dictionary and have equal values, remove them both.
#
# problem_seven({"a": "aaa", "b": "aaa", "c": "cake"}) → {"c": "cake"}
# problem_seven({"a": "aaa", "b": "bbb"}) → {"a": "aaa", "b": "bbb"}
# problem_seven({"a": "aaa", "b": "bbb", "c": "aaa"}) → {"a": "aaa", "b": "bbb", "c": "aaa"}

def problem_seven(dictionary):
    # Problem 7 code goes here:
    if 'a' in dictionary and 'b' in dictionary and dictionary['a'] == dictionary['b']:
        del dictionary['a']
        del dictionary['b']
    
    return dictionary

# Problem 8
# 
# Modify and return the given dictionary as follows: if exactly one of the keys "a" or
# "b" has a value in the dictionary (but not both), set the other to have that same value
# in the dictionary.
#
# problem_eight({"a": "aaa", "c": "cake"}) → {"a": "aaa", "b": "aaa", "c": "cake"}
# problem_eight({"b": "bbb", "c": "cake"}) → {"a": "bbb", "b": "bbb", "c": "cake"}
# problem_eight({"a": "aaa", "b": "bbb", "c": "cake"}) → {"a": "aaa", "b": "bbb", "c": "cake"}

def problem_eight(dictionary):
    # Problem 8 code goes here:
    if 'a' in dictionary and 'b' not in dictionary:
        dictionary['b'] = dictionary['a']
    if 'a' not in dictionary and 'b' in dictionary:
        dictionary['a'] = dictionary['b']
        
    
    return dictionary

# Problem 9
# Modify and return the given dictionary as follows: if the keys "a" and "b" have values that
# have different lengths, then set "c" to have the longer value. If the values exist and have
# the same length, change them both to the empty string in the dictionary.
#
# problem_nine({"a": "aaa", "b": "bb", "c": "cake"}) → {"a": "aaa", "b": "bb", "c": "aaa"}
# problem_nine({"a": "aa", "b": "bbb", "c": "cake"}) → {"a": "aa", "b": "bbb", "c": "bbb"}
# problem_nine({"a": "aa", "b": "bbb"}) → {"a": "aa", "b": "bbb", "c": "bbb"}

def problem_nine(dictionary):
    # Problem 9 code goes here:
    if 'a' in dictionary and 'b' in dictionary  and len(dictionary['a']) != len(dictionary['b']):
        if len(dictionary['a']) > len(dictionary['b']):
            dictionary['c'] = dictionary['a']
        else:
            dictionary['c'] = dictionary['b']
    if 'a' in dictionary and 'b' in dictionary  and len(dictionary['a']) == len(dictionary['b']):
        dictionary['a'] = ''
        dictionary['b'] = ''
    
    return dictionary

# Problem 10
#
# Given a list of strings, return a dictionary containing a key for every
# different string in the list, always with the value 0. For example the string "hello" makes
# the pair "hello":0.
#
# problem_ten(["a", "b", "a", "b"]) → {"a": 0, "b": 0}
# problem_ten(["a", "b", "a", "c", "b"]) → {"a": 0, "b": 0, "c": 0}
# problem_ten(["c", "b", "a"]) → {"a": 0, "b": 0, "c": 0}

def problem_ten(string_list):
    # Problem 10 code goes here:
    dictionary = {}
    for i in string_list:
        dictionary[i] = 0
    
    return dictionary

# Problem 11
#
# Given a list of strings, return a dictionary containing a key for every different
# string in the list, and the value is that string's length.
#
# problem_eleven(["a", "bb", "a", "bb"]) → {"bb": 2, "a": 1}
# problem_eleven(["this", "and", "that", "and"]) → {"that": 4, "and": 3, "this": 4}
# problem_eleven(["code", "code", "code", "bug"]) → {"code": 4, "bug": 3}

def problem_eleven(string_list):
    # Problem 11 code goes here:
    dictionary = {}
    for i in string_list:
        dictionary[i] = len(i)
    
    return dictionary

# Problem 12
#
# Given a list of non-empty strings, create and return a dictionary as follows: for
# each string add its first character as a key with its last character as the value.
#
# problem_twelve(["code", "bug"]) → {"b": "g", "c": "e"}
# problem_twelve(["man", "moon", "main"]) → {"m": "n"}
# problem_twelve(["man", "moon", "good", "night"]) → {"g": "d", "m": "n", "n": "t"}

def problem_twelve(string_list):
    # Problem 12 code goes here:
    dictionary = {}
    for i in string_list:
        a = i[0]
        b = i[len(i) - 1]
        dictionary[a] = b
    
    return dictionary

# Problem 13
#
# Given a list of strings, return a dictionary with a key for each different string,
# with the value the number of times that string appears in the list.
#
# problem_thirteen(["a", "b", "a", "c", "b"]) → {"a": 2, "b": 2, "c": 1}
# problem_thirteen(["c", "b", "a"]) → {"a": 1, "b": 1, "c": 1}
# problem_thirteen(["c", "c", "c", "c"]) → {"c": 4}

def problem_thirteen(string_list):
    # Problem 13 code goes here:
    dictionary = {}
    for i in string_list:
        if i in dictionary:
            dictionary[i] = dictionary[i] + 1
        else:
            dictionary[i] = 1
    
    return dictionary

# Problem 14
#
# Given a list of non-empty strings, return a dictionary with a key for every different
# first character seen, with the value of all the strings starting with that character
# appended together in the order they appear in the list.
#
# problem_fourteen(["salt", "tea", "soda", "toast"]) → {"s": "saltsoda", "t": "teatoast"}
# problem_fourteen(["aa", "bb", "cc", "aAA", "cCC", "d"]) → {"a": "aaaAA", "b": "bb", "c": "cccCC", "d": "d"}
# problem_fourteen([]) → {}

def problem_fourteen(strings):
   # Problem 14 code goes here:
   dictionary = {}
   for i in strings:
       if i[0] not in dictionary:
           dictionary[i[0]] = i
       else:
            dictionary[i[0]] = dictionary[i[0]] + i
   
   return dictionary

# Problem 15
#
# Loop over the given list of strings to build a result string like this: when a string
# appears the 2nd, 4th, 6th, etc. time in the list, append the string to the result. Return
# the empty string if no string appears a 2nd time.
#
# problem_fifteen(["a", "b", "a"]) → "a"
# problem_fifteen(["a", "b", "a", "c", "a", "d", "a"]) → "aa"
# problem_fifteen(["a", "", "a"]) → "a"

def problem_fifteen(string_list):
    # Problem 15 code goes here:
    a_string = ''
    count = {}
    for i in string_list:
        if i not in count:
            count[i] = 1
        else:
            count[i] = count[i] + 1
            if count[i] % 2 == 0:
                a_string = a_string + i
    return a_string

# Problem 16
#
# Given a list of strings, return a dictionary where each different string is a key and its
# value is true if that string appears 2 or more times in the list.
#
# problem_sixteen(["a", "b", "a", "c", "b"]) → {"a": true, "b": true, "c": false}
# problem_sixteen(["c", "b", "a"]) → {"a": false, "b": false, "c": false}
# problem_sixteen(["c", "c", "c", "c"]) → {"c": true}

def problem_sixteen(string_list):
    # Problem 16 code goes here:
    dictionary = {}
    for i in string_list:
        if i not in dictionary:
            dictionary[i] = 1
        else: dictionary[i] = dictionary[i] + 1
    for i in dictionary:
        if dictionary[i] > 1:
            dictionary[i] = True
        else:
            dictionary[i] = False
            
    
    return dictionary


# Test Cases. DO NOT ALTER!
assert prob_one({"a": "candy", "b": "dirt"}) == {"a": "", "b": "candy"}
assert prob_one({"a": "candy"}) == {"a": "", "b": "candy"}
assert prob_one({"a": "candy", "b": "carrot", "c": "meh"}) == {"a": "", "b": "candy", "c": "meh"}
assert prob_one({"b": "carrot"}) == {"b": "carrot"}
assert prob_one({"c": "meh"}) == {"c": "meh"}
assert prob_one({"a": "sparkle", "c": "meh"}) == {"a": "", "b": "sparkle", "c": "meh"}

assert problem_two({"a": "aaa", "b": "bbb", "c": "ccc"}) == {"a": "aaa", "b": "aaa"}
assert problem_two({"b": "xyz", "c": "ccc"}) == {"b": "xyz"}
assert problem_two({"a": "aaa", "c": "meh", "d": "hi"}) == {"a": "aaa", "b": "aaa", "d": "hi"}
assert problem_two({"a": "xyz", "b": "1234", "c": "yo", "z": "zzz"}) == {"a": "xyz", "b": "xyz", "z": "zzz"}
assert problem_two({"a": "xyz", "b": "1234", "c": "yo", "d": "ddd", "e": "everything"}) == {"a": "xyz", "b": "xyz", "d": "ddd", "e": "everything"}

assert problem_three({"a": "Hi", "b": "There"}) == {"a": "Hi", "ab": "HiThere", "b": "There"}
assert problem_three({"a": "Hi"}) == {"a": "Hi"}
assert problem_three({"b": "There"}) == {"b": "There"}
assert problem_three({"c": "meh"}) == {"c": "meh"}
assert problem_three({"a": "aaa", "ab": "nope", "b": "bbb", "c": "ccc"}) == {"a": "aaa", "ab": "aaabbb", "b": "bbb", "c": "ccc"}
assert problem_three({"ab": "nope", "b": "bbb", "c": "ccc"}) == {"ab": "nope", "b": "bbb", "c": "ccc"}

assert problem_four({"ice cream": "peanuts"}) == {"bread": "butter", "ice cream": "cherry"}
assert problem_four({}) == {"bread": "butter"}
assert problem_four({"pancake": "syrup"}) == {"bread": "butter", "pancake": "syrup"}
assert problem_four({"bread": "dirt", "ice cream": "strawberries"}) == {"bread": "butter", "ice cream": "cherry"}
assert problem_four({"bread": "jam", "ice cream": "strawberries", "salad": "oil"}) == {"bread": "butter", "ice cream": "cherry", "salad": "oil"}

assert problem_five({"ice cream": "cherry"}) == {"yogurt": "cherry", "ice cream": "cherry"}
assert problem_five({"spinach": "dirt", "ice cream": "cherry"}) == {"yogurt": "cherry", "spinach": "nuts", "ice cream": "cherry"}
assert problem_five({"yogurt": "salt"}) == {"yogurt": "salt"}
assert problem_five({"yogurt": "salt", "bread": "butter"}) == {"yogurt": "salt", "bread": "butter"}
assert problem_five({}) == {}
assert problem_five({"ice cream": "air", "salad": "oil"}) == {"yogurt": "air", "ice cream": "air", "salad": "oil"}

assert problem_six({"potato": "ketchup"}) == {"potato": "ketchup", "fries": "ketchup"}
assert problem_six({"potato": "butter"}) == {"potato": "butter", "fries": "butter"}
assert problem_six({"salad": "oil", "potato": "ketchup"}) == {"spinach": "oil", "salad": "oil", "potato": "ketchup", "fries": "ketchup"}
assert problem_six({"toast": "butter", "salad": "oil", "potato": "ketchup"}) == {"toast": "butter", "spinach": "oil", "salad": "oil", "potato": "ketchup", "fries": "ketchup"}
assert problem_six({}) == {}
assert problem_six({"salad": "pepper", "fries": "salt"}) == {"spinach": "pepper", "salad": "pepper", "fries": "salt"}

assert problem_seven({"a": "aaa", "b": "aaa", "c": "cake"}) == {"c": "cake"}
assert problem_seven({"a": "aaa", "b": "bbb"}) == {"a": "aaa", "b": "bbb"}
assert problem_seven({"a": "aaa", "b": "bbb", "c": "aaa"}) == {"a": "aaa", "b": "bbb", "c": "aaa"}
assert problem_seven({"a": "aaa"}) == {"a": "aaa"}
assert problem_seven({"b": "bbb"}) == {"b": "bbb"}
assert problem_seven({"a": "", "b": "", "c": "ccc"}) == {"c": "ccc"}
assert problem_seven({}) == {}
assert problem_seven({"a": "a", "b": "b", "z": "zebra"}) == {"a": "a", "b": "b", "z": "zebra"}

assert problem_eight({"a": "aaa", "c": "cake"}) == {"a": "aaa", "b": "aaa", "c": "cake"}
assert problem_eight({"b": "bbb", "c": "cake"}) == {"a": "bbb", "b": "bbb", "c": "cake"}
assert problem_eight({"a": "aaa", "b": "bbb", "c": "cake"}) == {"a": "aaa", "b": "bbb", "c": "cake"}
assert problem_eight({"ccc": "ccc"}) == {"ccc": "ccc"}
assert problem_eight({"c": "a", "d": "b"}) == {"c": "a", "d": "b"}
assert problem_eight({}) == {}
assert problem_eight({"a": ""}) == {"a": "", "b": ""}
assert problem_eight({"b": ""}) == {"a": "", "b": ""}
assert problem_eight({"a": "", "b": ""}) == {"a": "", "b": ""}
assert problem_eight({"aa": "aa", "a": "apple", "z": "zzz"}) == {"aa": "aa", "a": "apple", "b": "apple", "z": "zzz"}

assert problem_nine({"a": "aaa", "b": "bb", "c": "cake"}) == {"a": "aaa", "b": "bb", "c": "aaa"}
assert problem_nine({"a": "aa", "b": "bbb", "c": "cake"}) == {"a": "aa", "b": "bbb", "c": "bbb"}
assert problem_nine({"a": "aa", "b": "bbb"}) == {"a": "aa", "b": "bbb", "c": "bbb"}
assert problem_nine({"a": "aaa"}) == {"a": "aaa"}
assert problem_nine({"b": "bbb"}) == {"b": "bbb"}
assert problem_nine({"a": "aaa", "b": "bbb", "c": "cake"}) == {"a": "", "b": "", "c": "cake"}
assert problem_nine({"a": "a", "b": "b", "c": "cake"}) == {"a": "", "b": "", "c": "cake"}
assert problem_nine({"a": "", "b": "b", "c": "cake"}) == {"a": "", "b": "b", "c": "b"}
assert problem_nine({"a": "a", "b": "", "c": "cake"}) == {"a": "a", "b": "", "c": "a"}
assert problem_nine({"c": "cat", "d": "dog"}) == {"c": "cat", "d": "dog"}
assert problem_nine({"ccc": "ccc"}) == {"ccc": "ccc"}
assert problem_nine({"c": "a", "d": "b"}) == {"c": "a", "d": "b"}
assert problem_nine({}) == {}
assert problem_nine({"a": "", "z": "z"}) == {"a": "", "z": "z"}
assert problem_nine({"b": "", "z": "z"}) == {"b": "", "z": "z"}

assert problem_ten(["a", "b", "a", "b"]) == {"a": 0, "b": 0}
assert problem_ten(["a", "b", "a", "c", "b"]) == {"a": 0, "b": 0, "c": 0}
assert problem_ten(["c", "b", "a"]) == {"a": 0, "b": 0, "c": 0}
assert problem_ten(["c", "c", "c", "c"]) == {"c": 0}
assert problem_ten([]) == {}

assert problem_eleven(["a", "bb", "a", "bb"]) == {"bb": 2, "a": 1}
assert problem_eleven(["this", "and", "that", "and"]) == {"that": 4, "and": 3, "this": 4}
assert problem_eleven(["code", "code", "code", "bug"]) == {"code": 4, "bug": 3}
assert problem_eleven([]) == {}
assert problem_eleven(["z"]) == {"z": 1}

assert problem_twelve(["code", "bug"]) == {"b": "g", "c": "e"}
assert problem_twelve(["man", "moon", "main"]) == {"m": "n"}
assert problem_twelve(["man", "moon", "good", "night"]) == {"g": "d", "m": "n", "n": "t"}
assert problem_twelve([]) == {}
assert problem_twelve(["a", "b"]) == {"a": "a", "b": "b"}
assert problem_twelve(["are", "codes", "and", "cods"]) == {"a": "d", "c": "s"}
assert problem_twelve(["apple", "banana", "tea", "coffee"]) == {"a": "e", "b": "a", "c": "e", "t": "a"}

assert problem_thirteen(["a", "b", "a", "c", "b"]) == {"a": 2, "b": 2, "c": 1}
assert problem_thirteen(["c", "b", "a"]) == {"a": 1, "b": 1, "c": 1}
assert problem_thirteen(["c", "c", "c", "c"]) == {"c": 4}
assert problem_thirteen([]) == {}
assert problem_thirteen(["this", "and", "this", ""]) == {"": 1, "and": 1, "this": 2}
assert problem_thirteen(["x", "y", "x", "Y", "X"]) == {"x": 2, "X": 1, "y": 1, "Y": 1}
assert problem_thirteen(["123", "0", "123", "1"]) == {"0": 1, "1": 1, "123": 2}
assert problem_thirteen(["d", "a", "e", "d", "a", "d", "b", "b", "z", "a", "a", "b", "z", "x", "b", "f", "x", "two", "b", "one", "two"]) == {"a": 4, "b": 5, "d": 3, "e": 1, "f": 1, "one": 1, "x": 2, "z": 2, "two": 2}
assert problem_thirteen(["apple", "banana", "apple", "apple", "tea", "coffee", "banana"]) == {"banana": 2, "apple": 3, "tea": 1, "coffee": 1}

assert problem_fourteen(["salt", "tea", "soda", "toast"]) == {"s": "saltsoda", "t": "teatoast"}
assert problem_fourteen(["aa", "bb", "cc", "aAA", "cCC", "d"]) == {"a": "aaaAA", "b": "bb", "c": "cccCC", "d": "d"}
assert problem_fourteen([]) == {}
assert problem_fourteen(["apple", "bells", "salt", "aardvark", "bells", "sun", "zen", "bells"]) == {"a": "appleaardvark", "b": "bellsbellsbells", "s": "saltsun", "z": "zen"}

assert problem_fifteen(["a", "b", "a"]) == "a"
assert problem_fifteen(["a", "b", "a", "c", "a", "d", "a"]) == "aa"
assert problem_fifteen(["a", "", "a"]) == "a"
assert problem_fifteen([]) == ""
assert problem_fifteen(["a", "b", "b", "a", "a"]) == "ba"
assert problem_fifteen(["a", "b", "b", "b", "a", "c", "a", "a"]) == "baa"
assert problem_fifteen(["a", "b", "b", "b", "a", "c", "a", "a", "a", "b", "a"]) == "baaba"
assert problem_fifteen(["a", "b", "b", "b", "a", "c", "a", "a", "a", "b", "a"]) == "baaba"
assert problem_fifteen(["a", "b", "c"]) == ""
assert problem_fifteen(["this", "or", "that", "and", "this", "and", "that"]) == "thisandthat"
assert problem_fifteen(["xx", "xx", "yy", "xx", "zz", "yy", "zz", "xx"]) == "xxyyzzxx"

assert problem_sixteen(["a", "b", "a", "c", "b"]) == {"a": True, "b": True, "c": False}
assert problem_sixteen(["c", "b", "a"]) == {"a": False, "b": False, "c": False}
assert problem_sixteen(["c", "c", "c", "c"]) == {"c": True}
assert problem_sixteen([]) == {}
assert problem_sixteen(["this", "and", "this"]) == {"and": False, "this": True}
assert problem_sixteen(["d", "a", "e", "d", "a", "d", "b", "b", "z", "a", "a", "b", "z", "x"]) == {"a": True, "b": True, "d": True, "e": False, "x": False, "z": True}