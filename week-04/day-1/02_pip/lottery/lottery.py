# Create a method that returns the five most frequent lottery number in a pretty table format
def five_most_frequent():
    import csv
    f = open('D:/greenfox/Greenfox/t2botond/week-04/day-1/02_pip/lottery/otos.csv')
    content = csv.reader(f)
    for row in content:
        print(row[4])

five_most_frequent()
