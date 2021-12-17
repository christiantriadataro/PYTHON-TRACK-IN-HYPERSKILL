#### Theory: Search in a string

One of the essential skills when working with data is to
be able to search it and locate specific bits of information.
Working with textual data in Python, you may need to get
some information about its content: whether it includes a
specific **substring** (i.e. part of the string), where this
substring is, or how many times it occurs in the text. In
this topic, we will learn how to do it.

#### 1. A substring searching algorithm
We'll start with a substring searching problem. Given two
strings, __text__ and __pattern__, we need to identify whether
there is at least one occurrence of the __pattern__ in the text.
The simplest and most natural way to solve this problem
is to sequentially consider all substrings of the text
whose length is equal to the length of the __pattern__ and 
compare them with the pattern itself. If at least in one
case all corresponding symbols match, the __pattern__ is 
found. If none of such attempts were successful, we
should indicate that there is no __pattern__ in the text. Here's
how this simple algorithm can be implemented in Python:

def contains(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        found = True
        
        for j in range(len(pattern):
            if text
