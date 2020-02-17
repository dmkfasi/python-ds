Given a string with a certain rule: _k[string]_ should be expanded to string k times. So for example, _3[abc]_ should be expanded to *abcabcabc*. Nested expansions can happen, so _2[a2[b]c]_ should be expanded to *abbcabbc*.

Your starting point:

```python
def decodeString(s):
  # Fill this in.

print decodeString('2[a2[b]c]')
# abbcabbc
```