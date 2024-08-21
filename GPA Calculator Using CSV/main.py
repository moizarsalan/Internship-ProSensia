import csv

def gp(grade):
    points = {
        'A': 3.85,
        'B+': 3.65,
        'B': 3.45,
        'C+': 3.0,
        'C': 2.75,
        'D+': 2.0,
        'D': 1.8,
        'F': 0.0
    }
    return points.get(grade.upper(), 0.0)

def cal(grades, credits):
    total_points = 0
    total_credits = 0

    for grade, credit in zip(grades, credits):
        total_points += gp(grade) * credit
        total_credits += credit

    gpa = total_points / total_credits if total_credits != 0 else 0
    return round(gpa, 2)

def process_csv_file(file_path):
    with open(file_path, 'r') as input_file:
        reader = csv.reader(input_file)
        data = list(reader)

    data[0].append('GPA')

    students = {}
    for row in data[1:]:
        student_name, subject_name, grade, credit_hours = row
        credit_hours = float(credit_hours)
        if student_name not in students:
            students[student_name] = {'grades': [], 'credits': []}
        students[student_name]['grades'].append(grade)
        students[student_name]['credits'].append(credit_hours)

    for i, row in enumerate(data[1:]):
        student_name = row[0]
        gpa = cal(students[student_name]['grades'], students[student_name]['credits'])
        row.append(f'{gpa:.2f}')

    with open(file_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(data)

    print(f"Your result has been saved in the CSV file: {file_path}")

def main():
    while True:
        file_path = input("Enter the path to the CSV file: ")
        process_csv_file(file_path)
        choice = input("Do you want to process another file? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
