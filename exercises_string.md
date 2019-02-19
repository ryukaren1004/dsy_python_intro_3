<b><Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.</b>

<b>Exercise 2: Given that fruit is a string, what does fruit[:] mean? </b>

<b>Exercise 3: Encapsulate below code in a function named count, and generalize it so that it accepts the string and the letter as arguments.</b>

    word = 'banana'
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    print(count)

<b>Exercise 4: There is a string method called count that is similar to the function in the previous exercise. Read the documentation of this method at:

[https://docs.python.org/library/stdtypes.html#string-methods](https://docs.python.org/library/stdtypes.html#string-methods)

Write an invocation that counts the number of times the letter a occurs in "banana".**</b>

<b>Exercise 5: Take the following Python code that stores a string:

str = 'X-DSPAM-Confidence:0.8475'

Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.</b>

<b>Exercise 6: Read the documentation of the string methods at [https://docs.python.org/library/stdtypes.html#string-methods](https://docs.python.org/library/stdtypes.html#string-methods) You might want to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful.

The documentation uses a syntax that might be confusing. For example, in find(sub[, start[, end]]), the brackets indicate optional arguments. So sub is required, but start is optional, and if you include start, then end is optional.


