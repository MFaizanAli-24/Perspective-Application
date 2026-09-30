from claim_executors import add_supporting_claim, add_opposing_claim, add_neutral_claim, perform_balance_calculation

def main():

    while True:
        print("\nMenu:")
        print("1. Add Supporting Claim")
        print("2. Add Opposing Claim")
        print("3. Add Neutral Claim")
        print("4. Perform Balance Calculation")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_supporting_claim()
        elif choice == "2":
            add_opposing_claim()
        elif choice == "3":
            add_neutral_claim()
        elif choice == "4":
            perform_balance_calculation()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()