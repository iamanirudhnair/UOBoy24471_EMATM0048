from hatchery import Hatchery

def get_positive_integer(prompt):
    """
    Get a positive integer from the user.
    Repeatedly asks the user until a valid input is received.
    """
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                raise ValueError("Input can't be empty.")
            value = int(value)
            if value <= 0:
                raise ValueError("Input must be a positive integer.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")

def main():
    """
    Main function which starts the hatchery simulation, asks user to enter input.
    It runs for the specified number of quarters or until the hatchery goes bankrupt.
    """
    num_quarters = get_positive_integer("Please enter the number of quarters to simulate: ")

    try:
        hatchery = Hatchery(num_quarters)  # Initializing the hatchery with specified no. of quarters
    except Exception as e:
        print(f"Error initializing the hatchery: {e}")
        return

    # Iterating over the range of quarters and printing the current quarter number
    for quarter in range(1, num_quarters + 1):  # Start from 1 to num_quarters (inclusive)
        print(f"\n================================\n====== SIMULATING {quarter} ==========\n================================")  # Print current quarter
        try:
            if not hatchery.run_quarter():
                print("The hatchery has gone bankrupt. Simulation terminated.")
                break  # Stop the simulation if bankrupt
        except Exception as e:
            print(f"An error occurred during the quarter simulation: {e}")

if __name__ == "__main__":
    main()  # Running the main function to begin the simulation
