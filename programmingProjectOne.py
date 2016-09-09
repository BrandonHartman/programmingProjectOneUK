# Programming Project One
# Brandon Hartman
# September 9th, 2016
# ----------------------------------------------------------------------
# Writing a program that inputs the users amount of a purchase and then
# converts the input to having taxes at certain percentages given
# (State tax is calculated at 5 percent and the county tax is 2.5). We will
# need the program to display the output as a certain variable outcome and
# the output shall be formatted to two decimal points as well of having aligned
# formatting.
# ----------------------------------------------------------------------

# We will be asking the user for input and assigning it to amountOfPurchase
# This action will be using float to receive the decimal amount
amountOfPurchase = float(input("What is the purchased amount of your item? "))

# Takes the information from the user and will format and print the amount.
# Format output amounts to 2 decimal points.

print(format("Amount of purchase: ", "<15s"),
      format(amountOfPurchase, '>10,.2f'))

# The program will multiply the amountOfPurchase with 0.05. This will be assigned to
# the variable stateTaxes. Assign float to receive the decimal number.
stateTaxes = float(0.05 * amountOfPurchase)

# This statement prints the State tax and the amount of taxes it receives for
# purchased amount. Format is aligned so that the words and numbers connect with
# correct corresponding variables.
print(format("State tax: ", "<15s"),
      format(stateTaxes, '>15,.2f'))

# The program will multiply the amountOfPurchase with 0.025. This will be assigned to
# the variable countyTaxes. Assign float to receive the decimal number.
countyTaxes = float(0.025 * amountOfPurchase)

# This statement prints the County tax and the amount of taxes it receives for
# purchased amount. Format is aligned so that the words and numbers connect with
# correct corresponding variables.
print(format("County tax: ", "<15s"),
      format(countyTaxes, '>15,.2f'))

# This final statement adds all the variables together for the final total
# amount. Format is aligned so that the words and numbers connect with
# correct corresponding variables.
totalSalesAmount = float(amountOfPurchase + stateTaxes + countyTaxes)

print(format("Total of sale: ", "<15s"),
      format(totalSalesAmount, '>15,.2f'))
