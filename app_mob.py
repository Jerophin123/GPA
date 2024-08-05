import csv
import os
from flask import Flask, render_template, request, redirect, url_for
from openpyxl import Workbook

app = Flask(__name__)

# Function to calculate GPA
def calculate_gpa(subjects):
    total_points = 0
    total_credits = 0
    results = []

    for subject in subjects:
        subject_code = subject['subject_code']
        subject_name = subject['subject_name']
        grade_point = float(subject['grade_point'])
        credit = float(subject['credit'])

        total_points += grade_point * credit
        total_credits += credit

        results.append({
            'subject_code': subject_code,
            'subject_name': subject_name,
            'grade_point': grade_point,
            'credit': credit
        })

    gpa = total_points / total_credits if total_credits != 0 else 0
    return gpa, results

# Function to save results to CSV
def save_csv(student_name, gpa, results):
    csv_dir = os.path.join(os.getcwd(), 'csv_files')
    if not os.path.exists(csv_dir):
        os.makedirs(csv_dir)

    csv_filename = f"{student_name}_gpa.csv"
    csv_filepath = os.path.join(csv_dir, csv_filename)
    with open(csv_filepath, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Student Name:", student_name])
        writer.writerow(["GPA:", gpa])
        writer.writerow([])  # Empty row for separation
        writer.writerow(["Subject Code", "Subject Name", "Grade Point", "Credit"])
        for result in results:
            writer.writerow([
                result['subject_code'],
                result['subject_name'],
                result['grade_point'],
                result['credit']
            ])

# Function to save results to XLSX
def save_xlsx(student_name, gpa, results):
    xlsx_dir = os.path.join(os.getcwd(), 'xlsx_files')
    if not os.path.exists(xlsx_dir):
        os.makedirs(xlsx_dir)

    xlsx_filename = f"{student_name}_gpa.xlsx"
    xlsx_filepath = os.path.join(xlsx_dir, xlsx_filename)
    workbook = Workbook()
    sheet = workbook.active

    sheet.append(["Student Name:", student_name])
    sheet.append(["GPA:", gpa])
    sheet.append([])  # Empty row for separation
    sheet.append(["Subject Code", "Subject Name", "Grade Point", "Credit"])
    for result in results:
        sheet.append([
            result['subject_code'],
            result['subject_name'],
            result['grade_point'],
            result['credit']
        ])

    workbook.save(xlsx_filepath)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and save CSV and XLSX
@app.route('/calculate', methods=['POST'])
def calculate_and_save():
    student_name = request.form['student_name']
    num_subjects = int(request.form['num_subjects'])
    subjects = []

    for i in range(num_subjects):
        try:
            subject = {
                'subject_code': request.form[f'subject_code_{i}'],
                'subject_name': request.form[f'subject_name_{i}'],
                'grade_point': request.form[f'grade_point_{i}'],
                'credit': request.form[f'credit_{i}']
            }
            subjects.append(subject)
        except KeyError as e:
            return f"Missing form field: {str(e)}"

    gpa, results = calculate_gpa(subjects)

    # Save CSV and XLSX files
    save_csv(student_name, gpa, results)
    save_xlsx(student_name, gpa, results)

    return redirect(url_for('view_results', student_name=student_name))

# Route to view results
@app.route('/view_results', methods=['GET'])
def view_results():
    student_name = request.args.get('student_name')
    csv_filename = f"{student_name}_gpa.csv"
    csv_dir = os.path.join(os.getcwd(), 'csv_files')
    csv_filepath = os.path.join(csv_dir, csv_filename)
    results = []

    with open(csv_filepath, 'r') as csv_file:
        reader = csv.reader(csv_file)
        # Skip the first row (header)
        next(reader)
        gpa = next(reader)[1]
        # Skip the empty row
        next(reader)
        for row in reader:
            results.append({
                'subject_code': row[0],
                'subject_name': row[1],
                'grade_point': row[2],
                'credit': row[3]
            })

    return render_template('view_results.html', results=results, gpa=gpa)

if __name__ == '__main__':
    app.run(debug=True)

