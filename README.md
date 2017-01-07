Problem Definition
--------------------------------------------
Write a program that inputs the users amount of a purchase and then convert the input to having taxes at certain percentages given (State tax is calculated at 5 percent and the county tax is 2.5). We will need the program to display the output as a certain variable outcome and the output will be formatted to two decimal points away and also having aligned formatting for corresponding variables.

Analysis
---------------------------------------------
We have picked Python as our language for this project because we are currently learning the programming language in class... The program will start off with the user entering the purchase amount so will need a float variable and an input function to receive the information. The variable that the program will be using will be called amountOfPurchase. Also, the program will be formatting these variables with format() so that they are align together to the corresponding numbers that it is with. The String constant of “Amount of purchase: “will be moved “>15s” (‘s’ used for strings) for alignment and the float will be measured ’10.2f’ (‘f’ used for float) to receive the two decimals points away.

After the input of that section; it will lead into the calculation towards the State and County taxes.
StateTaxes will be calculated as 0.05 multiplied by the amountOfPurchase. The program will calculate 
it as a decimal point by using the float() function. Underneath will contain the same formatting functions.
The program needs to be printed and formatted into a neatly function. The string constant will contain “State tax:”
will be “<15s” and two decimal points away for the floating number it will output from the user. CountyTaxes will be
calculated by 0.025 multiplied by the amountOfPurchase. The program will run the same alignment for the formatting 
towards the string and float constants and will be aligned to the other functions as well.

The final performance of this program will be calculating the totalSalesAmount. Creating the variable and assigning
a float function to add the amountOfPurchase, stateTax and countyTax. After assignment, the program will print and 
format the string constant “Total of sale:” to “<15s”. Afterwards, it will take the total amount for that function 
and print and format it two decimal points away using ‘>15.2f”.

Design
-----------------------------------------
Here is the Pseudocode: 
•	Input “What is the purchase amount of your item? “
•	Assign that to amountOfPurchase
•	Print “Amount of purchase: “and receive the users amount
•	Format both string and float functions to the user needs
•	Multiply 0.05 to amountOfPurchase 
•	Assign that to stateTaxes
•	Print “State tax:” and compute the equation
•	Format stateTaxes towards the string and float functions needed
•	Multiply 0.025 to amountOfPurchase
•	Assign it to countyTaxes
•	Print “County tax:” and compute the equation
•	Format countyTaxes towards the string and float functions needed
•	 Add all three variables (AmountofPurchase, countyTaxes, stateTaxes.
•	Assign it to totalSalesAmount
•	Print and format “Total of sale:” and compute the equation
•	Format both string and float functions to the user needs.
•	Run the program and receive your final amount!

Implementation
-------------------------------------------
The development environment used for this program was PyCharm CE. I programmed it on my Mac pro using the OS Operating
System. I had a couple unusual situations happen while developing this program. I ran into a problem formatting the correct
alignment for the strings and floats to connect. It started acting strange when I decided to put backspaces to add a new
format. After some measuring and fiddling with the code…It finally aligned up perfectly! The main concern for me in this
project was fixing the format for it to measure correctly.

