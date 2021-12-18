## Theory: Rabin-Karp algorithm
For a pattern __p__ and a text __t__, the simplest substring
searching algorithm performs a symbol-by-symbol
comparison of the pattern with each substring of the text,
which results in __O(|p| ⋅ |t|)__ running time. If you work with large text and 
performance is crucial, this might be too slow. To find a 
substring faster, we need to use more efficient
approaches than the naive direct comparison.

One of the algorithms that help search a substring faster
is the **Rabin-Karp algorithm**. It uses string hashing for a
faster comparison thus significantly reducing the total
running time compared with the naive approach.

#### 1. Algorithm description
The main idea of the Rabin-Karp algorithm is to use **string
hashing** and compare strings' **hash values** instead of a 
direct comparison. To compute the substrings' hash
values fast, the algorithm uses the polynomial hash
functions and their rolling hash property. In more detail,
the algorithm can be formulated as follows:

