# CodeWars Python Solutions

---

## Is he gonna survive?



### Task
A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?

Return True if yes, False otherwise :)


---


### Solution


```python
def hero(bullets, dragons):
    if bullets / dragons >= 2:
        return True
    else:
        return False
        
```

---
### Comment


[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
