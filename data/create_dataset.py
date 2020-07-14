'''
Alex Knowlton
CSE 163 - Summer 2020
6/22/2020

This file creates a sample dataset, for a hypothetical student's spending
habits over four years at college, with columns of year, quarter, amount,
and type, where the type indicates what the amount was spent on, e.g.
housing, tuition, etc. Also saves the dataset to a .csv file called
'college_expenses.csv'
'''

import pandas as pd
from random import randint


def generate_quarter(year, quarter):
    """
    given ints of the year and the quarter,
    returns a DataFrame of a quarter's worth of expenses,
    tuition, room and board, textbooks, personal, and fees
    """
    years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
    quarters = ['Autumn', 'Winter', 'Spring']
    generated_quarter = list()
    year_tuition = calc_inflation(initial=3011, year=year)
    year_housing = calc_inflation(initial=3988, year=year)
    year_fees = calc_inflation(initial=304, year=year)
    # tuition dict
    generated_quarter.append({'Year': years[year], 'Quarter':
                             quarters[quarter], 'Type': 'Tuition',
                             'Amount': year_tuition})
    # housing dict
    generated_quarter.append({'Year': years[year], 'Quarter':
                             quarters[quarter], 'Type': 'Housing', 'Amount':
                             year_housing})
    # fees
    generated_quarter.append({'Year': years[year], 'Quarter':
                             quarters[quarter], 'Type': 'Fees',
                             'Amount': year_fees})
    # textbooks - anywhere from 1 to 4 books, costing from 40 to 105 $ each
    num_books = randint(1, 4)
    for i in range(num_books):
        cost = randint(40, 105)
        generated_quarter.append({'Year': years[year], 'Quarter':
                                 quarters[quarter], 'Type': 'Textbook',
                                 'Amount': cost})
    # personal
    num_personal = randint(2, 7)
    for i in range(num_personal):
        cost = randint(7, 45)
        generated_quarter.append({'Year': years[year], 'Quarter':
                                 quarters[quarter], 'Type': 'Personal',
                                 'Amount': cost})
    generated_quarter = pd.DataFrame(generated_quarter)
    return generated_quarter


def calc_inflation(initial, year):
    """
    based on the year, returns a pseudo-inflated form of the initial value,
    assuming a 1% yearly linear growth
    """
    return initial * (1 + (year * 0.01))


def generate_college_expenses():
    """
    generates a random college expense list for all four years
    """
    college = pd.DataFrame()
    for i in range(4):
        for j in range(3):
            college = college.append(generate_quarter(i, j))
    return college


def main():
    """
    saves a random college expense list as 'college_expenses.csv'
    """
    expenses = generate_college_expenses()
    expenses.to_csv('college_expenses.csv', index=False)


if __name__ == '__main__':
    main()
