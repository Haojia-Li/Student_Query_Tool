# -*- coding: utf-8 -*-
"""
# Python Term Project

# Team members:
# Letao Li
# Tianyi Hu
# Haojia Li

"""

import pandas as pd
# read file via pandas
df = pd.read_csv('Students.txt', sep = '\t')
# set index start from 1
df.index = df.index + 1
# set pandas may display all columns and all rows
pd.set_option('display.max_rows', df.shape[0]+1)
pd.set_option('display.max_columns', df.shape[1]+1)

# create a df_2 for edit
df_2 = df.copy()
# add a column for number of student
df_2['Num of student'] = 1
# add a column for the percentage of student
df_2['Percentage'] = 0.01

# function for finding correct name with given start chars of lastname
def Lastname(lastname):
    df_ln = df[df['Last'].str.lower().str.startswith(lastname)].reset_index().drop(columns=['index'])
    df_ln.index = df_ln.index + 1
    return df_ln

# function for filter all records by given gradyear
def Gradyear(year):
    result = df[df['GradYear'] == int(year)].reset_index().drop(columns = 'index')
    result.index = result.index + 1
    return result

# function for summary report on a certain gradyear
def Grad_on_year(year):
    df_grad_on_year = df_2.copy()
    df_grad_on_year = df_grad_on_year[df_grad_on_year['GradYear'] == int(year)][['DegreeProgram', 'Num of student', 'Percentage']].groupby('DegreeProgram').sum()
    # convert percentage from float to percent
    df_grad_on_year['Percentage'] = df_grad_on_year['Percentage'].apply(lambda x: format(x, '.2%'))
    # reset index
    df_grad_on_year = df_grad_on_year.reset_index()
    # set index start from 1
    df_grad_on_year.index = df_grad_on_year.index + 1
    return df_grad_on_year

# function for summary report after a certain gradyear
def Grad_after_year(year):
    df_grad_after_year = df_2.copy()
    df_grad_after_year = df_grad_after_year[df_grad_after_year['GradYear'] > int(year)][['DegreeProgram', 'Num of student', 'Percentage']].groupby('DegreeProgram').sum()
    # convert percentage from float to percent
    df_grad_after_year['Percentage'] = df_grad_after_year['Percentage'].apply(lambda x: format(x, '.2%'))
    # reset index
    df_grad_after_year = df_grad_after_year.reset_index()
    # set index start from 1
    df_grad_after_year.index = df_grad_after_year.index + 1
    return df_grad_after_year

t = True

while t:
    # set input questions
    inpt = input('Select the options below:\n1. Display all student records \n2. Display students whose last name begins with a certain string (case insensitive) \n3. Display all records for students whose graduating year is a certain year \n4. Display a summary report of number and percent of students in each program, for students graduating on a certain year \n5. Display a summary report of number and percent of students in each program, for students graduating after a certain year \n \n Enter 1, 2, 3， 4 or 5: ')
    print('')
    # input 1 for display all student records
    if inpt == '1':
        print(df)
        # ask if the user would like to keep using the system
        decision = input('Do you like to try again? Enter Y/Yes to try again, enter something else to stop: ').lower()
        if decision == 'y' or decision == 'yes':
            continue
        else:
            print('Thanks for using the system, bye bye.')
        t = False
    # input 2 for finding correct name with given start chars of lastname
    elif inpt == '2':
        inpt_2 = input('Enter a last name begins with a certain string (case insensitive): ').lower()
        print('')
        result = Lastname(inpt_2)
        if len(result) == 0:
            print("There is no student's last name starting with "+inpt_2)
        else:
            print(result)
        # ask if the user would like to keep using the system
        decision = input('Do you like to try again? Enter Y/Yes to try again, enter something else to stop: ').lower()
        if decision == 'y' or decision == 'yes':
            continue
        else:
            print('Thanks for using the system, bye bye.')
        t = False
    elif inpt == '3':
        # input 3 for filter all records by given gradyear
        inpt_3 = input('Enter a graduating year: ')
        print('')
        # ask if the user would like to keep using the system when user input invaild stuff
        if inpt_3.isdigit() == False:
            decision = input('Input is not valid, do you like to try again? Enter Y/Yes to try again, enter something else to stop: ').lower()
            if decision == 'y' or decision == 'yes':
                continue
            else:
                print('Thanks for using the system, bye bye.')
                break
        result = Gradyear(inpt_3)
        if len(result) == 0:
            print("There is no student's graduate on "+inpt_3)
        else:
            print(result)
        # ask if the user would like to keep using the system
        decision = input('Do you like to try again? Enter Y/Yes to try again, enter something else to stop: ').lower()
        if decision == 'y' or decision == 'yes':
            continue
        else:
            print('Thanks for using the system, bye bye.')
        t = False
    # input 4 for summary report on a certain gradyear
    elif inpt == '4':
        inpt_4 = input('Enter a graduating year: ')
        print('')
        # ask if the user would like to keep using the system when user input invaild stuff
        if inpt_4.isdigit() == False:
            decision = input('Input is not valid, do you like to try again? Enter Y/Yes to try again, enter something else to stop: ').lower()
            if decision == 'y' or decision == 'yes':
                continue
            else:
                print('Thanks for using the system, bye bye.')
                break
        result = Grad_on_year(inpt_4)
        if len(result) == 0:
            print("There is no student's graduating on "+inpt_4)
        else:
            print(result)
        # ask if the user would like to keep using the system
        decision = input('Do you like to try again? Enter Y/Yes to try again, enter something else to stop: ').lower()
        if decision == 'y' or decision == 'yes':
            continue
        else:
            print('Thanks for using the system, bye bye.')
        t = False
    # input 5 for summary report after a certain gradyear
    elif inpt == '5':
        inpt_5 = input('Enter a graduating year: ')
        print('')
        # ask if the user would like to keep using the system when user input invaild stuff
        if inpt_5.isdigit() == False:
            decision = input('Input is not valid, do you like to try again? Enter Y/Yes to try again, enter something else to stop: ').lower()
            if decision == 'y' or decision == 'yes':
                continue
            else:
                print('Thanks for using the system, bye bye.')
                break
        result = Grad_after_year(inpt_5)
        if len(result) == 0:
            print("There is no student's graduating after "+inpt_5)
        else:
            print(result)
        # ask if the user would like to keep using the system
        decision = input('Do you like to try again? Enter Y/Yes to try again, enter something else to stop： ').lower()
        if decision == 'y' or decision == 'yes':
            continue
        else:
            print('Thanks for using the system, bye bye.')
        t = False
    else:
        # ask if the user would like to keep using the system when user input invaild stuff
        inpt_6 = input('Input is not valid, do you like to try again? Enter Y/Yes to try again, enter something else to stop： ').lower()
        if inpt_6 == 'y' or inpt_6 == 'yes':
            continue
        else:
            print('Thanks for using the system, bye bye.')
            t = False
        