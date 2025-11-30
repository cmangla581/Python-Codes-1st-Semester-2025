class Employment:
    def __init__(self, employee_id, employee_name):
        self.employee_id = employee_id
        self.employee_name = employee_name

    def display_details(self):
        print("Employee ID:", self.employee_id)
        print("Employee Name:", self.employee_name)


# Create an object of the class
emp1 = Employment(101, "John Doe")

# Display employee details
emp1.display_details()
