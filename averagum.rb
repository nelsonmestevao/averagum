#!/usr/bin/env ruby

require 'csv'

DATA_PATH = "data/"

courses = CSV.read(DATA_PATH + "courses.csv")
weights = CSV.read(DATA_PATH + "weights.csv")

print courses
# def multiplier(type)
#   weights
# end

# total = 0
# soma = 0

# print "A tua média ponderada é: "
# puts soma/total
