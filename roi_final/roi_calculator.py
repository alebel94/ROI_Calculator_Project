from .modules import CashOnCashROI
## RUN THIS ONE
def calculator():
    
    rental = CashOnCashROI()
    
    print('Welcome to the Return of Investment (ROI) Calculator! \nPlease do not use commas or spaces when typing numbers.\n')
    rental.propertyValue()
    while True:
        choice = input('Would you like to calculate Income ("I"), Expenses ("E"), Cash Flow ("CF"), or Cash on Cash ROI ("ROI")? \nYou can also "Quit" to stop the program or "Value" to change the property value.\n')
        if choice.lower() not in ["i", "e", "cf", "roi", "quit", "value"]:
            print(f'Sorry, {choice} is not a valid input. Try "I" for Income, "E" for Expenses, "CF" for Cash Flow, "ROI" for Cash on Cash ROI, or "Quit" for Quit')
        elif choice.lower() == "i":
            print('You have selected Income. Here we will add all income from your rental property.\n')
            rental.income()
        elif choice.lower() == "e":
            print('You have selected Expenses. Here we will add all expense costs from your rental property.\n')
            rental.expenses()
        elif choice.lower() == "cf":
            print('You have selected Cash Flow. Here we will subtract your total monthly income from your monthly expenses.\n')
            rental.cashFlow()
        elif choice.lower() == "roi":
            print('You have selected Cash on Cash ROI. Here we will calculate your annual cash flow divided by your total investment.\nSimply put, it is a percentage of your annual return based on your initial investment.\n')
            rental.cashOnCashROI()
        elif choice.lower() == "value":
            rental.propertyValue()
        elif choice.lower() == "quit":
            print("Thanks for using the Return of Investment (ROI) Calculator! See you next time!\n")
            break
        
calculator()