# CodeWars Python Solutions

---

## Create phone number



### Description:

Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in
the form of a phone number.
Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!

---


### Solution


```python
def create_phone_number(n):
    for x in range(len(n)):
        return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"
        
```

---
### Comment

Well...
```python
def create_phone_number(n):
     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
```



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
