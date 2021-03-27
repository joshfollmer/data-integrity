import csv

with open('import.csv') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    #lists the rows as a list
    rows = list(rows)
    #defines the top row as the headers
    header = rows[0]
    #the counter has to start at 2 so it matches the rows
    counter = 2
    #loops through rows 1 and 604, i stopped at 604 because they are all wrong already
    for row in rows[1:604]:
        #checks rows ab and c and d combined
        if row[27] != 'C' + row[2] + '-' + row[3]:
            #if it finds a difference, prints the course title and line 
            print(f'error with {row[2]} - {row[3]} on row {counter}')
        #this checks columns d and w, finds one on 595
        if row[3] != row[22]:
            print(f'error with {row[2]} - {row[3]} on row {counter}')
        #checks c and v, needs to remove the c from the course sections in v, doesnt find any errors
        if row[2] != row[21][1:]:
            print(f'error with {row[2]} - {row[3]} on row {counter}')
        counter += 1