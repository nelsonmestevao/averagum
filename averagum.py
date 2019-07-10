#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

DATA_PATH = "data/"

courses = pd.read_csv(DATA_PATH + "courses.csv")
weights = pd.read_csv(DATA_PATH + "weights.csv")

courses = courses.dropna()

def multiplier(type):
    return weights[weights.Área_Científica == type].Ponderação.values[0]

total = 0
soma = 0

for index, row in courses.iterrows():
    soma += row.Classificação * multiplier(row.Área_Científica)
    total += multiplier(row.Área_Científica)

print("A tua média ponderada é:", soma/total)

