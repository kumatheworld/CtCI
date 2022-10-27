<details>
  <summary>11.1</summary>

  The code seems to be written in C or C++ and intended to print all the integers from 100 down to 0. However, after printing 0, it would never stop printing numbers since unsigned integers are always considered non-negative and 0 - 1 would return the largest unsigned integer.
</details>

<details>
  <summary>11.2</summary>

  One possible cause would be that the application makes some destructive changes to the environment. For example, if the app creates a temporary file and delete it later, the app might crash if the file was already there, but it will run without errors from next time since the file has been deleted. Another possible cause would be that the app used some random values to behave differently, where in the 10 debugging attempts happened to get around the crash. In any case I would just trace the error messages or find strings like "file" or "random" to find the cause of the crash.
</details>
