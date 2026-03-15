# Healthcare Claims Processing Project
# Author: Vinay Kumar
# Purpose: Validate and process healthcare claims data based on business rules

# Counters for error tracking
invalid_amount_count = 0
missing_amount_count = 0
negative_claim_count = 0
large_claim_count = 0

# Variable to store total approved claims
total_approved_claim_amount = 0

# Open and read the dataset
with open("claims_data.txt", "r") as file:

    for line in file:

        # Split the row values
        parts = line.strip().split(",")

        claim_id = parts[0]
        name = parts[1]
        amount = parts[2]
        status = parts[3]

        try:

            # Check for missing value
            if amount == "":
                missing_amount_count += 1
                raise ValueError("Missing claim amount")

            # Convert amount to float
            bill = float(amount)

            # Check for negative claim
            if bill < 0:
                negative_claim_count += 1
                raise ValueError("Negative claim amount")

            # Check for unrealistic large claim
            if bill > 10000:
                large_claim_count += 1
                raise ValueError("Claim amount too large")

        except ValueError as e:

            # Detect invalid text values
            if amount != "" and amount.isalpha():
                invalid_amount_count += 1

            print(name, "->", e)

        else:

            # Add only valid approved claims
            if status == "Approved":
                total_approved_claim_amount += bill


# Final Report
print("\n----- Claims Processing Summary -----")

print("Total Approved Claim Amount:", total_approved_claim_amount)
print("Invalid Amount Values:", invalid_amount_count)
print("Missing Amount Values:", missing_amount_count)
print("Negative Claims:", negative_claim_count)
print("Large Claims:", large_claim_count)