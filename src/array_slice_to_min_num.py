# -*- coding: UTF-8 -*-

import operator

if __name__ == "__main__":
    test = [3, 32, 321]

    numbers = list(map(str, test))
    numbers.sort(cmp=lambda x, y: operator.eq(x+y, y+x))
    print(''.join(numbers))
