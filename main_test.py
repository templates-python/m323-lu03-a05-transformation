import main

def test_increase_salary_by_department():
    employees = [
        {'name': 'Alice', 'age': 30, 'salary': 5000, 'department': 'HR'},
        {'name': 'Bob', 'age': 40, 'salary': 6000, 'department': 'IT'}
    ]
    updated_employees = main.increase_salary_by_department(employees, 'IT', 10)

    assert updated_employees[1]['salary'] == 6600, f"Expected 6600, got {updated_employees[1]['salary']}"
    assert updated_employees[0]['salary'] == 5000, f"Expected 5000, got {updated_employees[0]['salary']}"


def test_convert_names_to_uppercase():
    employees = [
        {'name': 'Alice', 'age': 30, 'salary': 5000, 'department': 'HR'},
        {'name': 'Bob', 'age': 40, 'salary': 6000, 'department': 'IT'}
    ]
    updated_employees = main.convert_names_to_uppercase(employees)

    assert updated_employees[0]['name'] == 'ALICE', f"Expected 'ALICE', got {updated_employees[0]['name']}"
    assert updated_employees[1]['name'] == 'BOB', f"Expected 'BOB', got {updated_employees[1]['name']}"


def test_transform_employee_data():
    employees = [
        {'name': 'Alice', 'age': 30, 'salary': 5000, 'department': 'HR'},
        {'name': 'Bob', 'age': 40, 'salary': 6000, 'department': 'IT'}
    ]

    def dummy_transformation(employees):
        return employees

    transformed_employees = main.transform_employee_data(employees, dummy_transformation)

    assert transformed_employees == employees, f"Expected {employees}, got {transformed_employees}"


def test_transform_employee_data():
    employees = [
        {'name': 'Alice', 'age': 30, 'salary': 5000, 'department': 'HR'},
        {'name': 'Bob', 'age': 40, 'salary': 6000, 'department': 'IT'}
    ]

    def dummy_transformation(employees):
        return employees

    transformed_employees = main.transform_employee_data(employees, dummy_transformation)

    assert transformed_employees == employees, f"Expected {employees}, got {transformed_employees}"


def test_transform_employee_data_with_args():
    employees = [
        {'name': 'Alice', 'age': 30, 'salary': 5000, 'department': 'HR'},
        {'name': 'Bob', 'age': 40, 'salary': 6000, 'department': 'IT'}
    ]

    expected_employees = [
        {'name': 'Alice', 'age': 30, 'salary': 5000, 'department': 'HR'},
        {'name': 'Bob', 'age': 40, 'salary': 6600, 'department': 'IT'}  # Salary increased by 10%
    ]

    transformed_employees = main.transform_employee_data(employees, main.increase_salary_by_department, 'IT', 10)

    assert transformed_employees == expected_employees, f"Expected {expected_employees}, got {transformed_employees}"
