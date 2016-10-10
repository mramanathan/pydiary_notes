#!_*_ coding:utf-8 _*_

#!/usr/bin/python3

import pandas as pd

""" The data refers to details on the total number of days each member of Rajya Sabha 
signed the member's attendance register during the 239 Session of Rajya Sabha for the 
period from 25-04-16 to 13-05-16.
"""

def nominated_members(attend):

    # 2: on read csv, get members filtered on states and use method on dataseries to get the names of nominated members
    print("~@" * 3 + " List of nominated members " + "~@" *3)
    member_list = attend.ix[:, 'State']
    for member, type in member_list.iteritems():
        if type == "Nominated":
            print(member + " was " + type.lower() + " to the Rajya Sabha.")

    return None


def nominated_members_details(attend):

    state_list = attend['State'] # mix of actual state names and nominations

    nom = state_list == "Nominated" # 
    print("~@" * 3 + " full list of nominations : " + "~@" *3)
    
    # output is garbled across multiple rows, but, atleast it works
    print(attend[nom])
    print("\n")

    # Interested to know if they signed in the register
    print("~@" * 3 + " And, did they remember to sign the register ? " + "~@" *3)
    print(attend[nom].ix[:, 'No of days member signed the register'])

    return None



def main():

    ''' read csv and run the desired function as per user's input '''

    # 1: Read csv, filter on states, get the nominations, apply on read csv to extract details about nominated members
    file = 'Rajyasabha_members_attendance_session239.csv'
    attend = pd.read_csv(file, index_col=2) # start the index with the MPs of Rajya Sabha

    nominated_members(attend)
    print("\n")
    nominated_members_details(attend)
    print("\n")


if __name__ == "__main__":
    main()
