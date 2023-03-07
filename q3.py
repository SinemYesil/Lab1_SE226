stdName=input('Enter the student name, please:')
labGrd=float(input('Enter the lab grade, please:'))
midGrd=float(input('Enter the midterm grade, please:'))
finalGrd=float(input('Enter the final grade, please:'))

print('Name', stdName)
print('Lab',labGrd)
print('Midterm',midGrd)
print('Final',finalGrd)

lastScore=labGrd*0.25+ midGrd*0.35+finalGrd*0.4

print('Last Score:', lastScore)