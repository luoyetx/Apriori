# -*- coding: utf-8 -*-
from collections import defaultdict
from itertools import combinations
from sys import stdout


class cached_property(object):
    """A cached property only computed once
    """
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, cls):
        if obj is None: return self
        value = obj.__dict__[self.func.__name__] = self.func(obj)
        return value


class Apriori(object):
    """A simple implementation of Apriori algorithm
        Example:
        
        dataset = [
            ['bread', 'milk'],
            ['bread', 'diaper', 'beer', 'egg'],
            ['milk', 'diaper', 'beer', 'cola'],
            ['bread', 'milk', 'diaper', 'beer'],
            ['bread', 'milk', 'diaper', 'cola'],
        ]
        minsup = minconf = 0.6

        apriori = Apriori(dataset, minsup, minconf)
        apriori.run()
        apriori.print_rule()

        Results:
            Rules
            milk --> bread (confidence = 0.75)
            bread --> milk (confidence = 0.75)
            diaper --> bread (confidence = 0.75)
            bread --> diaper (confidence = 0.75)
            beer --> diaper (confidence = 1.0)
            diaper --> beer (confidence = 0.75)
            diaper --> milk (confidence = 0.75)
            milk --> diaper (confidence = 0.75)
    """

    def __init__(self, transaction_list, minsup, minconf):
        self.transaction_list = transaction_list
        self.minsup = minsup
        self.minconf = minconf

        self.frequent_itemset = dict()
        # counter for every frequenr itemset
        self.frequent_itemset_counter = defaultdict(int)
        # convert transaction_list
        self.transaction_list = list([frozenset(transaction) \
            for transaction in transaction_list])
        self.rule = []

    @cached_property
    def items(self):
        """Return all items in the transaction_list
        """
        items = set()
        for transaction in self.transaction_list:
            for item in transaction:
                items.add(item)
        return items

    def filter_with_minsup(self, itemset):
        """Return subset of itemset which satisfies minsup
        and record their frequences
        """
        local_counter = defaultdict(int)
        for item in itemset:
            for transaction in self.transaction_list:
                if item.issubset(transaction):
                    local_counter[item] += 1
        # filter with counter
        result = set()
        for item, count in local_counter.items():
            support = float(count) / len(self.transaction_list)
            if support >= self.minsup:
                result.add(item)
                self.frequent_itemset_counter[item] = count
        return result

    def _apriori_gen(self, itemset, length, mode=0):
        """Return candidate itemset with given itemset and length
        """
        if mode == 0:
            # simply use F(k-1) x F(k-1) (itemset + itemset)
            return set([x.union(y) for x in itemset for y in itemset \
                if len(x.union(y)) == length])
        else:
            # simply use F(k-1) x F(1) (itemset + frequent_itemset[1])
            return set([x.union(y) for x in itemset for y in self.frequent_itemset[1] \
                if len(x.union(y) == length)])

    def generate_frequent_itemset(self):
        """Generate and return frequent itemset
        """
        k = 1
        current_itemset = set()
        # generate 1-frequnt_itemset
        for item in self.items: current_itemset.add(frozenset([item]))
        self.frequent_itemset[k] = self.filter_with_minsup(current_itemset)
        # generate k-frequent_itemset
        while True:
            k += 1
            current_itemset = self._apriori_gen(current_itemset, k)
            current_itemset = self.filter_with_minsup(current_itemset)
            if current_itemset != set([]):
                self.frequent_itemset[k] = current_itemset
            else:
                break
        return self.frequent_itemset

    def _generate_rule(self, itemset, frequent_itemset_k):
        """Generate rule with F(k)
        """
        # make sure the itemset has at least two element to generate the rule
        if len(itemset) < 2:
            return
        for element in combinations(list(itemset), 1):
            rule_head = itemset - frozenset(element)
            confidence = float(self.frequent_itemset_counter[frequent_itemset_k]) / \
                self.frequent_itemset_counter[rule_head]
            if confidence >= self.minconf:
                rule = ((rule_head, itemset - rule_head), confidence)
                # if rule not in self.rule, add and recall _generate_rule() in DFS
                if rule not in self.rule:
                    self.rule.append(rule);
                    self._generate_rule(rule_head, frequent_itemset_k)

    def generate_rule(self):
        """Generate and return rule
        """
        # generate frequent itemset if not generated
        if len(self.frequent_itemset) == 0:
            self.generate_frequent_itemset()
        # generate in DFS style
        for key, val in self.frequent_itemset.items()[1:]:
            for itemset in val:
                self._generate_rule(itemset, itemset)
        return self.rule

    def run(self):
        """Run Apriori algorithm and return rules
        """
        self.generate_frequent_itemset()
        self.generate_rule()
        return self.rule

    def print_frequent_itemset(self):
        """Print out frequent itemset
        """
        stdout.write('Frequent itemset:\n')
        for key, val in self.frequent_itemset.items():
            #stdout.write('frequent itemset size of {0}:\n'.format(key))
            for itemset in val:
                for item in itemset:
                    stdout.write('{0} '.format(item))
                stdout.write('(support = {0})\n'.format(self.frequent_itemset_counter[itemset] / \
                    float(len(self.transaction_list))))

    def print_rule(self):
        """Print out rules
        """
        stdout.write('Rules:\n')
        for rule in self.rule:
            head = rule[0][0]
            tail = rule[0][1]
            confidence = rule[1]
            for item in head:
                stdout.write('{0} '.format(item))
            stdout.write('--> ')
            for item in tail:
                stdout.write('{0} '.format(item))
            stdout.write('(confidence = {0})\n'.format(confidence))
