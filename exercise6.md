<details>
  <summary>6.1</summary>
  Label the bottles from #1 to #20. Take i pills from each i-th bottle and we get 1 + 2 + ... + 20 = 231 pills in total. Measure the total weight w (grams) of those pills on the scale. Then ((w - 231) / 0.1)-th bottle is the one that has heavier pills.
</details>

<details>
  <summary>6.2</summary>
  We want to choose the easier one. It is the one with the higher probability. The probability that we win each of the games is p and p^3 + 3(1-p)p^2, respectively. Therefore, we should choose Game 1 if and only if p >= p^3 + 3(1-p)p^2, solving which we get 0 <= p <= 1/2.
</details>

<details>
  <summary>6.3</summary>
  No we can't. A domino covers exactly one black square wherever it is put, but if we cut off the corner, there will remain either 30 or 32 black squares, in neither of which cases we can put the 31 dominos.
</details>

<details>
  <summary>6.4</summary>
  In the general settings, out of 2^n equally likely possibilities of the ants' directions, there are only 2 with which no collision occurs. Namely, those are the cases where all the ants go in the same direction. Therefore, the probability of any collision is 1 - 1 / 2^(n-1). If n = 3, it is 1 - 1/4 = 3/4.
</details>

<details>
  <summary>6.5</summary>
  Below is a procedure to make four quarts of water. Each step has a sketch of the states of the 2 jugs, where '+' indicates that the jug has that many quarts of water in it.

  0. The jugs are empty
  ```
    -----
    ---
  ```
  1. Fill the 5-quart jug
  ```
    +++++
    ---
  ```
  2. Fill the 3-quart jug with the water in the 5-quart jug
  ```
    ++---
    +++
  ```
  3. Throw away the water in the 3-quart jug
  ```
    ++---
    ---
  ```
  4. Move the water in the 5-quart jug to the 3-quart jug
  ```
    -----
    ++-
  ```
  5. Fill the 5-quart jug
  ```
    +++++
    ++-
  ```
  6. Fill the 3-quart jug with the water in the 5-quart jug and we get four quarts in the 5-quart jug
  ```
    ++++-
    +++
  ```
</details>
