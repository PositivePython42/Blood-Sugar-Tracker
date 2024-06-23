#Blood Sugar Tracker v0.1 : Sean Massey : seany42@gmail.com : Python 10.11
#Raise feedback and issues on GitHub please, https://github.com/PositivePython42/Blood-Sugar-Tracker/issues

import os, time

def refresh(delay):
    time.sleep(delay)
    os.system('clear')

#load data from CSV to working data frame
def auto_load():
    return

#save data from data frame to CSV
def auto_save():
    return
    
def record_reading():
    #take in date for reading
    #check it is a valid dd/mm input
    #ask if the reading breafast, lunch, dinner or bed
    #input reading and check it is valid
    #record to data from
    #print today's and yesterday's reading
    return
    
def last_readings(days):
    #print out formatted table of last x days readings
    #wait for user to press a key and return to menu
    return

#Main Program Loop

#If there is aready a data file, load it into a Panda's dataframe

while True:
    print('Blood Sugar Tracker v0.1')
    print()
    print('1. Record a blood sugar reading.')
    print('2. Last 7 days readings.')
    print('3. Current 5 day delta.')
    print('4. Current 20 day delta.')
    print('5. All reading averages graph.')
    print('6. Last reading versus average.')
    print('7. Export results to Excel.')
    print('0. Quit.')
    
    menu_option = int(input('Chose from 1 - 7, or 0 to quit :: '))
    match menu_option:
        case 1:
            print('Record a blood sugar reading')
        case 2:
            print('Last 7 days readings')
        case 3:
            print('Current 5 day delta')
        case 4:
            print('Current 20 day delta.')
        case 5:
            print('All reading averages graph')
        case 6:
            print('Last reading versus average.')
        case 7:
            print('Export to Excel.')
        case 0:
            break
        case _:
            print('Please chose one of the options above.')
            refresh(2)
        
