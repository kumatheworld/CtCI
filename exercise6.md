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

<details>
  <summary>6.6</summary>
  Skipped for now.
</details>

<details>
  <summary>6.7</summary>
  The probability that a family ends up having n boys before giving birth to a girl is 1/2<sup>n+1</sup>. Thus the expected number of boys a family gets is Σ<sub>n=0</sub><sup>∞</sup>n/2<sup>n+1</sup>=1. Therefore, the sex ratio will be roughly 1:1.

  [exercise6_7.py](exercise6_7.py) simulates this.
</details>

<details>
  <summary>6.8</summary>
  We can find N in 14 steps with the following strategy. We drop the first egg from the 14, 27, 39, 50, 60, 69, 77, 84, 90, 95, 99-th floors in this order until it breaks. If it does not, that means we have found N=100 in 11 steps. If it does, we go back to the previous floor where the egg did not break and start to drop the second egg from the next floor, increasing the level one by one. For example, if the first egg breaks at the 77th floor, we start to drop the second egg from the 70th floor. If it breaks at the 75th floor, that means we have found N=75 in 13 steps, having tried 14, 27, 39, 50, 60, 69, 77, 70, 71, 72, 73, 74, 75-th floors.

  Now we prove that this is an optimal strategy. Suppose that there is a way to find N in 13 steps. The first floor we drop an egg from should be no higher than the 13th floor because if it breaks, we would need to start dropping the second egg from the 1st floor, increasing the level one by one (if not, we might fail to find N), which takes more than 13 steps. Therefore, the first floor to drop the egg should be 13th. The next floor should be 25th for a similar reason. We cannot go higher because the second egg should be dropped from the 14th floor if the first egg breaks. Thus the optimal strategy is to drop the first egg from the 13, 25, 36, 46, 55, 63, 70, 76, 81, 85, 88, 90, 91-th floors, in which case we would need more than 13 steps if N>91. Thus there is no strategy that can always find N in less than 13 steps.
</details>
