Disclaimer: At this time, I have little to no experience about this topic during work, so my answers here will be far from being satisfactory.:confounded:

<details>
  <summary>9.1</summary>

  I'd store the data in the form of some Python object like a dictionary, design APIs, create a GitHub repository and host it using [PyPI](https://pypi.org/). If there's any other server that I'm supposed to use (e.g. one that belongs to my company), I'd just use it. If not, since this is a small service that only up to 1,000 clients use, I'd first try to host it on my own [GitHub Pages](https://kumatheworld.github.io/). If it doesn't work out, I'd consider using a cloud hosting service or designing a server on my own using [Raspberry Pi](https://www.raspberrypi.org/).
</details>

<details>
  <summary>9.2</summary>
  I'd use a hash table to represent the social network, where a user's ID is mapped to their friends' IDs. Since there could be billions of people and millions of connections per person, I'd have to divide up the table to multiple machines. I'd do so in a way that inter-machine connections would be minimized, where I'd rearrange the hash table occasionally. I'm not quite sure how to achieve that but one heuristic way would be to assign each key to a machine that the key has many values in while making sure that the keys are not located in a biased way.

  Now, to find the shortest path between two people, I would just do the breadth-first search across machines starting from one of the 2 people. During the process, all the machines that have at least one related person (i.e. one that's been discovered in the search) would share all the people that have been discovered, and each related person would keep track of the path from the source person. The algorithm would stop once we have found the other one of the 2 people. We could speed up the algorithm by starting the search from both of the 2 people.
</details>

<details>
  <summary>9.3</summary>
  I would use the breadth-first search algorithm to collect URLs. One way to avoid infinite loops would be to restrict the searching time or the number of (potentially duplicate) websites. We could easily remove the duplicates once the algorithm has stopped. Another way would be to use a container like a list or a heap to hold the already-visited websites to avoid visiting the same websites. This approach would be better if the search got into an infinite loop in the early stage, but I don't think it would be very likely. Even if it is, by setting the time limit to the first approach, we could actually collect many URLs by running the algorithm multiple times.
</details>

<details>
  <summary>9.4</summary>

  I would first sort the URLs and then compare 2 adjecent URLs from the beginning to the end. Of course, we could possibly find duplicate URLs during the sorting process, in which case we could stop the algorithm right away if we were supposed to find just one pair of duplicate URLs.

  We now consider how much storage space we would need. If the average URL length is $l$ (i.e. we need $l$ bytes for one URL), the total space we need to store the entire array of URLs would be roughly $10l$ GB. If $l=100$, we'd roughly need 1TB of space, which would be small enough to fit into one machine. An in-place sorting algorithm like the quick sort would work just fine with little to no extra space if we're allowed to change the order of the URLs.

  If not, or we have no space to store the URLs in one machine, we could perform sorting in each machine and then use the merge sort algorithm to sort the entire array of URLs in linear time. After sorting, the duplication check would be done in each machine for the most part. If there were no duplicates, we would need to check the last URL in one machine corresponds to the first URL in the next, which could also be easily done.
</details>

<details>
  <summary>9.5</summary>

  I would have all the 100 machines hold the same hash table to cache search results. The hash table would also hold keep the time the given query was most recently accessed the so it would work as an LRU cache. Now, we call the cache $C$ and suppose that a client has given a query $q$. We consider the following 3 situations.

  1. $q$ was not found in $C$

      In this case, the client would be added to a new empty queue $Q_q$ and the hash table would be updated with a pair $(q, \mathrm{None})$, where $\mathrm{None}$ is a dummy value.

  2. $q$ was found in $C$ with the value $\mathrm{None}$ (i.e. the query was being processed)

      In this case, the client would be added to $Q_q$ and wait. Once the process is done, the hash table would be updated with the return value of `processSearch(q)`, which would be broadcasted to the clients in $Q_q$. The queue would be cleared after the broadcast.

  3. $q$ was found in $C$ with the value not $\mathrm{None}$ (i.e. the query had already been processed and the result remains in $C$)

      In this case, the value would be immediately returned to the client. Meanwhile, `processSearch(q)` would run occasionally (i.e. at least once in a predefined time interval) to make sure that the cache stays up-to-date. Once the process is done, the cache would be updated with the new return value.
</details>
