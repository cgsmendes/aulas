#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

a=float(2)
b=float(20)
c=float(20)

def bhaskara(a, b, c):
    delta = (b * b) - (4 * a * c)
    print(delta)
    if delta < 0:
        # Delta menor que 0, a função não tem raízes
        return False
    else:
        delta = sqrt(delta)
        r1 = (-b + delta) / (2 * a)
        r2 = (-b - delta) / (2 * a)
        raizes = (r1, r2)
        # Retornando as raízes
        return raizes