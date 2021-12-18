## Theory: String hashing

String hashing is a technique that allows us to represent
a string as a number. A rule used to associate a string
with a number is called a **hash function**, and the resulting
number is called a **hash value** (or simply a **hash**):

![](https://ucarecdn.com/c785ca27-8634-46b5-be73-460fb08905bc/)

An important advantage of string hashing is that it makes
it possible to compare two strings in O(1) since we 
simply need to compare the strings' hash values. This
property is used to efficiently solve some substring
processing problems.

Usually, a hash for a string is calculated as follows: each
symbol of the string is associated with a number, then a 
hash value is computed as a sum of these numbers with
some coefficients. There are several ways to associate a 
symbol with a number. In this topic, we will use the 
following rule: **__A__** corresponds to **__1__**, **__B__** corresponds to
**__2__**, ..., **__Z__** corresponds to **__26__**. That is, each symbol is
associated with its order number in the alphabet. As for
string hashing functions, there are a few of them as well.
Our next step is to learn some of them and understand 
their pros and cons.

#### 1. Linear hashing
For a string **s = s<sub>0</sub>s<sub>1</sub> ... s<sub>n-1</sub>, a linear hash function **__h<sub>L</sub>__** is
defined as a sum of the symbols' associated values:

**__h<sub>L</sub>(s) = s[0] + s[1] + ... + s[n-1]

For example, a hash value for **s = ABAC** is 

**__h<sub>L</sub>(ABAC) = 1 + 2 + 1 + 3 + 7.

This is one of the simplest hash functions for strings. A
disadvantage of the linear hash function is that a hash
value does not depend on the order of symbols. This
means that if we reorder the symbols of a string, the hash
value for the string won't change. For example, strings
**s<sub>1</sub> = ABAC** and **s<sub>2</sub> = CBAA** are not equal, but they
consist of the same symbols and thus have equal hash
values:

h<sub>L</sub>(ABAC) = 1 + 2 + 1 + 3 = 7, 
h<sub>7</sub>(CBAA) = 3 + 2 + 1 + 1 = 7

A situation when two different strings have equal hash
values is called a **collision**. An important property of any
hash function is how many strings it maps to the same
hash value. The less the number of such strings, the 
better the hash function. At this point, linear hashing is
not the best choice since the limitation described above
results in many collisions.

#### 2. Polynomial hashing
For a string **s = s[0] s[1] ... s[n-1]>, a polynomial hash function
is defined as follows:
h<sub>p</sub>(s) = (s[0] ⋅ a<sup>0</sup> + s[1] ⋅ a<sup>1</sup> + ... + s[n-1] ⋅ a<sup>n-1</sup>) mod m

Here, **__a__** is a constant, usually a prime number
approximately equal to the total number of different
symbols in the alphabet; **__m__** is a constant as well, usually
a big prime number. Let's consider how we can calculate
the polynomial hash for **s = ACDC**. For simplicity, we
will use **a = 3** and **m = 11**.

h<sub>p</sub> (ACDC) = (1 ⋅ 3<sup>0</sup> + 3 ⋅ 3<sup>1</sup> + 4 ⋅ 3<sup>2</sup> + 3 ⋅ 3<sup>3</sup>) mod 11
h<sub>p</sup> (ACDC) = (1 ⋅ 1 + 3 ⋅ 3 + 4 ⋅ 9 + 3 ⋅ 27) mod all
                     = 2 + 9 + 36 + 81 mod 11 = 127 mod 11 = 6

Although the polynomial hash depends on the order of 
symbols in a string, collisions are still possible. For
example, **s<sub>1</sub> = BBAB** and **s<sub>2</sub> = ABCC** are different
strings with equal hash values:

h<sub>p</sub> (BBAB) = (2 ⋅ 3<sup>0</sup> + 2 ⋅ 3<sup>1</sup> + 2 ⋅ 3<sup>3</sup>) mod 11 = 71 mod 11 = 5,
h<sub>p</sub> (ABCC) = (1 ⋅ 3<sup>0</sup> + 3 ⋅ 3<sup>1</sup> + 3 ⋅ 3<sup>3</sup>) mod 11 = 115 mod 11 = 5,

However, the probability of a collision for the polynomial
hash function is ≈ 1/m, which is quite low for a big **__m__**.
Thus, the polynomial hash function is a good choice for
string hashing.

#### 3. Rolling hashing
This section describes not a distinct function, but rather a 
property of hash functions that is applicable to both
linear and polynomial hashing.

Consider a string **s = ABBCCB**. Let's use the linear 
hash function to calculate a hash for a prefix of **s** of 
length **4**:

**__h<sub>4</sub>(ABBC) = s[0] + s[1] + s[2]+ s[3] = 1 + 2 + 2 + 3 = 8__**.

Now, assume we need to calculate a hash value for the
next substring of **__s__** of length 4. This can be done as
follows:

**__h<sub>L</sub>(BBCC) = s[1] + s[2] + s[3] + s[4] = 2 + 2 + 3 + 3 = 10.

Note that the second sum can also be obtained if we
subtract s[0] from the first sum and then add s[4]:
                                                     first sum s[0] s[4]  
h<sub>L</sub> (BBCC) = h<sub>L</sub>(ABBC) - s[0] + s[4] = 8 - 1 + 3 = 10.

Thus, if we know a hash value h<sub>L</sub> (s[i] s[i]+1 ... s[j]), a hash
value for the next substring can be calculated in **__O(1)__** as
follows:

h<sub>L</sub> (s[i+1] + s[i+2] ... s[j+1]) = h<sub>L</sub>(s[i]+s[i+1] ... s[j]) - s[i] + s[j+1].

This property of a hash function is called a **rolling hash**.
the same property holds to the polynomial hash function:
the only difference is that we need to start the 
calculations with the last substring of **s**:

h<sub>p</sub>(BCCB) = (s[2] ⋅ 3<sup>0</sup> + s[3] ⋅ 3<sup>1</sup> + s[4] ⋅ 3<sup>2</sup> + s[5] ⋅ 3<sup>3</sup>) mod 11
                    = (2 ⋅ 1 + 3 ⋅ 3 + 3 ⋅ 9 + 2 ⋅ 27) mod 11
                    = 92 mod 11 = 4.

The next substring of **s** from the end has the following
has value:

h<sub>p</sub>(BBCC) = (s[1] ⋅ 3<sup>0</sup> + s[2] ⋅ 3<sup>1</sup> + s[3] ⋅ 3<sup>2</sup> + s[4] ⋅ 3<sup>3</sup>) mod 11
                    = (2 ⋅ 1 + 2 ⋅ 3 + 3 ⋅ 9 + 3 ⋅ 27) mod 11
                    = 116 mod 11 = 6

Using the hash value for the first substring, the second
one can be obtained as follows:

h<sub>p</sup> (BBCC) = ((h<sub>p</sup>(BCCB) - s[5] ⋅ 3^3) ⋅ 3 + s[1]) mod 11
                     = ((4 - 2 ⋅ 27) ⋅ 3 + 2) mod 11
                     = -148 mod 11 = 6

So, if we know the hash value h<sub>p</sub>(s[i+1] s[i+2] ... s[j]), a hash
value for a neighboring substring can be calculated as
follows:

h<sub>p</sub>(s[i]s[i+1]...s[j-1]) = ((h<sub>p</sub>(s[i+1]s[i+2]...s[j]) - s[j] ⋅ a<sup>j-i-1) ⋅ a + s[i]) mod m.

The rolling hash property allows us to efficiently solve
some substring processing problems. A good example is a 
**Rabin-Karp algorithm**, which is based on string hashing. It
allows us to find a substring in linear time, which is faster
than the naive approach. We will consider this algorithm
in more detail in the next topic.

#### 4. Summary
String hashing is a way to represent a string as a number.
It is useful for some string processing algorithms since
hash values can be compared in O(1). There are several
ways to hash a string, linear and polynomial hashing
being among them. The latter is a better choice for string
hashing since it has fewer collisions. Both hash functions
are rolling hashes. That is, if we know the hash value for 
some substring, a hash value for a neighboring substring
can be calculated in O(1).

