counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

print("----------------------------------------")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

print("----------------------------------------")

for county in counties_dict.keys():
    print(county)

print("----------------------------------------")

for voters in counties_dict.values():
    print(voters)

print("----------------------------------------")

for county in counties_dict:
    print(counties_dict[county])

print("----------------------------------------")

for county in counties_dict:
    print(counties_dict.get(county))

print("----------------------------------------")

for county, voters in counties_dict.items():
   print(str(county) + " county has " + str(voters) + " registered voters")

print("----------------------------------------")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

print("----------------------------------------")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

print("----------------------------------------")

# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)

import datetime as dt
now = dt.datetime.now()
print(f"The time right now is {now}") 

print("----------------------------------------")

## assign a varibale for the file to load and the path
file_to_load = 'Resources/election_results.csv'

##open the election reseults and read the file 
with open(file_to_load) as election_data:
        #to do: perform analysis
        print(election_data) #do this instead of opening and closing the data
##open the eleciton results and read the file.
#election_data = open(file_to_load,'r')
## to do : perform analysis

##close the file
#election_data.close() #THIS STEP IS VERY IMPORTANT, if you don't do it right you could lose data, and that would be BAD!

print("----------------------------------------")

import csv
import os
#assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#open the election results and read the file.
with open(file_to_load) as election_data:
        #print the file object
        print(election_data)

print("----------------------------------------")

#create a filename variable to a direct or iindirect path to the file.
file_to_save = os.path.join ("analysis", "election_analysis.txt")

#using the open() funciton witht he "w" mode we will write data to the file.
open(file_to_save, "w")
