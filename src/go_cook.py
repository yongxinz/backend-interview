#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def main():
    x = []

    # 此处没有用raw_input，是因为只能输入一行，换行，程序就结束;
    # sys.stdin想要结束输入，直接用ctrl+d;
    for line in sys.stdin:
        x.extend(line.split())

    return len(set(x))


if __name__ == "__main__":
    print main()
