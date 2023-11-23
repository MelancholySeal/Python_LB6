#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    text = input("Введите предложение: ")

    for i in range(len(text)):
        if text[i] == "а":
            print(i)
            break
        elif i == len(text)-1:
            print(
                'Буква "а" не найдена',
                file=sys.stderr
            )
