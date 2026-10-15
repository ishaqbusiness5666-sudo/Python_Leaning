import time
import sys
# stop code runing for these give second
# time.sleep(1)

print(time.time())  # prints the current time in seconds since the 1970 epoch

print(time.localtime().tm_hour ,time.localtime().tm_min ,time.localtime().tm_sec )  # prints the current local time as a struct_time object

print(time.ctime())  # prints the current time in seconds since the 1970 epoch as a float

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # prints the current local time in a formatted string

# sys.exit("Exiting the program")  # exits the program with a message
# print(sys.argv)

print(sys.version)  # prints the version of Python being used

print(sys.platform)  # prints the platform on which Python is running

