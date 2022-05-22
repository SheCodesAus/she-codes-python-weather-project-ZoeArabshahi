# numbers=[4,7,8,10,15,1]
# min_value=numbers[0]
# min_location = 0
# index = 0

# for num in numbers:
#     if num < min_value:
#         min_value = num
#         min_location=index
#     index += 1

# print(min_value, min_location)

def min(weather_data):
    
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

print(min([49, 57, 56, 55, 53, 49]))

# [49, 57, 56, 55, 53]   ==  expected_result = (49.0, 0)
#  [-10, -8, 2, -16, 4] ==  expected_result = (-16.0, 3)
#  [10.4, 14.5, 12.9, 8.9, 10.5, 11.7] ==  expected_result = (8.9, 3)
# ["49", "57", "56", "55", "53", "49"]  ==  expected_result = (49.0, 5)   ????
# [49, 57, 56, 55, 53, 49]  ==  expected_result = (49.0, 5)    ????
# []   == ()   ???

