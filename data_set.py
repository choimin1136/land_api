import csv
from pathlib import Path





# Read CSV file and return JSON type
# apt
def read_apt(apt_path):
    data=[]
    with open(apt_path, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

# bus
def read_bus(bus_path):
    data=[]
    with open(bus_path, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

# d_center
def read_center(center_path):
    data=[]
    with open(center_path, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

# educational
def read_edu(edu_path):
    data=[]
    with open(edu_path, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

# eschool
def read_eschool(eschool_path):
    data=[]
    with open(eschool_path, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

# kindergarden
def read_kinder(kinder_path):
    data=[]
    with open(kinder_path, "r", encoding="") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

# mart
def read_mart(mart_path):
    data=[]
    with open(mart_path, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

# road
def read_road(road_path):
    data=[]
    with open(road_path, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

# train
def read_train(train_path):
    data=[]
    with open(train_path, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data