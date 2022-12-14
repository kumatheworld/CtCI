<details>
  <summary>13.1</summary>

  Keeping a method private keeps subclasses from overriding or accessing it. If the constructor is private, subclasses are not able to instantiate an object by the constructor. This will be useful when one wants some restriction on instance creation like when the singleton design pattern is desirable.
</details>

<details>
  <summary>13.2</summary>

  Yes it does. For example, take a look at the following Java code.

  ```java
  class Exercise13_2 {
      public static void main(String[] args) {
          System.out.println(returnInsideTry());
      }

      private static String returnInsideTry() {
          try {
              System.out.println("try");
              return "tried";
          } catch (Exception e) {
              System.out.println("catch");
              return "catched";
          } finally {
              System.out.println("finally");
              return "finallied";
          }
      }
  }
  ```

  It prints the following, showing that the `finally` clause were executed right before the end of `try` and the value was return from `finally`.

  ```
  try
  finally
  finallied
  ```

</details>

<details>
  <summary>13.3</summary>

  `final` is an access modifier that keeps the class, field or method from being inherited. `finally` is a keyword that's used in `try-catch-finally` blocks, inside which the code is executed whether an exception was caught or not. `finalize` is a method of the `Object` class that's called before the deletion of the object.

  Since I was not familiar with `finalize`, I referred to the following website: <https://www.geeksforgeeks.org/finalize-method-in-java-and-how-to-override-it/>.
</details>

<details>
  <summary>13.4</summary>

  Both are meant to write classes or functions in a way that they can be instantiated with different types. Templates in C++ work like a macro and instantiated classes or functions of different types are compiled to different pieces of code. Generics in Java on the other hand, do type checking during compile time and are complied to one piece of code in which the type variables are substituted by `Object`, regardless of the actual types they are instantiated with.

  Since I was not familiar with generics in Java, I referred to the following websites.

* <https://www.geeksforgeeks.org/templates-in-c-vs-generics-in-java/>
* <https://stackoverflow.com/questions/36347/what-are-the-differences-between-generic-types-in-c-and-java>

</details>

<details>
  <summary>13.5</summary>

  All of them implements the `java.util.Map` interface. Here's a table that compares those 3.

  | Name          | Key order       | Lookup time complexity | Insertion time complexity | Implementation        |
  | ------------- | --------------- | ---------------------- | ------------------------- | --------------------- |
  | TreeMap       | Order in key    | Logarithmic            | Logarithmic               | Red-black tree        |
  | HashMap       | Arbitrary       | Constant               | Constant                  | Array of linked lists |
  | LinkedHashMap | Insertion order | Constant               | constant                  | Doubly-linked buckets |

  Some examples will be added later.

  Since I was not familiar with generics in Java, I referred to the following website: <https://www.geeksforgeeks.org/differences-treemap-hashmap-linkedhashmap-java/>
</details>
