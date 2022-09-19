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

<details>
  <summary>9.6</summary>

  To represent a product, I would define a class that holds as attributes a list of categories and how many times it has been purchased. The data would be spread out across multiple machines based on the hash value of the product ID.

  Say that there are 10,000 categories and we want to list out up to 10,000 best-selling products. Each product ID would be up to 10B large, so the total storage space to store all the information for best-selling products across all the categories would be up to 1GB, which would be small enough to fit in one machine. To get the list of the best-selling products by category, we would just make use of the ID tables of best-selling products and fetch the real objects from the machine cluster based on the hash values.

  To keep the table up-to-date, we would occasionally have to update it like once an hour. To do that, we would ask each machine to list up to 10,000 best-selling products and then aggregate all the information across machines to get the final list of 10,000 best-setting products.
</details>

<details>
  <summary>9.7</summary>

  I have actually never used such a financial management system and am not going to use one anytime soon. If I was asked to create one, I would first try to use similar applications out there and find user reviews to figure out what it should be like. Below are what I think would be good from the viewpoint of one that has little to no knowledge about finance.

  I would offer the system in the form of a mobile application or a web application. I would have the backend system include the following at least.

  * Manual editing of expenditure as well as automatic transaction history from the bank account. We would need this because people would still use cash to buy or sell things, the exact usage of which would not be tracked automatically.
  * Statistics (mean, median, standard deviation, etc.) about the income, expenditure and investments would be shown. If there were a large enough number of users, those statistics would be also shown by category like income, age, sex, etc.
  * Prediction using a machine learning model. I'm not quite sure about how to build such a model and keep it up-to-date, but we could rely on some solutions on recent competitions in a website like [Kaggle](https://www.kaggle.com/). Since the data we have would be tabular for the most part, we would not need large space to store the model like we would when we use deep neural networks. However, we could also possibly leverage some recent high-performance language model to make potentially better predictions, if there were a mecanism for users to input their demands in text.
  * Email or app notifications of recommendations on a weekly or monthly basis based on predictions.
</details>

<details>
  <summary>9.8</summary>

  I would first build a web server to store those pieces of text and design a web interface for users to interact. When a user confirms text, the server would generate a file with a .html file that has a random or user-specified name to store the content of the text. The user could also easily specify how it would be displayed like using different sizes or colors, where the server would make use of CSS or Javascript.

  I would design the website in a way that users may or may not sign up. Whether the user is registered or not,
  we would need some mecanism to limit the amount of text one user could create since they could possibly send a large piece of text or a ton of requests. We would do that based on the IP address if the user had not signed up.

  For users that have accounts, we would at least provide the following features:

  * The whole list or directory tree of URLs with previews that they have created
  * Rename URLs as much as possible
  * Change the content of a URL with the editing history
  * Delete pages
  * Paste links to other pieces of text

  I would provides as many of those features as possible to those who don't have accounts as well because it might be awkward if they could never delete pages, for example. To do that, for those who don't have accounts and would possibly like to change the text or delete it, I would include a password authentication system.
</details>
