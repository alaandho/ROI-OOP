class roiCalc():
    
    def __init__(self):
        self.investments = 0
        self.expenses = 0
        

    def monthlyExp(self):
        print('To calculate your ROI, enter your information below.')
        property_tax = int(input('Enter monthly Property Tax amount: $ '))
        property_ins = int(input('Enter monthly Property Insurance amount: $ '))
        property_manage = int(input('Enter monthly Property Management amount: $ '))
        capEx = int(input('Enter monthly CapEx amount: $ '))
        m_vacancy = int(input('Enter monthly vacancy amount: $ '))
        m_repairs = int(input('Enter monthly repairs amount: $ '))
        m_mortgage = int(input('Enter monthly mortgage amount: $ '))
        self.expenses = property_tax + property_ins + property_manage + capEx + m_vacancy + m_repairs + m_mortgage       
        


    def totalInvestments(self):
        print('To calculate your total investment, eneter your information below.')
        down_payment = int(input('Enter total down payment on house: $ '))
        closing_cost = int(input('Enter Closing Cost Estimate: $ '))
        rehab_budget = int(input('Enter total Rehab Budget: $ '))
        self.investments = down_payment + closing_cost + rehab_budget

    


    def totalCalc(self):
        rental_income = int(input('Enter monthly income: $ '))
        total_monthly_cashflow = rental_income - self.expenses
        print(f'Here is your estimated total monthly Cashflow based on your income and expenses: {total_monthly_cashflow}')
        roi_calc = ((total_monthly_cashflow * 12)/ self.investments) * 100
        print(f'Your yearly Return On Investment (ROI) for this property is: {roi_calc}')
        
     

    def runROI(self):
        print("Bigger Pockets is here to calculate your Rental Property ROI. Let's get started")
        while True: 
            r_roi = input('Your calculation has printed. Would you like to try another property? Enter yes or no ')
            if r_roi.lower() == 'no':
                print('Thank you, have a nice day!')
                break
            elif r_roi.lower() == 'yes':
                print("Let's get started!")
                self.monthlyExp()
                self.totalInvestments()
                self.totalCalc()
                
            else:
                print("Please enter valid response ")

runCalc = roiCalc()
runCalc.runROI()



        


    

        
        
        
        
