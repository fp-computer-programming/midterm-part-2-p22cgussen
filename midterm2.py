# Author: CCG 12/14/21

velo1 = input("Enter the initial velocity: ")
velo2 = input("Enter the final velocity: ")
time = input("Enter the time: ")

acceleration = (int(velo2) - int(velo1)) / int(time)

print("When the initial velocity is {0}m/s, the final velocity is {1}m/s, and the time is {2}s, the average acceleration is {3}m/s^2".format(velo1,velo2,time,acceleration))
