def datasort():
    all_employee = []
    with open("employee.txt", "r") as data : 
        for line in data:
            cleaned = line.replace("hours","").strip()
            sorted = cleaned.split(",")
            name = sorted[0].strip()
            hours = float(sorted[1])            
            emp_dict = {"name": name, "hours" : hours}
            all_employee.append(emp_dict)
    return all_employee


print(datasort())
