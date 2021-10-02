# Theory: Basics of sets

# 1. What is a set?
# Suppose we have a collection of numbers: 1,2,3,4,5, or a
# group of letters: a,b,c,d,e. In math, we call this group a set.
# So, simply put, it's a collection of distinct elements. For
# instance, a set of learners of programming, a set of learners of
# math, a set of books on the shelf, a set of people in the cafe, etc.
# We use curly brackets {} to denote a set.

# A finite set is a set that has a finite number of elements and an
# infinite set is a set that is not a finite set. For example,
#                   {1,2,3,4,5}

# − it is a finite set of integers from 1 to 5. We list each element
# separated by a comma, then put curly brackets around the
# whole thing. Another example:
#                   {1,2,3,4,5,...}

# - it is an infinite set of natural numbers. The three dots are
# called an ellipsis. That means this set continues for infinity. But
# sometimes we use the "..." in the middle to save writing long
# lists:

#                   {1,2,3,...,18,19,20}.

# In this case, the set is finite (there are only 20 integers).

# Usually, we denote a set by capital letters and an element in
# that set by lowercase letters: A = {a,b,c,...} - in this
# example A is a set, and a is n element in A.

# There are several ways we can define a set. For example, if
# B = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, we could write this as
#   B = {x: 1 ⩽ x ⩽ 10 where x is an integer}

# It reads like this: "B equals to the set of x such that x is greater
# or equal to 1, but less or equal to 10 where x is an integer".

# 2. Members of a set
# Objects in the set are called members or elements of a set. For
# example, 2 is an element of the set {1,2,3}, footbal is an
# element of the set {tennis, football, hockey}. Te symbol ∈
# shows that the element belongs to the given set, and not ∈ shows
# that the element does not belong to the set. For example,
#       JavaScript not ∈ {Python, C++, R}

# The number of members of a finite set A is written as |A|. It is
# called a cardinality of a set. Therefore the cardinality of the set
# {-1,1} is equal to 2.

# Another type of set you are going to meet is an empty set. This
# is a set that has no members. An empty set is written as ∅ or {}
# . The cardinality of an empty set is equal to 0. Thus, ∣∅∣ = 0. It is
# important to note that {0} is not empty! It is a set with an
# element 0 in it and |{0}| = 1.

# 3. Subsets
# If we take pieces of the set, we can form a subset. A is subset
# of B if and only if every element of A is in B. For example, the
# {1,3} is a subset of {1,2,3,4}, but the {2,9} is not a subset
# of this set since it has an element 9 which is not in the set
# {1,2,3,4}. If B is a subset of A, we denote that by B ⊆ A or
# A ⊇ B, We denote by A not ⊆ B if A is not a subset of B.

# Note that an empty set is a subset of any set, including the
# empty set itself, and a set is always considered a subset of
# itself.

# 4. Proper subsets
# A is a proper subset of B if and only if every element in A is
# also an element of B, and there exist at least one element in
# B that is not in A. We denote it by A ⊂ B or B ⊃ A.

# For example, {Ruby, Scala} is a subset of {Ruby,Scala},
# but it is not a proper subset of {Ruby,Scala}.

# {a1,a2,a7} is a proper subset of {a0,a1,a2,a3,a5,a7,a9}.


# 5. Equality
# Two sets are equal if they have exactly the same numbers. For
# example, A = {2,4,6} and B = {6,2,4} are equal. They
# both contain exactly the elements 2,4, and 6. Also, two sets A
# and B are equal if A ⊆ B and B ⊆ A.

# The set is uniquely determined by its elements and does not
# depend on the order of recording of these elements. For
# instance, a set of three elements a, b, and c can be written in six
# different ways:
# {a,b,c} = {a,c,b} = {b,a,c} = {c,b,a} = {c,a,b} = {b,c,a}

# In sets, it does not matter what order the members are in. Also,
# we should remember that all the elements are distinct. In some
# programming languages, where the concept of a set is
# implemented, we can add new elements to a set. But if we want
# to insert the same element into a set again, the set will not
# change. For instance, if we take the set {1,2,3} and try to
# insert into this set the numbers 2,2,3,3,3,4, we obtain just
# {1,2,3,4} - with no duplicated 2s or 3s.

# if sets A and B are equal, we write A = b.

#       The set theory is fundamental to all of mathematics. The
#       set theory is closely connected with the symbolic logic,
#       and these fields are becoming more and more relevant in
#       programming, in artificial intelligence and
#       communications security.