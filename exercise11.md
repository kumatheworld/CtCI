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
