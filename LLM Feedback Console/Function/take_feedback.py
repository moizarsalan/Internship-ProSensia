def feedback() -> dict:
    user_rating = None
    comm_sugg = "No Comment"
    
    while True:
        user_rating = input(
            "\n###########################################################################\n"
            "How satisfied are you with the answer provided? You can rate from 1 to 5: "
        )
        # Validation
        if user_rating.isnumeric():
            # Converting the user_rating to int data type
            user_rating = int(user_rating)
            # Validation
            if (user_rating) >= 1 and user_rating <= 5:
                break # Breaking the loop if the input is between 1 and 5
            else:
                print("Invalid rating.")
        else:
            print("Only numeric input is allowed.")
    
    # Message for unsatisfactory feedback 
    if user_rating <= 3:
        while True:
            comm_sugg = input(
                "\n########################################\n"
                "Any additional comments or suggestions?: "
            )
            # Validation
            if comm_sugg == "":
                print("Field cannot be empty.")
            else:
                break # Breaking the loop if any comment or suggestion is provided
    
    # Dictionary to store rating, comments and suggestion
    result = {
        "rating": user_rating,
        "suggestion": comm_sugg,
    }
    
    # Returning the dictionary
    return result