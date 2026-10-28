import pandas as pd
import matplotlib.pyplot as plt

# Read employee data
df = pd.read_csv("employee.csv")

# Display employee details
print("Employee Details:")
print(df[["Name", "Department", "Salary"]])

# Calculate average salary by department
avg_salary = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary by Department:")
print(avg_salary)

# Plot average salary
avg_salary.plot(kind="bar", color="skyblue")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.show()
