<details>
  <summary>11.1</summary>

  The code seems to be written in C or C++ and intended to print all the integers from 100 down to 0. However, after printing 0, it would never stop printing numbers since unsigned integers are always considered non-negative and 0 - 1 would return the largest unsigned integer.
</details>

<details>
  <summary>11.2</summary>

  One possible cause would be that the application makes some destructive changes to the environment. For example, if the app creates a temporary file and delete it later, the app might crash if the file was already there, but it will run without errors from next time since the file has been deleted. Another possible cause would be that the app used some random values to behave differently, where in the 10 debugging attempts happened to get around the crash. In any case I would just trace the error messages or find strings like "file" or "random" to find the cause of the crash.
</details>

<details>
  <summary>11.3</summary>

  I would first implement inside `Piece` a method `nextPositions` that lists all the possible positions the piece can move to. In Python, it would look something like the following.

  ```python
  def nextPositions(self, x, y):
      return [(x, y) for x in range(8) for y in range(8) if self.canMoveTo(x, y)]
  ```

  Once I have done this, I would quickly check the return values of `nextPositions()` of some pieces. We could do this either on a real chess board where other pieces sit or an imaginery board where only that pieces are put somewhere on the board. The latter case would be better for isolating `nextPositions()` but we would definitely have to test the method on the real board as well to see if it works under the presence of other pieces. Once this quick check has been done, I would write some exhaustive tests for sanity-check, such as seeing if all the elements of `nextPositions()` are on the chess board or they aren't on any piece of the player's piece.
</details>

<details>
  <summary>11.4</summary>

  I would first visit the website and load some pages following links from it. I might try different browsers to see if there's any difference, but since I have little knowledge about web, I would google how to test websites or simply ask friends how they would do that.
</details>

<details>
  <summary>11.5</summary>

  I would first hold the pen and try to write to see if it works decently. Next, I would think of the most fragile parts of the pen. Depending on the type of the pen, we could think of the following:

  1. If it's a with a cap, it's likely that the tip becomes too dry to write anything while there still remains some ink. We could remove the cap and leave it for a few days. Maybe we need longer days, in which case I would use a fan to put the pen under wind to shorten the process.
  2. It it's a click pen, it might break when it's clicked many times. I would test how many times it can be clicked by using some machine.
  3. If it's a mechanical pencil, its tip might break when it's dropped. I would test how tolerent the tip is by dropping it many times.

  We would need multiple pens for those tests. Also, there could be some unexpected use cases such as some people might want to modify it for penspinning, in which case we would need to make sure that the ink would not leak.
</details>

<details>
  <summary>11.6</summary>
  Most functionalities would have already been tested using a simluator, so tests on the real machine would be quick for the most part. One thing that's specific to the real situation is how much money is stored in the machine, which can be also simulated beforehand but needs some extra care. To test this, I would try to withdraw some money using a virtual account while deliverately making the amount of money in the ATM small. Or the opposite extreme could also happen, where the amount of money is too big too store, which could be tested similarly. Another core functionality of an ATM would be money transfer, but it would be easily tested using a simulator.
</details>
