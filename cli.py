# -*- coding: utf-8 -*-
import sys
import argparse
from apriori import Apriori, ImprovedApriori


def load_data_from_cvs_file(fname):
    """Load data from *.cvs
    """
    transactions = []
    with open(fname, 'r') as f:
        for line in f.readlines():
            items = line.strip('\n').split(',')
            transactions.append(items)
    return transactions


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Apriori CLI app")
    parser.add_argument('-f', dest='input', action='store',
                        help='input data file *.csv',
                        default=None)
    parser.add_argument('-s', dest='minS', action='store',
                        help='minimum support value',
                        default=0.15,
                        type=float)
    parser.add_argument('-c', dest='minC', action='store',
                        help='minimum confidence value',
                        default=0.6,
                        type=float)
    parser.add_argument('-a', dest='items', action='append',
                        help='selected items',
                        default=[])
    result = parser.parse_args()
    if result.input is not None:
        transactions = load_data_from_cvs_file(result.input)
        minsup = result.minS
        minconf = result.minC
        items = result.items
        apriori = ImprovedApriori(transactions, minsup, minconf, items)
        apriori.run()
        apriori.print_frequent_itemset()
        apriori.print_rule()
