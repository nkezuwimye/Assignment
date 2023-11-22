def enter_employee_info():
  num_employees = int(input("Enter the number of employees to record: "))
  employee_list = []

  for i in range(num_employees):
      print(f"\nEnter details for Employee {i + 1}:")
      employee = {}
      employee["Employee ID"] = input("Employee ID: ")
      employee["First Name"] = input("First Name: ")
      employee["Last Name"] = input("Last Name: ")
      employee["Date of Birth"] = input("Date of Birth (YYYY-MM-DD): ")
      employee["Sex"] = input("Sex: ")
      employee["Year of Recruitment"] = input("Year of Recruitment: ")
      employee["Salary"] = float(input("Salary: "))
      employee_list.append(employee)

  return employee_list

def display_employees(employee_list):
  print("\nList of Entered Employees:")
  for index, employee in enumerate(employee_list, start=1):
      print(f"\nEmployee {index}:")
      print("Employee ID:", employee["Employee ID"])
      print("Name:", employee["First Name"], employee["Last Name"])
      print("Date of Birth:", employee["Date of Birth"])
      print("Sex:", employee["Sex"])
      print("Year of Recruitment:", employee["Year of Recruitment"])
      print("Salary:", employee["Salary"])

def main():
  employees = enter_employee_info()
  display_employees(employees)

if __name__ == "__main__":
  main()
