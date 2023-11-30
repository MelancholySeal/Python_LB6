#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    text = input("Введите предложение: ")

    for i, char in enumerate(text):
        if char == "а":
            print(i)
            break
        elif i == len(text)-1:
            print(
                'Буква "а" не найдена',
                file=sys.stderr
            )
