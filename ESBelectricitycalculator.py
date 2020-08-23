"""
Ed MCGrath - ESB bill calculator
"""
#delcaring function for calculation
#USing 'A' as electric current is measured using ammeter 'ampere symbol = A'
def billCalculator(A):

#Using if statement to get the correct condition
    if (A <= 100):
        return A * 10;

    elif (A <= 200):
        return ((200 *10) + (A - 100) * 15);

    elif (A <= 300):
        return ((100 * 10) +
                (100 * 15) +
                (A - 200) * 20);
    elif (A > 300):

        return ((100 * 10) +
                (100 * 15) +
                (100 * 20) +
                (A - 300) * 25);
    return 0;


#Input set to integar
A = int(input("Please enter ampere units: "))

print("The result is :",billCalculator(A));