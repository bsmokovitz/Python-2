class StoreItem:
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.item_id} {self.name} {self.price} {self.quantity}"
    
class Inventory:
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item_id):
        for item in self.inventory:
            if item.item_id == item_id:
                # subtracts 1 from quantity
                self.inventory[self.inventory.index(item)].quantity -= 1
                return True
        return False

    def __str__(self):
        return "\n".join([str(item) for item in self.inventory])
    
class Employee:
    def __init__(self, employee_number, name, date_of_hire, job_description, department, salary):
        self.employee_number = employee_number
        self.name = name
        self.date_of_hire = date_of_hire
        self.job_description = job_description
        self.department = department
        self.salary = salary

    def __str__(self):
        return f"{self.employee_number} {self.name} {self.date_of_hire} {self.job_description} {self.department} {self.salary}"
    
class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        return "\n".join([str(employee) for employee in self.employees])
    
inventory = Inventory()
inventory.add_item(StoreItem(1, "Crans", 0.99, 500))
inventory.add_item(StoreItem(2, "Pen", 1.99, 200))
inventory.add_item(StoreItem(3, "Pencil", 0.59, 100))
print(inventory)

inventory.remove_item(2)
print(inventory)

employee_manager = EmployeeManager()
employee_manager.add_employee(Employee(1, "Jack Kelly", "01/01/2001", "Cashier", "Front End", 2000))
employee_manager.add_employee(Employee(2, "Mac Miller", "01/01/2001", "Manager", "Management", 5000))
print(employee_manager.list_employees())