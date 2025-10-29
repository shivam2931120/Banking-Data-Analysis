# 🏦 Banking Data Analysis (EDA with Python)
📌 Project Overview:
This project performs Exploratory Data Analysis (EDA) on a banking dataset to understand customer demographics, financial behavior, and factors influencing term deposit subscriptions.
The analysis focuses on uncovering insights related to age, job type, balance, education, loans, contact type, and campaign success.

🎯 Objectives:
Explore and summarize the dataset structure.
Identify data distributions and outliers.
Analyze customer demographics such as age, job, marital status, education.
Study financial indicators like balance, loan, housing loan.
Visualize key relationships between numerical variables.
Generate a correlation heatmap to identify patterns.

🧰 Technologies Used:
Python 3.x
Pandas – Data manipulation and analysis
NumPy – Numerical computations
Matplotlib – Data visualization
Seaborn – Statistical data visualization

📂 Dataset:
The dataset used in this project is stored as banking_data.csv.
It contains information about bank clients, their demographics, financial data, and whether they subscribed to a term deposit.

Example Columns:
| Column Name      | Description                                           |
| ---------------- | ----------------------------------------------------- |
| `age`            | Age of the client                                     |
| `job`            | Type of job (admin, technician, etc.)                 |
| `marital_status` | Marital status (married, single, divorced)            |
| `education`      | Education level                                       |
| `default`        | Has credit in default (yes/no)                        |
| `balance`        | Average yearly balance in euros                       |
| `housing`        | Has a housing loan (yes/no)                           |
| `loan`           | Has a personal loan (yes/no)                          |
| `contact`        | Communication type                                    |
| `day`, `month`   | Last contact day and month                            |
| `duration`       | Duration of last contact (in seconds)                 |
| `poutcome`       | Outcome of the previous marketing campaign            |
| `y`              | Has the client subscribed to a term deposit? (yes/no) |

📊 Analysis Performed

Univariate Analysis:
Frequency distributions and unique value counts for each column.
Box plot and count plot for age.
Value counts for categorical variables (job, education, marital_status, etc.).

Bivariate Analysis:
Correlation matrix and heatmap for numerical columns.
Comparison between financial and demographic factors.

Key Insights:
Distribution of client age groups.
Common job categories among subscribers.
Proportion of clients with existing loans or defaults.
Correlation between age, balance, and campaign success.
