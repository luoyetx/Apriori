# -*- coding: utf-8 -*-

if __name__ == '__main__':

    transactions = dict()
    flag = True
    with open('origin_data.txt', 'r') as f:
        for line in f.readlines():
            no, null, item = line.strip('\n').split('\t')
            if no not in transactions:
                transactions[no] = []
            transactions[no].append(item)
    with open('data.csv', 'w') as f:
        for key, transaction in transactions.items():
            if not flag:
                f.write('\n')
            f.write(','.join(transaction))
            flag = False
