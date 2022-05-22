import csv
from datetime import datetime
from encodings import utf_8


DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    #strptime() -> what data type do they expect as an argument
    #strftime()
    date_in=datetime.strptime(iso_string,"%Y-%m-%dT%H:%M:%S%z")
    date_out=datetime.strftime(date_in,"%A %d %B %G")
    return(date_out)


def convert_f_to_c(temp_in_fahrenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """

    temp_in_c = (float(temp_in_fahrenheit) - 32) * (5/9)
    temp_in_c_float = "{:.1f}".format(temp_in_c)
    return float(temp_in_c_float)


    







def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    length=len(weather_data)
    sum=0
    for n in weather_data:
        sum += float(n)
    ave= sum/length
    return (float(ave))



def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    # pass
    list_from_reader=[]
    with open (csv_file, encoding="utf-8") as object_file:
            reader=csv.reader(object_file)
            next(reader) # this is to remove the header
            for line in reader:
                if line != []:
                    list_from_reader.append([line[0],int(line[1]), int(line[2])])
            print(list_from_reader)
    return list_from_reader




def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    # pass
    index=0
    min_location=0
    if weather_data != []:
        min_value=float(weather_data[0])
        for num in weather_data:
        
            if float(num) <= min_value:
                min_value= float(num)
                min_location=index
            index = index + 1
    else:
        return()
    return min_value, min_location




def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    # pass
    index=0
    max_location=0
    if weather_data != []:
        max_value=float(weather_data[0])
        
        for num in weather_data:
            if float(num) >= max_value:
                max_value = float(num)
                max_location=index
            index = index + 1
    else:
        return()
    return max_value, max_location


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
#to get the lowest and highest temp in the min temps and max temps, I created the following loop
# to collect the mins and max temps in a list and get the lowest and highest by calling
# the above functions. 

    min_temps=[]
    max_temps=[]
    date_collection=[]

    for i in weather_data:
        # print(i[1]) 
        date_collection.append(i[0])
        min_temps.append(i[1])
        max_temps.append(i[2])
    # print(date_collection)
    lowest_temp=find_min(min_temps)
    avg_min_temps=calculate_mean(min_temps)
    highest_temp=find_max(max_temps)
    avg_max_temps=calculate_mean(max_temps)
#     # min_temp,min_index=find_min(min_temps)
#     # return min_index
# # example=[
#         #     ["2021-07-02T07:00:00+08:00", 49, 67],
#         #     ["2021-07-03T07:00:00+08:00", 57, 68],
#         #     ["2021-07-04T07:00:00+08:00", 56, 62],
#         #     ["2021-07-05T07:00:00+08:00", 55, 61],
#         #     ["2021-07-06T07:00:00+08:00", 53, 62]
#         # ]
# # to generate_summary:
    # for i in weather_data:
    #     summary=f"{len(weather_data)} Day Overview\n"
    #     summary+=f"  The lowest temperature will be {convert_f_to_c(lowest_temp[0])}{DEGREE_SYMBOL}, and will occur on {convert_date(weather_data[(lowest_temp[-1])][0])}. \n"
    #     summary+=f"  The highest temperature will be {(convert_f_to_c(highest_temp[0]))}{DEGREE_SYMBMOL}, and will occur on {convert_date(weather_data[(highest_temp[-1])][0])}.\n"
    #     summary+=f"  The average low this week is {convert_f_to_c(ave_min_temps)}{DEGREE_SYMBMOL}.\n"
    #     summary+=f"  The average high this week is {convert_f_to_c(ave_max_temps)}{DEGREE_SYMBMOL}.\n"
    # return(summary)

    for i in weather_data:
        summary=f"{len(weather_data)} Day Overview\n"
        summary+=f"  The lowest temperature will be {convert_f_to_c(lowest_temp[0])}{DEGREE_SYBMOL}, and will occur on {convert_date(weather_data[(lowest_temp[-1])][0])}.\n"
        summary+=f"  The highest temperature will be {(convert_f_to_c(highest_temp[0]))}{DEGREE_SYBMOL}, and will occur on {convert_date(weather_data[(highest_temp[-1])][0])}.\n"
        summary+=f"  The average low this week is {convert_f_to_c(avg_min_temps)}{DEGREE_SYBMOL}.\n"
        summary+=f"  The average high this week is {convert_f_to_c(avg_max_temps)}{DEGREE_SYBMOL}.\n"
    return(summary)













def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary=""
    list=[]
    for i in weather_data:
        summary+=f"---- {convert_date(i[0])} ----\n"
        summary+=f"  Minimum Temperature: {convert_f_to_c(i[1])}{DEGREE_SYBMOL}\n"
        summary+=f"  Maximum Temperature: {convert_f_to_c(i[2])}{DEGREE_SYBMOL}\n"
        summary+=f"\n"
        list.append(summary)
    return(summary)
