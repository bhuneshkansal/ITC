gross_inc = int(input("Enter your gross income(in digits only) = "))
dependants = int(input("No. of dependant members = "))
tax_inc = gross_inc-10000-(dependants*3000)
# Taxable income = Gross Income - Standard deduction - (Dependent deduction* No. of dependents)

Tax_Amount = 0.2*tax_inc
# Tax = Taxable Income * Tax Rate

print(Tax_Amount)
