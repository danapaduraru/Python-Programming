"""
5. The validate_dict function that receives as a parameter:
a set of tuples that represent validation rules for a dictionary with string keys and values of the string type and a dictionary.

A rule is defined as follows: (key, "prefix", "middle", "suffix").
A value is considered valid if it starts with "prefix", "middle" is inside the value (
not at the beginning or end) and ends with "suffix".
The function will return True if the given dictionary matches all the rules, False otherwise.


Example: the rules  s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}  and
d = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
=> False because although the rules are respected for "key1" and "key2", "key3" that does not appear in the rules.
"""

def validate_dict(tuples):
    pass
