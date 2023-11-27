#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word = input("Введите слово: ")
    k = int(input("Введите номер буквы для удаления: "))
    if k <= 0 or k > len(word):
        print("Некорректный номер буквы для удаления.")
    else:
        new_word = word[:2] + word[3:]
        new_word = new_word[:k - 1] + new_word[k:]
        print("Исходное слово:", word)
        print("Измененное слово:", new_word)
