## Git

In many organizations worldwide, [Git](https://git-scm.com/) has established itself as the heartbeat of modern software development. Organizations use Git in various ways, and a lot of them have even built software as interfaces to Git for their dev cycle. They view Git as the source of truth for the state of their applications/platforms at most times.

Personally, I view Git as an extremely significant tool that is essential for your everyday use as a DevOps engineer. We have been tooting Gits horn for the past 3-4 sentences so let's actually talk about what it is.

### What is Git?

In the simplest of definitions Git is a version control system, which could be distributed with a Git host. A version control system allows developers to basically collaborate on a code base in a way where every change to that code base can be tracked and versioned accordingly. Each edit to the code in a codebase can eventually be assigned a unique identifier called a commit hash, and that is how collaborators on the code base can refer to each change that happened in the code base, and even download the version of the code if they know the unique identifier (commit hash).

In order for developers to avoid clashing and stepping on each others toes when making edits to a code base, they can do what is called [branching](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell). Essentially, instead of working directly on a production copy of a code base, a developer can branch from the production copy, creating another copy identical to the production copy, but safer for edits. On this copy, a developer can make edits and do whatever they please with that copy, and if they are happy with there changes, they can [merge](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) there changes to the production copy.

There are a lot more nuances to this cycle of development such as [conflicts](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts), [being out of date with main copy](https://github.blog/changelog/2022-02-03-more-ways-to-keep-your-pull-request-branch-up-to-date/), etc. But if you understand basic branching and merging, you are about 80% of the way there to understanding, in my opinion. 

Now the distributed nature of Git only works when there is a Git host. Basically some upstream hosted service that understands the Git protocol. There are many SaaS (software-as-a-service) providers that act as Git hosts, and there are some open source ones that you can host yourself. For the rest of this module we will be using [GitHub](https://github.com/), which is one of the most popular SaaS products that provide Git repository hosting.

At this time, sign up for a GitHub account (it should be free!). And we will come back to that later in the module. Now lets get started with using Git.