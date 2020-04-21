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

Hash Functions

* Sum ascii values of a string 'abcd' (ex. ord(a) == 97)










