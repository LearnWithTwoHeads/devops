## Code collaboration

### Intro
- Problem
    - You have a team of engineers and a codebase to run on a machine somewhere
    - How would you allow for the team to work together on that same codebase?
    - You make some edits to a codebase and it causes problems
    - How would you go back to a working version of the code base?
    - Someone makes edits to a codebase
    - How would you track who made what edits and why?
- Version control (Git)
    - Git allows multiple engineers to make contributions to a codebase without communication with each other
    - Git allows for audit trails for what piece of code got introduced to the codebase
    - Git allows for versioning the codebase, enabling easy spotting of code base versions
### Body
- Anatomy of a git repository
    - A data structure that represents a collection of files
    - Usually has an upstream reference, this is a remote version of a codebase hosted on some provider (GitHub, GitLab, etc.)
    - Branches:
        - lightweight pointers to specific commits within the repo
        - Allow developers to work on different features or bug fixes simultaneously
        - One developer can be in charge of a branch while the other developer is in charge of another branch
    - Commit:
        - Snapshot of the project at a specific point in time
        - Logical unit of work and captures changes made to the files
        - Has unique identifier (SHA-1 HASH)
- Git
    - Multiple moving parts but the marjotiry of the functionality lies mostly in three commands/actions
    - Three actions:
        - Adding changes: stages the changes for a commit action
        - Commit changes: adds some hashing for versioning of what is going to be contributed
        - Pushing/merging changes: introduces the new code into the existing codebase

### Examples
- Initializing a git repo
    - `git init`: creates a new git repository, and creates the `.git` subdirectory in the current working directory (configuration for git repo)
    -  `git remote add {upstream}`: show adding upstream repository for pushing changes out to it
    - `git checkout -b new-branch`: create a new branch to show making changes
    - `git add .`: show staging changes for committing
    - `git commit`: show commit those changes and how those changes get a version
    - `git push`: show pushing those changes to a remote repository and the effects in has

### Homework/Assignments
- Initialize a Git repo locally and connect it to a remote repository. Add some bash scripts that you can think of as code to your repo, whatever is helpful