# Program to calculate CLV from NFL odds

# Function to convert odds to breakeven precent
def percent(odds):
    if odds < 0:
        return odds / (odds - 100)
    else:
        return 100 / (odds +100)

# Push Data from SBR

nflPush = [0, 0.025/2, 0.02/2, 0.098/2, 0.03/2, 0.017/2, 0.034/2, 0.057/2, 0.021/2, 0.009/2, 0.049/2, 0.022/2, 0.004/2, 0.013/2, 0.049/2, 0.015/2, 0.035/2, 0.046/2]

nbaPush = [0.0, 0.0227/2, 0.0403/2, 0.0383/2, 0.0348/2, 0.0437/2, 0.0416/2, 0.0411/2, 0.042/2, 0.0476/2, 0.0416/2, 0.0387/2, 0.0351/2, 0.0385/2, 0.0349/2, 0.033/2, 0.0499/2, 0.0299/2, 0.0341/2, 0.0333/2, 0.0227/2]

spread = 0
odds = 0
closingLine = 0
closingOdds = 0

while True:

    adv = 0
    sport = ""

    # Ask for sport, bet, and closing line info

    while sport != "b" or "f":

        print('What sport? n(f)l or n(b)a?' )
        sport = input()

        if sport == "b":
            pushData = nbaPush
            break
        elif sport == "f":
            pushData = nflPush
            break
        else:
            print("Please select the right sport.")
            continue

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

     # Checks if spread crosses zero to closing line

    if (a+0.1) / (b+0.1) < 0: # Add 0.1 to both values to avoid divide by 0 error
        while a != 0:

            adv += pushData[int(abs(a))]

            if a > 0: # Steps in 1/2 point until spread gets to closing line
                a = a - 0.5
            else:
                a = a + 0.5

        while b != 0:

            adv += pushData[int(abs(b))]

            if b > 0:
                b = b - 0.5
            else:
                b = b + 0.5

    else: # Adds advantage from push data for crossing spreads
        while a != b:

            adv += pushData[int(abs(a))]

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
