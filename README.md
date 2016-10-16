
### ReScience submission repository

This is the submission repository for the [Re**Science** journal](https://rescience.github.io).

### How to submit an article ?


1. Create a [github](https://github.com) account

2. [Fork](https://help.github.com/articles/fork-a-repo/) the [ReScience submission](https://github.com/ReScience/ReScience-submission) repository

3. Clone this new repository into your desktop environment

   ```
   $ git clone https://github.com/YOUR-USERNAME/ReScience-submission
   ```

4. Create a branch (the branch name should be author names separated with dashes)

   ```
   $ git checkout -b AUTHOR1-AUTHOR2
   ```


5. Add your code & article (see [author guidelines](https://rescience.github.io/write)) and commit your changes:

   ```
   $ git commit -a -m "Some comment"
   ```


6. [Push](https://help.github.com/articles/pushing-to-a-remote/) to github

   ```
   $ git push origin AUTHOR1-AUTHOR2
   ```

7. Issue a [pull request](https://help.github.com/articles/using-pull-requests/) (PR) to Re**Science** with title containing author(s) name and follow the template that will appear once you opened the pull request:

  ```
  **AUTHOR**

  Dear @ReScience/editors,

  I request a review for the following replication:

  ### Original article

  **Title:**  
  **Author(s):**  
  **Journal (or Conference):**  
  **Year:**  
  **DOI:**  
  **PDF:**   

  ### Replication

  **Author(s)**:   
  **Repository**:  
  **PDF**:  
  **Keywords**:  
  **Language**:  
  **Domain**:  

  ### Results

  * [ ] Article has been fully replicated
  * [ ] Article has been partially replicated
  * [ ] Article has not been replicated

  ### Potential reviewers
  <!-- If you know potential reviewers, you can tell us here -->
  <!-- You can look at http://rescience.github.io/board for the -->
  <!-- list of registered reviewers (but you can propose others) -->

  ---

  **EDITOR**

  * [ ] Editor acknowledgment
  * [ ] Reviewer 1 
  * [ ] Reviewer 2
  * [ ] Review 1 decision [accept/reject]
  * [ ] Review 2 decision [accept/reject]
  * [ ] Editor decision [accept/reject]
  ```

8. You can suggest reviewers from [editorial board](https://rescience.github.io/board).

9. Answer questions and requests made in the PR conversation page.
