def pyramid(rows):
    for row in range(1, rows+1):
        yield '*' * (row)
        
for line in pyramid(5):
    print(line)
