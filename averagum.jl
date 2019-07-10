#!/usr/bin/env julia

using Pkg

PKGS = [
        "CSV",
        "DataFrames",
     ]

for pkg in PKGS
  if pkg ∉ keys(Pkg.installed())
    Pkg.add(pkg)
  end
end

using CSV
using DataFrames

DATA_PATH = "data/"

courses = CSV.read(DATA_PATH * "courses.csv")
weights = CSV.read(DATA_PATH * "weights.csv")

courses = courses[completecases(courses), :]

nrows, ncols = size(courses)

multiplier(type) = weights[weights[:Área_Científica] .== type, :Ponderação][1]

total = 0
soma = 0

for i in 1:nrows
    global soma
    global total
    soma  += courses[:Classificação][i] * multiplier(courses[:Área_Científica][i])
    total += multiplier(courses[:Área_Científica][i])
end

println("A tua média ponderada é: ", soma/total)

