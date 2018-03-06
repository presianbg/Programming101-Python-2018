import sys
from datetime import datetime
from collections import defaultdict


def main(argv):
    balance = defaultdict(int)
    fin = 0
    with open(argv, 'r') as raw_balance:
        for line in raw_balance:
            if line.startswith("---"):
                fin = 1
                continue
            day_spent = (line.strip('\n').split(','))
            if fin:
                end_date = datetime.strptime(day_spent[0], "%d/%m/%Y")
                break
            balance[datetime.strptime(day_spent[1], "%d/%m/%Y")] += int(day_spent[0])
        print(sum([amount for date, amount in balance.items() if date <= end_date]))


if __name__ == '__main__':
    main(sys.argv[1])
