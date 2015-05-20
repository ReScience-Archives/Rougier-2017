
### ReScience submission repository

This is the submission repository for the [Re**Science** journal](https://github.com/ReScience/ReScience/wiki).


### How to submit an article ?

1. Fork this repository

2. Clone this fork on your machine:

   ```
   $ git clone https://github.com/YOUR-USERNAME/ReScience-submission
   ```

3. Make your modifications (code & article) and commit them

   ```
   $ git commit -a -m "Some comment"
   ```

4. Push your modifications on github

   ```
   $ git push
   ```

5. Issue a pull request (PR) from the github interface and add a `Review:
   request` label on your PR

6. Read and reply any editor or reviewers comments and requests

7. You're done (accepted or rejected)


### How to submit several articles ?

If you intend to submit several articles, you'll need to create a dedicated
branch for each submission in your forked repository:

To create a local branch to work on your submission

   ```
   $ git checkout -b BRANCH-NAME
   ```

To push this branch on github

   ```
   $ git push origin --set-upstream origin BRANCH-NAME
   ```

You can then issue a pull request from this branch on the github interface
(just select the branch). If you want to submit another article, just create a
new branch from the master branch:

   ```
   $ git checkout master
   $ git checkout -b OTHER-BRANCH-NAME
   ```
