## Extending Ansible Playbook

In the previous section we wrote and executed our first Ansible playbook against the frontend machine. We will now look into doing the same for the other two tiers and provision what we need to there.

### Getting the backend machine ready

As we have done before, Before getting started let us copy the directory on the Ansible control machine to another directory called `ansible-exercise3`.

```bash
$ cp -r ansible-exercise2 ansible-exercise3
```

The directory should contain `frontend.yml`, lets change this to `fe-be.yml`.

```bash
$ mv frontend.yml fe-be.yml
```
