
def max(weather_data):

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

print(max([49, 57, 56, 55, 57, 53, 49]))

# [49, 57, 56, 55, 53]   ==  expected_result = (57.0, 1)
#  [-10, -8, 2, -16, 4] ==  expected_result = (4.0, 4)
#  [10.4, 14.5, 12.9, 8.9, 10.5, 11.7] ==  expected_result = (14.5, 1)
# ["49", "57", "56", "55", "53", "49"]  ==  expected_result = (57.0, 1)   ????
#  [49, 57, 56, 55,57, 53, 49]  ==  expected_result = (57.0, 4)   ????
# []   ==  ()


