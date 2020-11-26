import csv
import json
import pandas as pd

emps = []
emps_json = []

def read_records():
    global emps
    with open("emp.csv") as f:
        rows = csv.DictReader(f)
        emps = [x for x in rows]

    global emps_json
    with open('emp.json') as emp_json_data_file:
        emp_json_data = json.load(emp_json_data_file)
        emps_json = [y for y in emp_json_data]

def correct_types():
    for e in emps:
        e['age'] = int(e['age'])

# average employee age
def find_average_age():
    avg_age = sum([x['age'] for x in emps]) / len(emps)
    return avg_age

# TODO:: implement this
def find_average_age_for_dept_through_csv(dept):
     dept_of_emps = []
     avg_age_departmentwise = 0
     for x in emps:
         if x['dept'] == dept:
            dept_of_emps.append(x)
            avg_age_departmentwise = (sum(s['age'] for s in dept_of_emps))/len(dept_of_emps)
     return avg_age_departmentwise
# df = pd.DataFrame(emps)
# return df.groupby(['dept']).mean()
def find_average_age_for_dept_through_json(dept):
     df = pd.DataFrame(emps_json)
     return df.groupby(['dept']).mean()
def main():
    read_records()
    correct_types()
    print("Average emp age is:", find_average_age())
    print("Average emp age for departments respectively through CSV :", find_average_age_for_dept_through_csv("d1"))
    print("Average emp age for departments respectively through CSV :", find_average_age_for_dept_through_csv("d2"))
    # TODO: Do same thing with json file instead of csv file
    print("Average emp age for departments respectively through Json:", find_average_age_for_dept_through_json("d"))

if __name__ == "__main__":
    main()
