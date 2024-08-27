import os
import pandas as pd
from duckduckgo_search import DDGS
# My Files
from functions.take_feedback import feedback

# Paths
CW_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_DIR = "Feedback data"
CSV_FILE = "Feedback.csv"

# Checking if the "Feedback data" directory exists
if not os.path.exists(os.path.join(CW_DIR, CSV_DIR)):
    os.mkdir(os.path.join(CW_DIR, CSV_DIR)) # Creating a new directory if it doesn't exists


# Taking the input from the user
while True:
    search_query = input("Question: ")
    # Input Validation
    if search_query == "":
        print("Field can't be empty")
    else:
        break # Breaking the loop if the field is filled

# Query configuration
results = DDGS().text(
    keywords=search_query,
    region='wt-wt',
    safesearch='off',
    timelimit='7d',
    max_results=10
)

# Crating the data frame
results_df = pd.DataFrame(results)

concatenated_body = ' '.join(results_df['body'].astype(str))

results = DDGS().chat("Answer this question: " + search_query + " with this information: " + concatenated_body, model='claude-3-haiku')

print(f"Answer: {results}")

# Taking the feedback from user
user_feedback = feedback()
print(f"Rating: {user_feedback['rating']}, Comment or suggestion: {user_feedback['suggestion']}")


# Creating a dataframe of user feedback
df_user_feedback = pd.DataFrame({
    "RATING": [user_feedback['rating']],
    "COMMENT OR SUGGESTION": [user_feedback['suggestion']],
})


# Validation for csv
if os.path.exists(os.path.join(CW_DIR, CSV_DIR, CSV_FILE)):
    # Appending in already created csv
    df_user_feedback.to_csv(os.path.join(CW_DIR, CSV_DIR, CSV_FILE), header=False, mode='a', index=False)
else:
    # Creating the new csv and writing the data (If it doesn't exists)
    df_user_feedback.to_csv(os.path.join(CW_DIR, CSV_DIR, CSV_FILE), index=False)
    