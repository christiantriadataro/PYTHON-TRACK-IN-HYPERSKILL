## Theory: String basics

#### 1. What is a string?

# A string is one of these words that shift their meaning
# depending on the context: it can refer to the charming
# sounds of a harp or describe the structure of the universe.
# In computer programming, a string is simply an ordered
# sequence of symbols. We begin the indexation from 0, i.e.
# given the string s, its first symbol is s[0], the second is
# s[1], and so on until the last symbol. The length of the
# string s is the total number of characters it contains. We
# denote it by |s|. Examples:

#   - 100101 - a string of length 6;
#   - GATTACA - a string of length 7.

# A string can have zero length. In this case, it is called an
# empty string.

# One can perform numerous operations on strings. Let's
# mention briefly a couple of them:

# - reverse(s) - it returns the reversed string, i.e. the
#   string written backward. For example,
#   reverse(LIVE) = EVIL.
# - concat(s,t) - concatenates the given strings s
#   and t. For instance, concat(STR, INGS) =
#   STRINGS.

# Pretty often one may have to compare two given strings.
# This is done by scanning and comparing each element of
# the first string with the corresponding element of the
# same index in the other string. More precisely, given the
# string s and t, we check for every i whether s[i] = t[i].
# If they all match, then we conclude that s = t.

#### 2. Substrings
# A substrings is a contiguous subsequence of symbols of an
# original string. For instance, ATTA is a substring of the
# string GATTACA because the string GATTACA contains the
# sequence ATTA. Naturally, a substring is called proper if
# does not coincide with the whole string.

        # Note: Any strign is a nonproper substring of itself.
        # An empty string is a substring of any string.

# A substring of the string s starting from the i-th and
# ending with the j-th symbol is denoted by s[i, j].
# Example: for s = GATTACA, s[1, 4] = ATTA.

# A substring starting from the index 0 is a prefix, and a
# substring ending with the last index is a suffix. A proper
# substring that is a prefix and a suffix at the same time is
# called border of the string. Sometimes, the word prefix-
# suffix is used instead. For example, s[0,2] = GAT is a
# prefix of s, and s[4,6] = ACA  is a suffix of s. On the other
# hand, w[0,0] = A is a border of the string w = ATTA.

#### 3. Strings applications
# Strings are one of the most used data structures in
# programming. In almost any field, there are problems
# requiring knowledge of string-processing algorithms.
# Consider a few typical string processing algorithms and
# problems.

# - String-searching algorithms. Let's say we are
#   developing a text editor and want to add a function
#   you've ever tried finding a specific word in a wall of
#   text, you know the ordeal. To solve this problem, we
#   need to implement an algorithm that finds all
#   occurrences of a given pattern in a string.

# - Similarity measure. Suppose that we are developing
#   a search engine. We want to correct users' spelling
#   mistakes to process their requests better (recall
#   googling something in a rush: it feels gorgeous
#   when a search engine understands you anyway).
#   After getting a word with a typo, we may find the
#   most similar word in our dictionary and use it
#   instead of the initial one. To do that, we need to
#   implement a measure of similarity between two
#   strings.


#### 4. Why study string algorithms?

# Usually, programming languages provide some standard
# string methods. But some of the more complex problems
# require you to develop and implement the solution
# manually.
# It's often easy to come up with a simple solution to a
# particular problem, but a naive algorithm probably won't
# be efficient in terms of running time and memory
# consumption. More efficient algorithms are often less
# obvious.
# For these reasons, it's essential to be familiar with some
# standard and well-known string processing algorithms
# and their applications. We will examine some of them in
# the next topics.
