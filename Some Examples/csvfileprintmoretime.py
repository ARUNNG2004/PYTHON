B=int(input("Enter the number you want"))
import csv
a=0
while a<=B:

    fields=['ARUN']

    with open(r'spam', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        a+=1
