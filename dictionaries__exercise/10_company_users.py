company_reg = {}

while True:
    command = input()
    if command == "End":
        break
    company, emp_id = command.split(" -> ")
    if company not in company_reg.keys():
        company_reg[company] = []
    if emp_id not in company_reg[company]:
        company_reg[company].append(emp_id)

for company_name in company_reg.keys():
    print(f"{company_name}")
    for employee_id in company_reg[company_name]:
        print(f"-- {employee_id}")
