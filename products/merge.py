"""
Merges all the txt files in the directory into one txt file
"""
LAST_PART = 39

with open('db_all.txt', 'w') as outfile:
    for i in range(0, LAST_PART):
        with open("db_{}.txt".format(i + 1)) as infile:
            outfile.write(infile.read())
        