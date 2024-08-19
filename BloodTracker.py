#Blood Sugar Tracker v0.1 : Sean Massey : seany42@gmail.com : Python 3.10.11
#Raise feedback and issues on GitHub please, https://github.com/PositivePython42/Blood-Sugar-Tracker/issues

import os, time, csv
from dateutil.parser import parse
import pandas as pd
from pandas.core.frame import DataFrame

blood_data = []
the_columns = ['Date', 'Time', 'Blood Sugar']


def refresh(delay):
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')


def is_valid_date(test_date, fuzzy=False):
    try:
        parse(test_date, fuzzy=fuzzy)
        return True
    except ValueError:
        return False


def create_new_data_file():
    with open('blood_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Time', 'Blood Sugar'])


def load_data(data):
    with open('blood_data.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = []
        for row in reader:
            rows.append(row)
            return rows


def auto_save(data_to_save):  #save data from list to CSV
    data_to_save.to_csv('blood_data.csv', index=False)
    print('Data saved successfully.')
    refresh(1)


def record_reading():
    reading_time = 0

    while True:  #check it is a valid dd/mm input
        print()
        data_date = input('What is the date for the reading (dd/mm/yy) : ')
        if is_valid_date(data_date) is False:
            print('Enter data in the right format (dd/mm/yy).')
            continue
        else:
            break

    while reading_time <= 0 or reading_time >= 5:  #ask if the reading breafast, lunch, dinner or bed
        print()
        print('Was the reading taken before:')
        print('1. Breakfast')
        print('2. Lunch')
        print('3. Dinner')
        print('4. Bedtime')
        print()
        reading_time = int(input('Chose 1, 2, 3, 4 : '))
        print()
    reading = float(input('What was the reading : '))  #input reading as a float
    new_blood_data = [data_date, reading_time, reading]
    refresh(1)
    return new_blood_data


def last_readings(readings): # print last x days of data, come back to do it in a nice format!
    print()
    print('Blood Sugar readings for the last', readings, 'readings:')
    print(blood_data.tail(readings).to_string(index=False))
    refresh(5)
    return

def last_readings_bydate(days):
    #turn the data column data in proper dates and create a new df with the DF sorted by date.
    blood_data['Date'] = pd.to_datetime(blood_data['Date'], format='%d/%m/%Y')
    sorted_df = blood_data.sort_values(by="Date", ascending=False)
    
    #get the last 5 unique days that data has been entered on
    dates_to_print = []
    for index, row in sorted_df.iterrows():
        if row['Date'] not in dates_to_print:
            dates_to_print.append(row['Date'])
        if len(dates_to_print) == 5:
            break
       
    #print any entries in the last x days list
    filtered_df = pd.DataFrame(columns=the_columns)
    entry_row = 1
    print(f'Your last {days} results are;')
    for index, row in sorted_df.iterrows():
        if row['Date'] in dates_to_print:
            temp_df = [row['Date'], row['Time'], row['Blood Sugar']]
            filtered_df.loc[entry_row] = temp_df
            entry_row += 1
    print(filtered_df.to_string(index=False))
    refresh(5)
    return

def previous_period(period):
    #show the same for the previuous x days before the period requested
    #show previous x days readings + daily average + period average
    #show the range, average delta for the 4 resding times and the x day periods
    #colour the readings that are lower or same green, the ones that are high red
    return


def all_readings():
    #Pulls up a line chart of the 4 daily readings and the daily average
    return


def current_readings_comparison():
    #Choses the last day when you input all 4 daily readings
    #builds a histogram comparting them to average for each time slot + data table of both
    return


#Main Program Loop

try:
    blood_data = pd.read_csv('blood_data.csv')

except FileNotFoundError:
    blood_data = pd.DataFrame(columns=the_columns)
    blood_data.to_csv('blood_data.csv', index=False)

while True:
    print('🍚🩸Blood Sugar Tracker v0.1\n')
    print('1. Record a blood sugar reading.')
    print('2. Last 10 readings.')
    print('3. Last 7 days readings.')
    print('4. Current 5 day delta.')
    print('5. Current 20 day delta.')
    print('6. All reading averages graph.')
    print('7. Last reading versus average.')
    print('8. Export results to Excel.')
    print('0. Quit.')

    menu_option = int(input('Chose from 1 - 7, or 0 to quit :: '))
    match menu_option:
        case 1:
            new_data = record_reading()
            blood_data.loc[len(blood_data.index)] = new_data
            auto_save(blood_data)
        case 2:
            last_readings(10)
        case 3:
            last_readings_bydate(7)
        case 4:
            print('Current 5 day delta')
        case 5:
            print('Current 20 day delta.')
        case 6:
            print('All reading averages graph')
        case 7:
            print('Last reading versus average.')
        case 8:
            blood_data.to_excel('excel_blood_data.xls', index=False)
        case 0:
            break
        case _:
            print('Please chose one of the options above.')
            refresh(2)
