# Changelogs Generator
Hey! This Package is a [changelogs-cli](https://pypi.org/project/changelogs-cli/)  package that creates automatic changelogs that supports [Conventional Commits.](https://www.conventionalcommits.org/en/v1.0.0/)
Since we use Bitbucket, we needed something like this and I wanted to share it publicly in case you need it too.

# Emoji Support
If comments comply with conventional commit rules, they are supported with emoji.

```json
[
    "feat": "โ",
    "fix": "๐",
    "build": "๐",
    "chore": "๐",
    "docs": "๐",
    "style": "๐จ",
    "refactor": "๐ท",
    "perf": "โก๏ธ",
    "test": "๐งช",
    "merge": "๐",
    "revert": "โช๏ธ"
]  
````
 
# Installing

    pip install changelogs-cli

# Example

First, let's get into the current your repository. 

Example;
    ```cd /home/repository/```

Example usage is as follows.
    changelogs ```example/commits/``` (this should be commit link to show reference  on changelogs md.)


# Demo

i will use this repo for example ; https://github.com/qoomon/git-conventional-commits

<img src="https://raw.githubusercontent.com/AliYmn/changelog/master/images/ex1.png">

<img src="https://raw.githubusercontent.com/AliYmn/changelog/master/images/ex2.png">

---

The sample check logs are as follows : [Check it!](./exChangelog.md)
