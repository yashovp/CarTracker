#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File name : root.py
"""

def read_datafile(filename):
     """
    Reads information in the text file and stores each line of that information 
    as an array within an array. The array of arrays is returned.
    INPUT:
        Text file of data
    OUTPUT:
        array of arrays
     """
     file = open(filename,"r")
     text = file.read()   
     file.close()
        
     driving_data = []
     text=text.split("\n")

     for index in text:
            index = index.strip()
            driving_data.append((index).split(" "))
            
            
     return driving_data

def complie_output_data(driving_data):
     """
     Iterates through the array of arrays return by read_datafile() function. 
     Stores driver name as key in hash map, and then distance covered and 
     average speed are stored in a list which serves at the value of the hasmap.
     INPUT:
         array of arrays from read_datafile() fucntion.
     OUTPUT:
         returns hashmap where key is driver name, value is distance covered 
         and average speed
    
     """
     data_driver = {}
     
     for line in driving_data:
        if line[0] == "Driver":
            data_driver[line[1][:len(line[1])-1]] = [0,0]
            
        elif line[0] == "Trip":
            
            start = line[2]
            start = start.replace(':','')
            start = float(start[:2]) + float(start[2:])/60
            
                        
            end = line[3]
            end = end.replace(':','')
            end = float(end[:2])+ float(end[2:])/60
            end = float(end)
            
            distance = line[4].replace("\\",'')
            distance = float(distance)
            
            time = end - start 
            
            avg_speed = distance / time
            if avg_speed < 5 or avg_speed > 100:
                0
            elif data_driver[line[1]][0] == 0: 
                data_driver[line[1]] = [distance, avg_speed]
            
            else: 
                time_current = data_driver[line[1]][0]/data_driver[line[1]][1] 
                data_driver[line[1]][0] = data_driver[line[1]][0] + distance 
                data_driver[line[1]][1] = data_driver[line[1]][0] / (time + time_current)
                
     return data_driver



def data_ordering(final_data):
    """
    Iterates through hashmap returned by complie_output_data() function 
    and returns a hashmap where key is distance covered and value is an array of
    all drivers who've covered that distance.
    INPUT:
        hashmap from complie_output_data() function.
    OUTPUT:
        hashmap where key is distance covered and value is an array of drivers
        who've covered that distance.
    """
    print_data = {}
    
    for key in final_data:
        if final_data[key][0] not in print_data:
            print_data[final_data[key][0]] = [key]
        else:
            holder = print_data[final_data[key][0]]
            holder.append(key)
            holder.sort()
            print_data[final_data[key][0]] = holder

    return print_data

def cout_data(distance_map, final_data):
    """
    Purpose: A dedicated fucntion to control how the data is printed to the console.
    INPUT:
        hasmap from complie_output_data() function and hashmap from data_ordering() 
        function.
    OUTPUT:
        none; 
        just prints information from the hashmaps
    """
    list_distance  = list(distance_map.keys()) 
    list_distance.sort(reverse = True)
    for distance in list_distance:
        for driver in distance_map[distance]:
            str_distance = str(round(final_data[driver][0]))
            str_avg_speed = str(round(final_data[driver][1]))
            print(str(driver)+ ": "+ str_distance + " miles @ "+ str_avg_speed)

def main():
    file_name = "test.rtf"
    preliminary_data = read_datafile(file_name)
    final_data = complie_output_data(preliminary_data)
    distance_map = data_ordering(final_data)
    cout_data(distance_map,final_data)
    
main()