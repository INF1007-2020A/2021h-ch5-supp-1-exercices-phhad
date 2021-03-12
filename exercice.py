#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import math

def get_bill(name, data):
    INDEX_NAME = 0
    INDEX_QUANTITY = 1
    INDEX_PRICE = 2
    taxe = 0.15
    VAL_Taxe = 0
    Sous_total = 0
    for item in data:
        Sous_total += item[INDEX_QUANTITY] * item[INDEX_PRICE]

    VAL_Taxe = Sous_total * taxe

    TOTAL = Sous_total + VAL_Taxe

    sous_total_print=f"SOUS-TOTAL {Sous_total : >10.2f} $"


    taxes_print = f"TAXES      {VAL_Taxe : >10.2f} $"
    total_print =  f"TOTAL      {TOTAL : >10.2f} $"

    return name + "\n" + sous_total_print + "\n" + taxes_print + "\n"  + total_print

def format_number(number, num_decimal_digits):
    #1234.5678
    number = round(number,3)
    #3451234.568
    numberStr = str(number)
    resultat = ""
    resultat = numberStr[3:7]

    #'3 451 234.568'




def get_triangle(num_rows):
    CHAR_BORD = "+"
    resultat = ""
    CHAR_TRIANGLE = "A"

    chaineBord = CHAR_BORD * (num_rows * 2 + 1 )

    resultat = resultat + chaineBord + "\n"
    for i in range(num_rows):
        chaine =  "+" + " " * (num_rows - i - 1)
        chaine = chaine + CHAR_TRIANGLE * (2 * i + 1 )
        chaine = chaine + " " * (num_rows - i - 1) + "+"
        resultat = resultat + chaine + "\n"
    resultat = resultat + chaineBord
    return resultat


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
