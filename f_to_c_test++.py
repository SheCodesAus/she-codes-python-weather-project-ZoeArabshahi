import math
from unittest import result


# 1)
def convert_f_to_c(temp_in_fahrenheit):
    temp_in_c = (float(temp_in_fahrenheit) - 32) * (5/9)
    temp_in_c_float = "{:.1f}".format(temp_in_c)
    return(temp_in_c_float)

print(convert_f_to_c("77"))


# 90 == 32.2
# -10  == -23.3
# 64.4  == 18        what i get = 18.0
# "77"  == 25.0



# 2)
# def convert_f_to_c(temp_in_faren):
#     temp_in_c = (float(temp_in_faren) - 32) * (5/9)
#     print(temp_in_c)
#     if math.modf(temp_in_c) > 0:
#         result = "{:.1f}".format(temp_in_c)
#     elif math.modf(temp_in_c) == 0:
#         result=temp_in_c

#     return(result)

# print(convert_f_to_c(64.4))


