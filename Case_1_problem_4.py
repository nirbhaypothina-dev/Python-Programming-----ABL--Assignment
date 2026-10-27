# Case 1 - Problem 4: Employee Payroll and Deduction Analysis

emp_id = input("Enter Employee ID: ")
emp_name = input("Enter Employee Name: ")
basic = float(input("Enter Basic Pay: "))
ot_hours = int(input("Enter Overtime Hours: "))
incentive = float(input("Enter Incentive Amount: "))

if basic < 0 or ot_hours < 0 or incentive < 0:
    print("Invalid input values")
else:
    hra = basic * 0.20
    da = basic * 0.15
    ot_pay = ot_hours * 250

    gross = basic + hra + da + ot_pay + incentive
    pf = basic * 0.12

    if gross <= 30000:
        tax = 0
    elif gross <= 60000:
        tax = gross * 0.05
    else:
        tax = gross * 0.10

    total_ded = pf + tax
    net_salary = gross - total_ded

    print("--- Salary Statement ---")
    print("Employee ID:", emp_id)
    print("Employee Name:", emp_name)
    print("Basic Pay:", basic)
    print("HRA:", hra)
    print("DA:", da)
    print("Overtime Pay:", ot_pay)
    print("Incentive:", incentive)
    print("Gross Salary:", gross)
    print("PF Deduction:", pf)
    print("Tax Deduction:", tax)
    print("Total Deductions:", total_ded)
    print("Net Salary:", net_salary)
