import csv
dataset1=[]
dataset2=[]
with open("final.csv","r")as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        dataset1.append(row)
with open("archive_dataset_sorted1.csv","r")as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        dataset2.append(row)
header1=dataset1[0]
planet_data_1=dataset1[1:]
header2=dataset2[0]
planet_data_2=dataset2[1:]
headers=header1+header2
planet_data=[]
for index,data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index]+(planet_data_2[index]))
with open("merge_data.csv","a+")as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)
