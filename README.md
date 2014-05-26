Apriori
=======

a simple implementation of Apriori algorithm in Python.

### How to use

```python
from apriori import Apriori

dataset = [
    ['bread', 'milk'],
    ['bread', 'diaper', 'beer', 'egg'],
    ['milk', 'diaper', 'beer', 'cola'],
    ['bread', 'milk', 'diaper', 'beer'],
    ['bread', 'milk', 'diaper', 'cola'],
]
minsup = minconf = 0.6

ap = Apriori(dataset, minsup, minconf)
# run algorithm
ap.run()
# print out frequent itemset
ap.print_frequent_itemset()
# print out rules
ap.print_rule()
```

### LICENSE

MIT
