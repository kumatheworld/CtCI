<details>
  <summary>12.3</summary>

  According to the [reference](https://en.cppreference.com/w/cpp/container/map), STL maps are usually implemented as red-black trees, where keys are sorted and search, removal, and insertion operations have logarithmic complexity. Hash tables on the other hand perform those operations in constant time on average and in linear time in the worst cases. Since a hash table is basically 2-dimensional, it can be implemented as a double pointer to pairs (key, value). Additionally, the size of the table or the number of elements can be tracked as members of a `struct` that has the double pointer in it.

  If the the number of inputs is small, we could use a `std::vector` of tuples instead of a hash table, where the lookup can be done by `std::find_if()`, but if we don't care about the performance too much, we can just use `std::map`.
</details>

<details>
  <summary>12.4</summary>

  A virtual function is a method in a class definition declared with the keyword `virtual`, which can be overridden by subclasses during runtime unlike those without it.

  As I am not familiar with C++, I had to refer to the following [website](https://www.geeksforgeeks.org/virtual-functions-and-runtime-polymorphism-in-cpp/).
</details>

<details>
  <summary>12.5</summary>

  Deep copy is a means to copy an object by recursively replicating all the members and the objects they may refer to, while shallow copy only copies the members. They are different when the object has a dynamically allocated member. It is generally recommended to use deep copy in such a situation to avoid object members being changed by a shallowly copied object. However, we could still use shallow copy like when we train a neural network like a [Siamese network](https://en.wikipedia.org/wiki/Siamese_neural_network), where we would like to share the referenced dynamic object.
</details>

<details>
  <summary>12.6</summary>

  `volatile` is a type qualifier that tells the compiler not to do any optimization about the variable that could possibly change the behavior of the program. Specifically, without the declaration, the compiler might assume that the variable would never change though it could due to another thread accessing it or simply being a global variable that could be modified somewhere else, for example. Adding the `volatile` qualifier can prevent those potentially unexpected situations.

  Here I list some websites as references since I was not so familiar with C/C++. Good examples can be found there.

* <https://en.wikipedia.org/wiki/Volatile_(computer_programming)>
* <https://www.geeksforgeeks.org/understanding-volatile-qualifier-in-c/>
* <https://stackoverflow.com/questions/246127/why-is-volatile-needed-in-c>

</details>

<details>
  <summary>12.7</summary>

  This is because failing to make the destructor `virtual` could lead to an undefined behavior. Specifically, suppose a class `Base` has defined a destructor without `virtual` and another class `Derived` inherits `Base`. When we have a `Base` pointer that actually refers to a `Derived` object and tries to delete it through the pointer, the behavior of the deletion process is undefined. If we have defined the destructor of `Base` as a virtual function, the deletion process will call the destructors of `Derived` and `Base` in this order.

  Here I list some websites as references since I was not so familiar with C/C++. Good examples can be found there.

* <https://www.geeksforgeeks.org/virtual-destructor/>
* <https://stackoverflow.com/questions/461203/when-to-use-virtual-destructors>

</details>
