# cyclist_planner 

## requirements
    Python3 (3.6 used)
    git
Here is how you can install python3 in your ubuntu machine. I am using Ubuntu 16.04 @https://docs.python-guide.org/starting/install3/linux/

    
## Step:1
Copy the link @https://github.com/jahangir091/cyclist_planner.git 
go to your terminal and just type:

    git clone https://github.com/jahangir091/cyclist_planner.git
and press enter button.
The code will be downloaded to your local machine.

## step:2
run the command below from your terminal:
    
    cd cyclist_planner
this will take you to the project directory.

## step:3
Here you can see some files as below

  - .gitignore
  - README.md
  - riders1.py
  - riders2.py
  - sample_data.csv
  - utils.py
  
here **riders1.py** is the solution of problem no: 1 and **riders2.py** is the solution of problem no: 2.

**sample_data.csv** is a headless **.csv** file. This file includes the sample data of 3 riders as stated in the problem no: 1.
The sample data is in the format below:

** ***no need to add header for csv file of sample data***

| Time elapsed in Seconds | Time elapsed in Minutes | Cyclist 1 (%FTP) | Cyclist 2 (%FTP)  | Cyclist 3 (%FTP) |
| ------ | ------ | ------ | ------ | ------ |
| 0 | 0 | 50 | 40 | 40 |
| 5 | 0 | 50 | 40 | 50 |
| 10 | 0 | 50 | 40 | 50 |
| 15 | 0 | 50 | 40 | 50 |
| 20 | 0 | 50 | 40 | 50 |
| 25 | 0 | 50 | 40 | 50 |
| 30 | 0 | 50 | 40 | 50 |
| 35 | 0 | 50 | 40 | 50 |
| 40 | 0 | 50 | 40 | 50 |
| 45 | 0 | 50 | 40 | 50 |
| 50 | 0 | 50 | 40 | 50 |
| 55 | 0 | 50 | 40 | 50 |
| 0 | 1 | 50 | 40 | 50 |



**utils.py** is a utility python file. In this file **planned data** and **truth tables** are defined by seperate 
list and dictionary.

## step: 4
Now type the command below in your terminal and press enter.

    python3 riders1.py
    
This will print the result for the problem no: 1 in your terminal.

This result is according to the sample data given to the **sample_data.csv** file.

## step:5
Now type the command below in your terminal:

    python3 riders2.py
    
This will print the result for problem no: 2 in your terminal.

***sample rides and capabilities for problem no: 2 are defined inside the riders2.py file itself with a list of tuples and with a dictionary of tuples accordingly***
