class CashOnCashROI:      
    def __init__(self, property_value = 0, rental_income =0, total_income= 0, total_expenses= 0, total_investment = 0, cash_flow = 0, annual_cashflow = 0):
        self.property_value = property_value
        self.rental_income = rental_income
        self.total_income = total_income        
        self.total_expenses = total_expenses 
        self.total_investment = total_investment
        self.cash_flow = cash_flow
        self.annual_cashflow = annual_cashflow



    def propertyValue(self, value = None):
        initial_value = input('How much will you pay for the property? \n')
        while initial_value.isdigit() == False:
            initial_value = input('Sorry, we need a number for property value? What is the proposed property value? \n')
        print(f"The current purchase value for the property is: {initial_value}")
        self.property_value = int(initial_value)



    def income(self):
    # Rental Income
        self.rental_income = input('What is the monthly base rental income you charge your tenants? \n')
        while self.rental_income.isdigit() == False:
            self.rental_income = input('Sorry, we need a number for base rental income? What is the base rental income? \n')
        other_income = input('Would you like to add income laundry, storage, or other? Yes/No \n')
        self.rental_income = int(self.rental_income)
        while other_income.lower() not in ["yes", "y", "no", "n", "quit"]:
    # Other types of income
            other_income = input(f'Sorry, "{other_income}" is not a valid input. Try "Yes" to add other types of income, "No" to keep rent income as only income or "Quit"\n')
        if other_income.lower() == "no" or other_income.lower() == "n":
            other_income_bool = False
            laundry, storage, other = "0", "0", "0"
    # Laundry income
        elif other_income.lower() == "yes" or other_income.lower() == "y":
            laundry = input(f'What is the monthly laundry income you charge your tenants? \n')
            while laundry.isdigit() == False:
                laundry = input(f'Sorry, we need a number for laundry income? What is the laundry income? \n')
    # Storage Income
            storage = input(f'What is the monthly storage income you charge your tenants? \n')
            while storage.isdigit() == False:
                storage = input(f'Sorry, we need a number for storage income? What is the storage income? \n')
    # Other types of income
            other = input(f'What is the monthly other income you charge your tenants? \n')
            while other.isdigit() == False:
                other = input(f'Sorry, we need a number for other income? What is the other income? \n')
            other_income_bool = True
    # Quit functionality
        elif other_income.lower() == "quit":
            print("Thanks for using the Return of Investment (ROI) Calculator! See you next time!")
    # Sum of other types income
        non_rental_income = int(laundry) + int(storage) + int(other)
        print(f'Your rental income: {self.rental_income}\n')
    # Bool to print out other types of income
        if other_income_bool == False:
            pass
        elif other_income_bool == True:
            print(f'Your laundry income: {laundry}\nYour storage income: {storage}\nYour other income: {other}\n')
        print(f'Total Income:{int(self.rental_income) + non_rental_income}')
        self.total_income = int(self.rental_income) + non_rental_income



    def expenses(self):
        print(f'The total income from the property calculated is: {self.total_income}')
    #Tax
        tax_mult = input('What is the percent tax on your area? remember to use percent or type "Value" to input a monthly nominal amount. \n You can go to https://www.propertyshark.com/mason/text/infopages/Property-Tax-Records.html for an estimate! \n')
        while tax_mult.lower() not in ["value", "v"] and tax_mult.isdigit() != True:
            tax_mult = input(f'Sorry, "{tax_mult}" is not a valid input. Input a percent value to be used as multiplier or type "value" to add a monthly nominal value.\n')
        if tax_mult.lower() == "value" or tax_mult.lower() == "v":
            tax = input('Please add a monthly nominal value of taxes for the property to be paid.\n')
        elif tax_mult.isdigit() == True:
            tax = int((float(tax_mult)/100) * self.rental_income)
        print(f'Your taxes to be paid are: {tax}')        
    #Insurance
        insurance = input('What is the monthly nominal value paid on insurance?. \n You can go to https://www.policygenius.com/homeowners-insurance/how-much-does-homeowners-insurance-cost/ for an estimate! \n')
        while insurance.isdigit() != True:
            insurance = input(f'Sorry, "{insurance}" is not a valid input. Input a nominal value for monthly insurance paid for the property.\n')
        print(f'Your insurance to be paid is: {insurance}')    
    #Mortgage
        mortgage = input('What is the monthly nominal value paid on mortgage?.\nYou can go to https://www.nerdwallet.com/mortgages/mortgage-rates for an estimate! \n')
        while mortgage.isdigit() != True:
            mortgage = input(f'Sorry, "{mortgage}" is not a valid input. Input a nominal value for monthly mortgage paid for the property.\n')
        print(f'Your mortgage to be paid is: {mortgage}')
    #Utilities
        utilities_option = input('Would you like to add utilities? Yes/No \n')
        while utilities_option.lower() not in ["yes", "y", "no", "n", "quit"]:
            utilities_option = input(f'Sorry, "{utilities_option}" is not a valid input. Try "Yes" to add utilities or "No" to skip utilities.\n')
        if utilities_option.lower() == "no" or utilities_option.lower() == "n":
            utilities_bool = False
            utilities_total = 0
        elif utilities_option.lower() == "yes" or utilities_option.lower() == "y":
            utilities_option2 = input('Would you like to add one ("One") amount for all or several ("Several") individual amounts for separate categories? One/Several \n')
            while utilities_option2.lower() not in ["one", "o", "1", "several", "s", "many", "separate"]:
                utilities_option2 = input(f'Sorry, "{utilities_option2}" is not a valid input. Type "One" to add one value for utilities or "Several" to add each utility separate.\n')
            if utilities_option2.lower() == "one" or utilities_option2.lower() == "o" or utilities_option2.lower() == "1":
                utilities_total = input("How much for monthly utilities would you be paying? \n") 
                utilities_bool = False
                while utilities_total.isdigit() == False:
                    utilities_total = input('Sorry, we need a number for the monthly utilities. What is the amount? \n')
            elif utilities_option2.lower() == "several" or utilities_option2.lower() == "s" or utilities_option2.lower() == "many" or utilities_option2.lower() == "separate":
                utilities_bool = True
    # Electricity bill
                electricity = input('What is the monthly electric bill amount for the property? \n')
                while electricity.isdigit() == False:
                    electricity = input('Sorry, we need a number for the monthly electric bill. What is the bill amount? \n')
    # Water Bill    
                water = input('What is the monthly water bill amount for the property? \n')
                while water.isdigit() == False:
                    water = input('Sorry, we need a number for the monthly water bill. What is the bill amount? \n')
    # gas Bill 
                gas = input('What is the monthly gas bill amount for the property? \n')
                while gas.isdigit() == False:
                    gas = input('Sorry, we need a number for the monthly gas bill. What is the bill amount? \n')
    # Garbage Bill     
                garbage = input('What is the monthly garbage bill amount for the property? \n')
                while garbage.isdigit() == False:
                    garbage = input('Sorry, we need a number for the monthly garbage bill. What is the bill amount? \n')
    # Sewer Bill     
                sewer = input('What is the monthly sewer bill amount for the property? \n')
                while sewer.isdigit() == False:
                    sewer = input('Sorry, we need a number for the monthly sewer bill. What is the bill amount? \n')
    # Other Bill     
                other_bill = input('What is the other monthly bill amount for the property? \n')
                while other_bill.isdigit() == False:
                    other_bill = input('Sorry, we need a number for the monthly electric bill. What is the bill amount? \n')

    #utilities Bool print
        if utilities_bool == False:
            print(f'Your monthly utilities to be paid is: {utilities_total}')
        if utilities_bool == True: 
            utilities_total = int(electricity) + int(water) + int(gas) + int(garbage) + int(sewer) + int(other_bill)
            print(f'Your monthly utilities to be paid is: {utilities_total}')
            print(f'Your electricity bill is: {electricity}\nYour water bill is: {water}\nYour gas bill is: {gas}\nYour garbage bill is: {garbage}\nYour sewer bill is: {sewer}\nYour other bills are: {other_bill}\n')
            
    #property_manager
        property_manager_mult = input('What is the monthly amount you pay your property manager? If this is a percent from the base rental income type "Percent".\nIf you manage your own property input 0 for this value.\n')
        while property_manager_mult.lower() not in ["percent", "p", "%"] and property_manager_mult.isdigit() != True:
            property_manager_mult = input(f'Sorry, "{property_manager_mult}" is not a valid input. Input a monthly nominal value paid to your property manager or type "percent" if the income is a percent of the base rent.\n')
        if property_manager_mult.isdigit() == True:
            property_manager = int(property_manager_mult)
        elif property_manager_mult.lower() == "percent" or property_manager_mult.lower() == "p" or property_manager_mult.lower() == "%":
            property_manager_mult = input("What is the percent of the base rental income given to the property manager?")
            property_manager = int((float(property_manager_mult)/100) * self.rental_income)

        print(f'Your property manager fees to be paid are: {property_manager}')        
        
    #optional expenses: home_owners_assoc, lawn_snow, vacancy, repairs, capEx, optional expenses
        expenses_optional_types = input('Would you like to add home owners association fees, lawn/snow services, vacancy fund,\nrepairs fund, capital expenditure fund, and other expenses? Yes/No \n')
        while expenses_optional_types.lower() not in ["yes", "y", "no", "n"]:
            expenses_optional_types = input(f'Sorry, "{expenses_optional_types}" is not a valid input. Try "Yes" to add additional expenses categories or "No" to skip additional expenses categories.\n')
        if expenses_optional_types.lower() == "no" or expenses_optional_types.lower() == "n":
            expenses_optional_bool = False
            optional_expenses_total = 0
        elif expenses_optional_types.lower() == "yes" or expenses_optional_types.lower() == "y":
            expenses_optional_bool = True
    # Home owners association fees
            home_owners_assoc = input('What is the monthly home owners association fees for the property? \n')
            while home_owners_assoc.isdigit() == False:
                home_owners_assoc = input('Sorry, we need a number for the monthly home owners association fees. What is the amount? \n')
    # Lawn/snow services   
            lawn_snow = input('What is the monthly Lawn/snow services bill amount for the property? \n')
            while lawn_snow.isdigit() == False:
                lawn_snow = input('Sorry, we need a number for the monthly Lawn/snow services bill. What is the amount? \n')
    # Vacancy fund 
            vacancy_mult = input("type the monthly vacancy fund amount for the property? or type 'Percent' to add a value based on the rental income.\nVacancy fund is a reserve fund ifor months when the property isn't being rented out\nSuggested estimates: 3-4% of base rental income\n")
            while vacancy_mult.lower() not in ["percent", "p", "%"] and vacancy_mult.isdigit() != True:
                vacancy_mult = input(f'Sorry, "{vacancy_mult}" is not a valid input. Input a monthly nominal value for the vacancy fund or type "percent" if the fund amount will be a percent of the base rent.\n')
            if vacancy_mult.isdigit() == True:
                vacancy = int(vacancy_mult)            
            elif vacancy_mult.lower() == "percent" or vacancy_mult.lower() == "p" or vacancy_mult.lower() == "%":
                vacancy_mult = input("What is the percent of the base rental to be saved for the vacancy fund?")
                vacancy = int((float(vacancy_mult)/100) * self.rental_income)

            print(f'Your expenses for the vacancy fund are: {vacancy}') 
    # Repairs fund     
            repairs = input("What is the monthly repairs fund amount for the property?\nRepair fund is a reserve fund for home repairs usually due to the tenant's fault.\nSuggested estimates: $100-$250 monthly\n")
            while repairs.isdigit() == False:
                repairs = input('Sorry, we need a number amount for the monthly repairs fund. What is the amount? \n')
    # Capital expenditure fund     
            capEx = input('What is the monthly capital expenditure fund amount for the property?\nCapital expenditure or CapEx is a reserve fund used for maintaining and repairing the property.\nSuggested estimates: $100-$250 monthly.\n')
            while capEx.isdigit() == False:
                capEx = input('Sorry, we need a number amount for the monthly capital expenditure fund. What is the amount? \n')
    #other expenses
            other_expenses = input('Do you have other expenses?\nAdd your other nominal expenses or add 0 if you do not have any.\n')
            while other_expenses.isdigit() == False:
                other_expenses = input('Sorry, we need a number amount for other expenses or 0 if none. What is the amount? \n')
    # Printing all expenses
        print(f'Your total calculated income from before: {self.total_income}\n\n') #from previous method
        print(f'Your taxes to be paid are: {tax}\nYour insurance to be paid is: {insurance}\nYour mortgage to be paid is: {mortgage}\n')
    # printing utilities again
        if utilities_bool == False:
            print(f'Your monthly utilities to be paid is: {utilities_total}')
        if utilities_bool == True: 
            utilities_total = int(electricity) + int(water) + int(gas) + int(garbage) + int(sewer) + int(other_bill)
            print(f'Your monthly utilities to be paid is: {utilities_total}')
            print(f'  The break down is as follows:\n    Your electricity bill is: {electricity}\n    Your water bill is: {water}\n    Your gas bill is: {gas}\n    Your garbage bill is: {garbage}\n    Your sewer bill is: {sewer}\n    Your other bills are: {other_bill}\n')
        print(f'Your property manager fees to be paid are: {property_manager}')    
    #Optional expenses Bool print
        if expenses_optional_bool == False:
            print(f'Your optional expenses are: {utilities_total}')
        if expenses_optional_bool == True: 
            optional_expenses_total = int(home_owners_assoc) + int(lawn_snow) + int(vacancy) + int(repairs) + int(capEx) + int(other_expenses)
            print(f'Your optional expenses are: {optional_expenses_total}')
            print(f'Your Homeowners association fees are: {home_owners_assoc}\nYour Lawn/snow services fees are: {lawn_snow}\nYour vacancy reserve amount is: {vacancy}\nYour repairs reserve amount is: {repairs}\nYour capital expenditure (CapEx) reserve amount is: {capEx}\nYour other expenses are: {other_expenses}\n')
        
        self.total_expenses = int(tax) + int(insurance) + int(mortgage) + utilities_total + int(property_manager) + optional_expenses_total
        print(f'\n\nTotal expenses:{self.total_expenses}')



    def cashFlow(self):
        cf_choice = input("Would you like to input total Income or total Expenses now? Yes/No\n\nThese two parameters are required to calculate Cash Flow\nIf input is 'Yes' the previous calculated values will overwrite.\nIf input is 'No' the previous calculated values will be unchanged.\n\n")
        while cf_choice.lower() not in ["yes", "y", "no", "n"]:
            cf_choice = input(f'Sorry, "{cf_choice}" is not a valid input. Try "Yes" to add/overwrite Income or Expenses or "No" to keep old values.\n')
        if cf_choice.lower() == "no" or cf_choice.lower() == "n":
            pass
        elif cf_choice.lower() == "yes" or cf_choice.lower() == "y":
    #Change total Income value
            cf_income_choice = input("Would you like to edit the total Income value? Yes/No\n")
            while cf_income_choice.lower() not in ["yes", "y", "no", "n"]:
                cf_income_choice = input(f'Sorry, "{cf_income_choice}" is not a valid input. Try "Yes" to add/overwrite Income or "No" to keep old value.\n')
            if cf_income_choice.lower() == "no" or cf_income_choice.lower() == "n":
                pass
            elif cf_income_choice.lower() == "yes" or cf_income_choice.lower() == "y":
                self.total_income = int(input('What is your total income?\n'))
                while type(self.total_income) != int:
                    self.total_income = input(f'Sorry, "{self.total_income}" is not a valid input. Try "Yes" to add/overwrite Income or "No" to keep old value.\n')
    #Change total Expenses value
            cf_expenses_choice = input("Would you like to edit the total Expenses value? Yes/No\n")
            while cf_expenses_choice.lower() not in ["yes", "y", "no", "n"]:
                cf_expenses_choice = input(f'Sorry, "{cf_expenses_choice}" is not a valid input. Try "Yes" to add/overwrite Expenses or "No" to keep old value.\n')
            if cf_expenses_choice.lower() == "no" or cf_expenses_choice.lower() == "n":
                pass
            elif cf_expenses_choice.lower() == "yes" or cf_expenses_choice.lower() == "y":
                self.total_expenses = int(input('What is your total Expenses?\n'))
                while type(self.total_expenses) != int:
                    self.total_expenses = input(f'Sorry, "{self.total_expenses}" is not a valid input. Try "Yes" to add/overwrite Expenses or "No" to keep old value.\n')
                                    
        if self.total_income == 0 or self.total_expenses == 0:
            print("Please make sure to first calculate Income and Expenses before calculating Cash Flow.")
        else:
            self.total_cash_flow = self.total_income - self.total_expenses
            print(f"Your total Income:{self.total_income}\nYour total expenses:{self.total_expenses}\n\nYour total Cash Flow is: {self.total_cash_flow}\n\nIf the total Cash Flow is a positive (+) value then that is your monthly profit.\n\nIf the total Cash Flow is a negative (-) value then that is how you will have in monthly losses\n")



    def cashOnCashROI(self):
        if self.total_income == 0 or self.total_expenses == 0:
            print("Please make sure to first calculate Cash Flow before calculating Cash on Cash ROI.")
        else:
            print(f"Your current purchase value for the property is: {self.property_value}\nHowever, current purchase value is not part of your investment and will not be used to calculate ROI.")
    #Down payment
            down_payment = input('What is your original down payment ammount for the property? \n')
            while down_payment.isdigit() == False:
                down_payment = input('Sorry, we need a number for original down payment. What is the amount? \n')
    #Closing costs
            closing_costs = input('What where your closing cost fees for the property?\nThis includes attorney and appraiser fees.\n')
            while closing_costs.isdigit() == False:
                closing_costs = input('Sorry, we need a number for closing cost fees. What is the amount? \n')
    #Rehabilitation Budget
            rehab_budget = input('What was the rehabilitation budget for the property?\nThis includes any immediate expenses on the house such as an outside paint job.')
            while rehab_budget.isdigit() == False:
                rehab_budget = input('Sorry, we need a number for rehabilitation budget. What is the amount? \n')
    #miscellaneous Budget
            misc_other = input('If you have a miscellaneous budget for the property, please add it here?\nThis includes any other fees or payments not added to the other categories.')
            while misc_other.isdigit() == False:
                misc_other = input('Sorry, we need a number for miscellaneous budget. What is the amount? \n')
    #total investment calculation
            self.total_investment = int(down_payment) + int(closing_costs) + int(rehab_budget) + int(misc_other)
    #Cash on Cash ROI
            self.annual_cashflow = (self.total_cash_flow * 12)
            cash_on_cash_roi_decimal = (self.annual_cashflow / self.total_investment) * 100
            self.cash_on_cash_roi = float("{:.2f}".format(cash_on_cash_roi_decimal))
            
            print(f"Your previously calculated monthly total Cash Flow is: {self.total_cash_flow}\nYour yearly calculated total Cash Flow is: {self.annual_cashflow}\n\nYour down payment is: {down_payment}\nYour closing costs are: {closing_costs}\nYour rehabilitation budget is: {rehab_budget}\nYour miscellaneous budget is: {misc_other}\n\nYour total investment on the property is: {self.total_investment}\n\n\nYour Cash on Cash ROI for this property is: {self.cash_on_cash_roi}%\nThis is a percent value of your annual return based on your initial investment.")
