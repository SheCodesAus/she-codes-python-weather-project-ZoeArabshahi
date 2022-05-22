def mean(weather_data):
    length=len(weather_data)
    sum=0
    for n in weather_data:
        sum += float(n)
    # print(sum)
    ave= sum/length
    return (float(ave))
print(mean([49, 57, 56, 55, 53]))  

# [49, 57, 56, 55, 53]  == 54   But mine= 4
# [-51, -58, -59, -52, -52, -48, -47, -53] == -52.5
    
# ["51", "58", "59", "52", "52", "48", "47", "53"])) == 52.5
    
# [51.0, 58.2, 59.9, 52.4, 52.1, 48.4, 47.8, 53.43]))  == 52.90375