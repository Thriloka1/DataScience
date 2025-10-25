# read, clean, grouping, filtering and summarize data from a CSV student_exam_scores.csv (columns- student_id,hours_studied,sleep_hours,attendance_percent,previous_scores,exam_scor) also replce with zero in filtering with function call
import pandas as pd
def process_student_data(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Fill missing values with zero
    df_filled = df.fillna(0)

    # Group by 'attendance_percent' and calculate mean 'exam_score'
    grouped = df_filled.groupby('attendance_percent')['exam_score'].mean().reset_index()

    # Filter students who studied more than 5 hours and had more than 70% attendance
    filtered = df_filled[(df_filled['hours_studied'] > 5) & (df_filled['attendance_percent'] > 70)]

    #  Calculate average exam score
    average_exam_score = df_filled['exam_score'].mean()

    summary = {
        'mean': df.mean(),
        'median': df.median(),
        'std_dev': df.std(),
        'min': df.min(),
        'max': df.max(),
        'count': df.count()
    }

    return {
        'grouped_data': grouped,
        'filtered_data': filtered,
        'average_exam_score': average_exam_score,
        'summary': summary
    }
# Example usage
file_path = 'student_exam_scores.csv'

result = process_student_data(file_path)
print("Grouped Data:\n", result['grouped_data'])
print("\nFiltered Data:\n", result['filtered_data'])
print("\nAverage Exam Score:", result['average_exam_score'])
print("\nSummary Statistics:\n", result['summary'])
