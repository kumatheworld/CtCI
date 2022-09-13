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
