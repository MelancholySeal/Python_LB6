#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    word1 = input("Введите первое слово:")
    word2 = input("Введите второе слово:")
    nullword = ''
    for i, char in enumerate(word1):
        if char not in word2:
            nullword += char+' '

    for i, char in enumerate(word2):
        if char not in word1:
            nullword += char+' '

    print(nullword)