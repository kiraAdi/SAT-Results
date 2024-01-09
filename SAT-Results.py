# Write a code in python with the following features:

# - Must have a menu to select option from
# 1. Insert data
# 2. View all data
# 3. Get rank
# 4. Update score
# 5. Delete one record
# 6. Put the inserted data in json format in a file.

# - Insert data - this needs to handle input data for the following Object and store in memory:
# SAT Results
# - Name (Unique Identifier)
# - Address
# - City
# - Country
# - Pincode
# - SAT score
# - Passed - this needs to be calculated in the backend as follows - if SAT score > 30% = Pass else Fail
# - View all data - this should display all the data from the memory in Json format
# - Get rank - this takes the name and returns their rank according to the data from the memory
# - Update score - this allows to update SAT score for a candidate by name
# - Delete one record - this deletes a record by name
# - (Optional) Make use of a database of your choice



# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import json

# In-memory data structure to store SAT results
sat_results = []

def insert_data():
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    city = input("Enter City: ")
    country = input("Enter Country: ")
    pincode = input("Enter Pincode: ")
    sat_score = float(input("Enter SAT Score: "))
    
    passed = "Pass" if sat_score > 30 else "Fail"
    
    # Creating a dictionary for the SAT result
    result = {
        "Name": name,
        "Address": address,
        "City": city,
        "Country": country,
        "Pincode": pincode,
        "SAT Score": sat_score,
        "Passed": passed
    }
    
    sat_results.append(result)
    print("Data inserted successfully!")

def view_all_data():
    print(json.dumps(sat_results, indent=2))

def get_rank():
    name = input("Enter the name to get the rank: ")
    for i, result in enumerate(sorted(sat_results, key=lambda x: x["SAT Score"], reverse=True), 1):
        if result["Name"] == name:
            print(f"Rank for {name}: {i}")
            return
    print(f"No data found for {name}")

def update_score():
    name = input("Enter the name to update the SAT score: ")
    for result in sat_results:
        if result["Name"] == name:
            new_score = float(input("Enter the new SAT Score: "))
            result["SAT Score"] = new_score
            result["Passed"] = "Pass" if new_score > 30 else "Fail"
            print("SAT score updated successfully!")
            return
    print(f"No data found for {name}")

def delete_record():
    name = input("Enter the name to delete the record: ")
    for result in sat_results:
        if result["Name"] == name:
            sat_results.remove(result)
            print("Record deleted successfully!")
            return
    print(f"No data found for {name}")

def save_to_json():
    filename = input("Enter the filename to save the data in JSON format: ")
    with open(filename, "w") as file:
        json.dump(sat_results, file, indent=2)
        print("Data saved to JSON file successfully!")

def main():
    while True:
        print("\nMenu:")
        print("1. Insert data")
        print("2. View all data")
        print("3. Get rank")
        print("4. Update score")
        print("5. Delete one record")
        print("6. Save to JSON file")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            insert_data()
        elif choice == "2":
            view_all_data()
        elif choice == "3":
            get_rank()
        elif choice == "4":
            update_score()
        elif choice == "5":
            delete_record()
        elif choice == "6":
            save_to_json()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()




