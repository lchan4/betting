# Program to calculate CLV from NFL odds
# Issues when spread to closing line crosses 0 due to counting "down"

# Function to convert odds to breakeven precent
def percent(odds):
    if odds < 0:
        return odds / (odds - 100)
    else:
        return 100 / (odds +100)

nflPush = [0, 0.025/2, 0.02/2, 0.098/2, 0.03/2, 0.017/2, 0.034/2, 0.057/2, 0.021/2, 0.009/2, 0.049/2, 0.022/2, 0.004/2, 0.013/2, 0.049/2, 0.015/2, 0.035/2, 0.046/2]

spread = 0
odds = 0
closingLine = 0
closingOdds = 0
adv = 0

# Ask for bet and closing line info

print('What is the spread of your bet?')
spread = float(input())

print('What are the odds of your bet?')
betOdds = int(input())

print('What is the closing line?')
closingLine = float(input())

print('What are the closing odds?')
closingOdds = int(input())

# print('Your bet was ' + str(spread) + ' at ' + str(betOdds))
# print('The closing line was ' + str(closingLine) + ' at ' + str(closingOdds))

# Convert odds to breakeven percentages

betP = percent(betOdds)
closingP = percent(closingOdds)

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
    adv += nflPush[int(abs(a))]

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
