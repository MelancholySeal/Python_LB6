#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    text = input("Введите предложение: ")

    for i in enumerate(text):
        char = i[0]
        if text[char] == "а":
            print(char)
            break
        elif char == len(text)-1:
            print(
                'Буква "а" не найдена',
                file=sys.stderr
            )
