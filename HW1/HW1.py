# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '/home/ee2405/ee2405/HW1/108011244.csv'
data = []
target_data = [['C0A880', 'None'], #initiate the target data: set all TEMP(temperature) to 'None'
               ['C0F9A0', 'None'], 
               ['C0G640', 'None'], 
               ['C0R190', 'None'], 
               ['C0X260', 'None']] 
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Data process
for i in range(0, len(data)):                                        # one-by-one check the input data                                    

   temp_data = data[i]                                              

   for j in range(0, len(target_data)):                              # compare the raw data to out target data

      if temp_data['station_id'] == target_data[j][0]:               # Check1: 'station_id' should be what we care about

         if temp_data['TEMP'] != ('-99.000' or '-999.000'):          # Check2: 'TEMP' should not equal to '-99.000' or '-999.000'

            if target_data[j][1] == 'None':                          # Check3-1: If it is the first time getting the information corresponding to the 'station_id'?
               target_data[j][1] = float(temp_data['TEMP'])          #           Yes -> store the information
                                                                     #           No  -> goto Check3-2
            elif float(temp_data['TEMP']) > target_data[j][1]:       # Check3-2: If the new 'TEMP' is bigger than old one?
               target_data[j][1] = float(temp_data['TEMP'])          #           Yes -> update the target data ensuring the target data gets the temporary maximum 
                                                                     #           No  -> do nothing
            continue                                                 # since we have check the 'station_id' and 'TEMP' of this data,
                                                                     # we go to see next raw data right away

#=======================================

# Part. 4
#=======================================
# Print result
print(target_data)
#========================================