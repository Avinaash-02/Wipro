def calculate_salary(basic):
    if basic <= 20000:
        hra = basic * 0.20
        da = basic * 0.80
        tax = basic * 0.05
    elif basic <= 50000:
        hra = basic * 0.25
        da = basic * 0.90
        tax = basic * 0.10
    else:
        hra = basic * 0.30
        da = basic * 1.00
        tax = basic * 0.15

    gross = basic + hra + da
    net_salary = gross - tax

    return hra, da, tax, net_salary

try:
    with open("employee_data.txt", "r") as infile, open("salary_slips.txt", "w") as outfile:
        for line in infile:
            name, basic = line.strip().split(",")
            basic = float(basic)

            hra, da, tax, net_salary = calculate_salary(basic)

            outfile.write("Employee Salary Slip\n")
            outfile.write(f"Name        : {name}\n")
            outfile.write(f"Basic Salary: {basic}\n")
            outfile.write(f"HRA         : {hra}\n")
            outfile.write(f"DA          : {da}\n")
            outfile.write(f"Tax         : {tax}\n")
            outfile.write(f"Net Salary  : {net_salary}\n")
            outfile.write("-" * 30 + "\n")

except:
    pass
