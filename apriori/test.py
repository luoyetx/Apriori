# -*- coding: utf-8 -*-
from . import Apriori, ImprovedApriori


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

minsup = minconf = 0.6

if __name__ == '__main__':
    # test1
    apriori = Apriori(dataset1, minsup, minconf)
    apriori.run()
    apriori.print_frequent_itemset()
    apriori.print_rule()
    # test2
    apriori = Apriori(dataset1, minsup, minconf)
    apriori.set_selected_items(['beer', 'diaper'])
    apriori.run()
    apriori.print_frequent_itemset()
    apriori.print_rule()
    # test3
    apriori = ImprovedApriori(dataset1, minsup, minconf)
    apriori.run()
    apriori.print_frequent_itemset()
    apriori.print_rule()
    # test4
    apriori = ImprovedApriori(dataset1, minsup, minconf)
    apriori.set_selected_items(['beer', 'diaper'])
    apriori.run()
    apriori.print_frequent_itemset()
    apriori.print_rule()
