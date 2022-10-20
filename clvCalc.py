# Program to calculate CLV from NFL odds
# Issues when spread to closing line crosses 0 due to counting "down"

spread = 0
odds = 0
closingLine = 0
closingOdds = 0
adv = 0

# Ask for bet and closing line info

print('What is the spread of your bet?')
spread = float(input())

print('What are the odds of your bet?')
odds = int(input())

print('What is the closing line?')
closingLine = float(input())

print('What are the closing odds?')
closingOdds = int(input())

# print('Your bet was ' + str(spread) + ' at ' + str(odds))
# print('The closing line was ' + str(closingLine) + ' at ' + str(closingOdds))


# Convert odds to breakeven percentages

if odds < 0:
    betP = odds / (odds - 100)
else:
    betP = 100 / (odds +100)
    
if closingOdds < 0:
    closingP = closingOdds / (closingOdds - 100)
else:
    closingP = 100 / (closingOdds +100)

# Program works by counting down from higher number
# Setting variable "a" to higher absolute value

if abs(spread) > abs(closingLine):
    a = spread
    b = closingLine
else:
    a = closingLine
    b = spread

# Adds advantage from push data for crossing spreads

while a != b:
    if int(abs(a)) == 17:
        adv = adv + 0.046/2
    elif int(abs(a)) == 16:
        adv = adv + 0.035/2
    elif int(abs(a)) == 15:
        adv = adv + 0.015/2
    elif int(abs(a)) == 14:
        adv = adv + 0.049/2
    elif int(abs(a)) == 13:
        adv = adv + 0.013/2
    elif int(abs(a)) == 12:
        adv = adv + 0.004/2
    elif int(abs(a)) == 11:
        adv = adv + 0.022/2        
    elif int(abs(a)) == 10:
        adv = adv + 0.049/2
    elif int(abs(a)) == 9:
        adv = adv + 0.009/2
    elif int(abs(a)) == 8:
        adv = adv + 0.021/2
    elif int(abs(a)) == 7:
        adv = adv + 0.057/2
    elif int(abs(a)) == 6:
        adv = adv + 0.034/2
    elif int(abs(a)) == 5:
        adv = adv + 0.017/2
    elif int(abs(a)) == 4:
        adv = adv + 0.03/2
    elif int(abs(a)) == 3:
        adv = adv + 0.098/2
    elif int(abs(a)) == 2:
        adv = adv + 0.02/2
    elif int(abs(a)) == 1:
        adv = adv + 0.025/2

# Steps in 1/2 point until spread gets to closing line

    if a > b:
        a = a - 0.5
    else:
        a = a + 0.5

# Adds advantage to closing line precentage
    
if spread > closingLine:
    closingP = closingP + adv
else:
    closingP = closingP - adv

# Calculates CLV and prints results

clv = 100 * (closingP - betP) / betP

print('The CLV is ' + str(round(clv,1)) + '%')
