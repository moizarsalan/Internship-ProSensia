import os
import pandas as pd

# Paths
CW_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_DIR = "Feedback data"
CSV_FILE = "Feedback.csv"

# Function to calculate the stats of feedback
def calculate_feedback_stats():
    # Validation for Paths and files
    if os.path.exists(os.path.join(CW_DIR, CSV_DIR, CSV_FILE)):
        # Reading the csv data
        df = pd.read_csv(os.path.join(CW_DIR, CSV_DIR, CSV_FILE))
        # Validation for csv data
        if not df.empty:
            avg_rating = df["RATING"].mean()
            comments_list = df["COMMENT OR SUGGESTION"].tolist() # Converting the df to list of comments
            rating_list = df["RATING"].tolist() # Converting the df to list of ratings
            print(f"Average Satisfaction: {avg_rating:.2f}") # Printing with 2 decimal format
            
            # Displaying the ratings and comments
            for rating, comment in zip(rating_list, comments_list):
                print(f"Rating: {rating}, Comment: {comment}")
        else:
            print("No feedback data available.")
    else:
        print("Feedback data file does not exist.")
        
# Executing as script
if __name__ == "__main__":
    calculate_feedback_stats()