# -*- coding: utf-8 -*-
from apriori import Apriori


dataset1 = [
    ['bread', 'milk'],
    ['bread', 'diaper', 'beer', 'egg'],
    ['milk', 'diaper', 'beer', 'cola'],
    ['bread', 'milk', 'diaper', 'beer'],
    ['bread', 'milk', 'diaper', 'cola'],
]

dataset2 = [
    [1, 2, 3, 4],
    [1, 2, 4],
    [1, 2],
    [2, 3, 4],
    [2, 3],
    [3, 4],
    [2, 4],
]

if __name__ == '__main__':
    apriori = Apriori(dataset1, 0.6, 0.6)
    apriori.run()
    apriori.print_frequent_itemset()
    apriori.print_rule()
