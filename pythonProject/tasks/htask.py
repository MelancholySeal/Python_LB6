#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    word1 = input("Введите первое слово:")
    word2 = input("Введите второе слово:")
    nullword = ''
    for i in range(len(word1)):
        if word1[i] not in word2:
            nullword += word1[i]+' '

    for i in range(len(word2)):
        if word2[i] not in word1:
            nullword += word2[i]+' '

    print(nullword)