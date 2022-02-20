# CodeWars Python Solutions

---

## Needle in the haystack


### Description:

Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:

find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
should return "found the needle at position 5" (in COBOL "found the needle at position 6")


### Solution


```python
def find_needle(haystack):
    if "needle" in haystack:
        return (f"found the needle at position {haystack.index('needle')}")
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
