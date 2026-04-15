#Log analyze
import os

def analyze_log(targeted_word) :
    print(f"\n Scanning logs for: '{targeted_word}'...\n")

    found_count = 0
    
    if os.path.exists("server.log"):
        with open("server.log" , "r") as file :
            for line_number , line in enumerate(file) :
                if targeted_word.upper() in line.upper() :
                    print(f" ALERT on Line {line_number + 1}: {line.strip()}")
                    found_count += 1
        print(f"\n--- Analysis Completed. Found {found_count} incidents. ---")
    else :
        print(" Error: 'server.log' file not found. Run the setup script first!")

print("--- CYBER SECURITY LOG PARSER ---")

while True :
    print("\n1: Scan for Errors")
    print("2: Scan for Failed Logins")
    print("3: custom scan")
    print("4: Quit")

    choice = input("Please enter in what would you like to do (1/2/3/4): ")

    if choice == "1" :
        analyze_log("Error")
    
    elif choice == "2" :
        analyze_log("Failed login")
    
    elif choice == "3" :
        custom_word = input("What would you like to look for? ")
        analyze_log(custom_word)
    
    elif choice == "4" :
        print("Take care!")
        break
    
    else :
        print("Invalid input!")



    