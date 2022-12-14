"""
Program Name: avg_grade.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    This script calculates the average of 3 students' grades.
Dates: 2022-08-30 - File created.
"""

# Initialize variables
score1 = 45
score2 = 74
score3 = 63

# Average and round the scores
score_avg = (score1 + score2 + score3) / 3
score_avg = round(score_avg, 1)

# Print the average to the user
print(f"The average score is {score_avg}.")
