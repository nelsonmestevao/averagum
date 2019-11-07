#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='averagum.py'
        , description='''
            this description was indented weird but that is okay
        '''
        , epilog='''
            Enjoy :)
        '''
    )

    parser.add_argument('-d', '--data-path'
                        , metavar="PATH"
                        , help="directory data path"
                        , type=str
                        # , nargs=1
                        , default='data/'
                        , required=False
                        )

    return parser.parse_args()


def read_data(data_path):
    courses_csv = pd.read_csv(data_path + "courses.csv").dropna()
    weights_csv = pd.read_csv(data_path + "weights.csv")
    return courses_csv, weights_csv


def multiplier(course_type):
    return weights[weights.Área_Científica == course_type].Ponderação.values[0]


def show_results(courses_data_frame):
    total = 0
    soma = 0

    for index, row in courses_data_frame.iterrows():
        soma += row.Classificação * multiplier(row.Área_Científica)
        total += multiplier(row.Área_Científica)

    print("avg \t", round(soma / total, 2))
    print(round(courses.Classificação.describe(), 2))


if __name__ == '__main__':
    args = parse_arguments()
    courses, weights = read_data(args.data_path)
    show_results(courses)
