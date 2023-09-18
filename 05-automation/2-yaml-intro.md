## YAML

YAML is a widely-used data serialization language. It allows one to reason about data in a structured way.

As we have learned in networking, there exists ways you can connect computers to talk to each other. Once you have set the hardware, and cables up for the computers to talk to each other, how would computers make sense of the information they are receiving from other computers through the network?

This is where a data serialization language like YAML comes into play. You can think about it as a set of conventions that allow for easy and seamless communication from one machine to the next. This property of YAML allows for it to also be a nice configuration language, which Ansible makes use of it as.

Lets learn about some types you will encounter in YAML.

### Types

There are 3 top level types that are native to YAML. Lets talk about each 3:

1. Maps/Dictionaries: Unordered sets of key/value pairs
2. Arrays/Lists: Ordered sequence of nodes (a node here can be a dictionary or a literal)
3. Literals: Base type (string, number, boolean) All lists or Dictionaries eventually boil down to having properties with literal values

Do not worry too much about the technicalities here, this is just to introduce how YAML is made up. If you want more detail you can read more about YAML and its types [here](https://spacelift.io/blog/yaml).

### Examples

To understand YAML a bit more, it might be useful to look at some examples:

**Example 1:** Just literals

```yaml
name: Abena
occupation: DevOps Engineer
salary: 1000000
```

The above snippet has three literals, `name`, `occupation`, and `salary`. The values of these literals are a string "Abena", another string "DevOps Engineer", and a number "1000000" respectively.

**Example 2:** A dictionary with literals

```yaml
employee:
  name: Abena
  occupation: DevOps Engineer
  salary: 1000000
```

The above snippet has one dictionary called `employee`. Remember that dictionary are unordered sets of key/value pairs and eventually boil down to literals. That happens in this case. `employee` has three key/value pairs: `name`, `occupation`, `salary`, which have the same values as the above example snippet.

**Example 3:** An array/list of literals

```yaml
occupations:
  - engineer
  - doctor
  - lawyer
  - accountant
```

The above snippet has one array/list called `occupations`. The array/list has 4 literal values which are strings `engineer`, `doctor`, `lawyer`, and `accountant`.

**Example 4:** Nesting types

```yaml
employees:
  - name: Abena
    occupation: DevOps Engineer
    salary: 100000
  - name: Yaa Asentwaa
    occupation: Software Engineer
    salary: 100000
  - name: Kwaku Frimpong
    occupation: Designer
    salary: 100000
```

The above snippet shows the power of `YAML` when it comes to nesting types. It has a top-level key which is a array/list called `employees`. The array/list has values which are dictionaries that all have the same three keys `name`, `occupation`, and `salary`. The keys in these dictionaries boil down to literal values which are `Abena`, `Yaa Asentwaa`, and `Kwaku Frimpong` for names respectively, `DevOps Engineer`, `Software Engineer`, and `Designer` for occupation respectively, and `1000000` for all three salaries.

You can nest these types as deep as you want, all according to your use case.

Now that we know a bit about YAML let us now write some configuration for Ansible and get it to do something in the next section!