## Theory: The big O notation

Suppose you need to choose one of several algorithms to
solve a problem. How can you pick the best one? To do it,
you need to measure the algorithm efficiency somehow.

One of the options might be to measure the time your
program needs to process its input. However, different
computers may take different time to process the same
data. Furthermore, the processing time may depend on
the data itself. We obviously need something more
universal. So, let's try to estimate the efficiency using **big
O notation.**

#### 1. Input size
What does an algorithm usually do? It makes some
calculations. Let's call **operations** the basic actions, such
as addition, multiplication, comparison, variable
assignment, etc. Of course, the calculation time depends
on the machine, but it doesn't matter now because we
want to compare algorithms, not machines. Now let's try
to estimate the number of operations in an algorithm!

![](https://ucarecdn.com/f4233b0c-4d4e-498e-84ae-772c9ed09c39/)

Buses aren't always punctual, are they? One day it may
happen that they are there on time, while the other day
they will take a lifetime to arrive. You can't blame solely
the driver for that: the time of the trip depends directly on
the number of passengers on the bus. The more
passengers, the more stops, the longer the time to arrive.
Likewise, the running time of an algorithm depends on
the **input data**. Naturally, the program will take a different
time to proceed with 10 or 1 000 000 numbers. We will
use the term **input size** as a proxy measure of the size of 
input data. If you need to work with **m** numbers, then **m** is
the input size. The input size isn't always the amount of 
the input data itself. If you need to find the first __n__ prime
numbers, then searching for 10 first primes or 10 000 __first
primes__ will also take a different time, however, you only
enter a single number **n** as input. In such cases, that
number's value is typically considered the input size.

If we can estimate how the number of operations depends
on the input size, we will have a machine-independent
measure of algorithm complexity. This is exactly what we
need! Also, if we want to find a good algorithm, we are
mostly interested in its behavior with big data. For this,
we can compare the behavior of the algorithm's running
time with some standard functions.

#### 2. Big O notation
As we already mentioned, we will use the **big O notation**
to measure the efficiency of algorithms. As a matter of 
fact, we have borrowed this symbol from mathematics;
however, we shall not worry about the mathematical
meaning or definition of the big O. Less formally, we can
say that an algorithm has the **time complexity** __O(f(n)))__ if 
its number of operations grows bigger similar to (or
slower than) the function __f(n)__ when the input size n is a 
large number. In order to avoid unnecessary abstractness,
let's consider the following task: given a n x n table with
integers in its cells. Find the number k in the given table.

![](https://ucarecdn.com/e619ff5f-8741-42a5-bf9d-c6abc51a613d/)

Alice and Bob have come up with their own algorithms to solve the 
problem. Bob's algorithm consists in scanning 
every cell of the table and checking if the corresponding
value is equal to k. Well, this implies a maximum of n<sup>2</sup>
comparisons, which means that the time complexity of 
Bob's algorithm is __O(n<sup>2</sup>)__. On the other hand, Alice
somehow knows earlier in which column the number k
will be located, hence, she only needs to scan the 
elements of that column. A column consists of n cells,
meaning that Alice's algorithm will take O(n) time.

Basically, on a table 2 x 2, Bob will have to perform a 
maximum of 4 operations; meanwhile, Alice will perform
no more than 2. Not a big difference really, is it? What if 
we have a table n x n for a large n? In this case, n<sup>2</sup> will
be considerably bigger than n, as shown below. This is 
exactly what determines the efficiency of an algorithm - 
the way it behaves with large input sizes. Hence, we
conclude that Alice's algorithm is faster than Bob's as the 
big O notation suggests.

However, a simple question arises: why can't we write
simply n<sup>2</sup> or n for the complexities? Why do we need to
add this beautiful round letter in front of these functions?
Well, imagine that the element __k__ is place in the first cell
of the table. Bob will find it immediately and terminate his
algorithm. How many steps does he perform: n<sup>2</sup>? No, just
one.

![](https://ucarecdn.com/57ac2090-8c2c-4bb9-94df-948b068ab3c7/)

That is why use the big O: roughly speaking, it
describes the upper bound for the function's growth rate.
This is one of the big O notation's essential advantages. It
means that you can calculate how much time to allocate
for processing a certain amount of input data and be sure
that the algorithm will process it all in due time. In
practice, an algorithm might sometimes work even better
than what the big O notation shows for its complexity, but
not worse.

#### 3. Common growth rates
Below are, from best to worse, some common values of 
the big O function for the time complexity, also known as
complexity classes.
- __O(1)__(**constant time**). The algorithm performs a
  constant number of operations. Maybe one, two,
  twenty-size, or two hundred - it doesn't matter. What 
  is important is that is doesn't depend on the input
  size. Typical algorithms of this class include
  calculating the answer using a direct formula,
  printing a coupe of values, all letters of the English
  alphabet, etc.
- __O(log n)__ (**logarithmic time**). Perhaps a quick
  reminder on logarithms is necessary. We usually
  refer to logarithms of base 2; however, the base
  does not affect the class. By definition, __**log<sub>2</sub>n**__
  equals the number of times n must be divided by 2
  to get 1. That being said, it should not be difficult to 
  guess that such algorithms divide the input size into
  **halves** at each step. They are relatively fast: if the 
  size of the input is huge, say 2<sup>31</sup> (programmers
  should know the importance of this number), the
  algorithms will perform approximately log(<sub>2</sub>)(2<sup>31</sup>) = 
  31 operations, which is pretty effective.
- __O(n)__ (**linear time). The time is proportional to the 
  input size, i.e., the time grows linearly as the input
  size increases. Often, such algorithms are iterated
  only once. They occur quite frequently, because it is 
  usually necessary to go through every input
  element before calculating the final answer. This
  makes the __O(n)__ class one of the most effective
  classes in practice.
- __O(n<sup>2</sup>)__ (**quadratic time**). Normally, such algorithms
  go through all pairs of input elements. Why? Well,
  mathematics is generous, it constantly provides us
  with important results: in this case, basic maths
  confirms that the number of unordered pairs in a set
  of **n** elements is equal to n(n - 1) / 2, which, as we will
  learn later in this topic, is __O(n<sub>2</sub>)__. If you find it scary
  or difficult to understand, it is completely normal,it
  happens to the best of us. On the other hand, for
  those who are familiar with programming terms, the 
  following sentence might come in handy: quadratic
  time algorithms usually contain two nested loops.
- __O(2<sub>n</sub>)__ (**exponential time**). Just in case, let's
  mention that __2<sub>n</sub>__ is the same as multiplying __2__ by
  itself n times. Again, math states that the number
  of subsets of a set of n elements is equal to __2<sub>n</sub>__,
  therefore, it is reasonable to expect that such
  algorithms scan all the subsets of the input
  elements. It is worth noting that this class is 
  extremely inefficient in practice; even for small
  input sizes, the time taken by the algorithms will be
  remarkably high.

There are also other less common complexity classes,
which you will come across in some following topics:
- __O(√n)__ (**square root time);
- __O(n log n)__ (**log-linear time**);
- __O(n<sub>k</sub>)__ (**polynomial time**);
- __O(n!)__ (**factorial time**).

Now let's gather all the classes together and sort them
from the best to the worst, so that you remember which
ones are the most effective, and which ones you should
stay away from.

![](https://ucarecdn.com/a59bc4ff-df5e-460b-9e58-27e88e9ae228/)

#### 4. Calculating complexity
Let's look at a simple example. You want to find the
maximum of __n__ numbers. You will probably decide to go
through them and compare every new element with the 
maximum so far. You will make __n__ comparisons, so the
time complexity is __O(n)__.

However, algorithms are usually quite complex and 
consist of several steps, whose time complexity may
belong to different time complexity classes from the list
above. Therefore, to be able to calculate complexities by
yourself, it is essential for you to get familiar with the
basic properties of the Big O;

- **Ignore the constants**. As we discussed above, while
  calculating complexities, we focus solely on the 
  behavior of our algorithm with large input sizes.
  Therefore, repeating some steps a constant number
  of times does not affect the complexity. For
  example, if you traverse __n__ elements __5__ times, we say
  that the algorithm's time complexity is __O(n)__, and
  not __O(5n)__. Indeed, there is no significant difference
  between 1 000 000 000 and 5 000 000 000
  operations performed by the algorithm. In either
  case, we conclude that it is relatively slow. Formally,
  we write __c ⋅ O(n) = O(n)__. It is similar for the rest
  of the complexity classes.

- **Smaller terms do not matter**. Another common case
  is when after doing some actions, you need to do
  something else. For instance, you traverse __n__
  elements __n__ times and then traverse __n__ elements
  again. In this case, the complexity is still _O(n<sup>2</sup>).
  Additional __n__ actions do not affect your complexity,
  which is proportional to __n<sup>2</sup>. In big O notation, it
  looks like this: __O(n) + O(n<sup>2</sup>) = O(n<sup>2</sup>)__. All in all,
  always keep the largest term in Big O and forget
  about all others. It is rather easy to understand
  which terms are larger based on the order provided
  in the previous section. Naturally, a question arises:
  why is it correct to ignore the smaller terms? Let's 
  illustrate the example above:

![](https://ucarecdn.com/27c7e5ef-eb2d-48ca-8a56-e5423589515a/)

The images show that when the input size __n__ is large, the
graphs of __n<sup>2</sup>__ and __n<sup>2</sup> + n__ almost coincide (their growth
rate is similar). As for __n<sup>2</sup>__, for large __n__ this value is
considerably greater than __n__, therefore adding __n__ to it does
not affect the value of the function much. This is why we
can rightfully write __O(n<sup>2</sup>)__ instead of __O(n<sup>2</sup> + n)__.

#### 5. Conclusion
Big O notation is an essential instrument for algorithm
performance evaluation. We can use it to access both the
time and the memory complexity. The greatest advantage
of big O notation is that it classifies an algorithm rather
than gives you a real running time in seconds or required
memory in megabytes.

We should note that it is completely normal if you still
find the concept of Big O a bit confusing. It is similar to
reading the rules of a board game for the first time
without actually having the board in front of you. As soon
as you start playing, you wil better realize the meaning of
those rules. Analogously, in the following topics on
algorithms, we will describe in detail how to calculate
algorithm complexity. That will definitely lead to a better
understanding of this topic as well. In a nutshell, we hope
this topic hasn't demotivated you, on the contrary, you
should be motivated and hungrier for more.

