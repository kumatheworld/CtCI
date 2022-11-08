<details>
  <summary>12.3</summary>

  According to the [reference](https://en.cppreference.com/w/cpp/container/map), STL maps are usually implemented as red-black trees, where keys are sorted and search, removal, and insertion operations have logarithmic complexity. Hash tables on the other hand perform those operations in constant time on average and in linear time in the worst cases. Since a hash table is basically 2-dimensional, it can be implemented as a double pointer to pairs (key, value). Additionally, the size of the table or the number of elements can be tracked as members of a `struct` that has the double pointer.
</details>
