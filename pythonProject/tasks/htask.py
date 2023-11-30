#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    word1 = input("Введите первое слово:")
    word2 = input("Введите второе слово:")
    nullword = ''
    for i in enumerate(word1):
        char = i[0]
        if word1[char] not in word2:
            nullword += word1[char]+' '

    for i in enumerate(word2):
        char = i[0]
        if word2[char] not in word1:
            nullword += word2[char]+' '

    print(nullword)