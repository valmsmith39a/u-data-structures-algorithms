* Using a data structure that uses a hash function
+ Biggest benefit is the ability to do *constant time lookups*
+ Lookups in *constant time * O(1) time
+ Lookups using lists, sets, arrays are in linear time O(n)
- Need to look through every element to find what you're looking for
- Stacks/Queues enable lookup of oldest/newest elements in constant time but not other elementsk

Hash functions
* value => hash function => hash value (aka hash code) which can be used as index of an array
* Can go to array and get your value in constant time because
an array lookup with an index happens in constant time

Collisions:
* when a function outputs the same hash value for 2 different inputs
* Fix a collision
+ Change hash value
+ Change hash function
+ Change the structure of array
- Can store all the values hashed at the hash code in a list (aka "buckets")
- Instead of storing one value at each hash code, you can store a collection in each bucket.

Hash functions have a constant time in the average lookup case.
But the bucket system, may store every value in 1 bucket, then would be in linear time O(n) 

* Hash functions run-time:
+ Average case: constant time O(1)
+ Worst case: linear time O(n)
+ Hash function tradeoffs
+ 1) spread out your values well vs using a lot of space
+ 2) fewer buckets vs more elements to search in each bucket
- Ideally have 1 - 3 elements stored in each bucketk
- Can use a 2nd hash function within the bucket to split up the elements even more (Works well for few really large buckets)
+ Need to know the upsides/downsides to the approach you use 

Hash Maps
* key => hash function => hash code => store key, value pair in the bucket at the hash vode 

For interviews:
Create a Hash Table
Know the upsides/downsides of your hash function

Simple Hash Function
* Sum ascii values of a string 'abcd' (ex. ord(a) == 97)

Hash Map:
* We need to store key/value pairs
* We can use 2 arrays, linked-lists, stacks, queues: but would have O(n) run-times
because need to traverse the data structure to find the key
* For an array, to find an element at an index (ex a[5]) takes constant O(1) time.
* We can think of the indexes as keys
* So for keys that are non-zero integers, we can use an array
* Now we need a function that can produce integer keys from any input

Hash Functions
* Hash functions enable use to create integer keys (indexes for our array) from any input
* Hash functions can map data of any size to date of fixed size (hash code)
* Ex. input a string key into hash function to output an integer value
* Map data to an integer value

Popular Hash Function

a * p^(n) + b * p^(n-1) + c * p^(n-2)... 

ascii * prime number (31, 37)^(n)
n -> 0

* We store the hash codes in a "bucket array". Each entry is called a "bucket".
Index of each "bucket" is a "bucket index"

***

Time Complexity

Primary component is the linked list traversal because length of the string is very small compared to the number of entries so we can disregard it.

O (n/b)
n key/value pairs
b buckeets

n/b <= 0.7 (load factor)















