# Python Refresher Course
I'll be spending time reviewing Python fundamentals today

## Terms
**Functions** are reusable code. When done right, you can write clean and maintainable code. Functions can return something so that it does something useful. Functions can also call other existing functions, but they can also have side-effects

**method signature**, arguments that are required when you use a function 

**tuples** = sequence of immutable python obj. sequences like list, but unlike lists, tuples cannot be changed and denoted by parenthesis

**classes** are way to bundle behaviors and properties together. It’s a way to represent real-life information. 

## Class Example:
```python3
class Vegetable(object):
  def __init__(self, name, color, fresh):
    self.name = name
    self.color = color
    self.fresh = fresh

carrot = Vegetable('carrot', 'orange', True)
```

- We define a class called Vegetable who inherits from `object`. By default, classes run the `__init__` method, which is a reserved word for a constructor
- [More about self & __init__](https://www.tutorialspoint.com/What-is-difference-between-self-and-init-methods-in-python-Class)


## Goals:
- Data types (completed: 5/7)
- Functions (completed: 5/7)
- Classes (completed: 5/7)
- Build a full-stack app (inprogress: 5/7)
  - flask
    - frontend
    - backend => api 
- nginx
- unit testing 
- aws cloud
- elastic search
