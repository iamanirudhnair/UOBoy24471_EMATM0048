from hatchery import Hatchery

def main():
    num_quarters = int(input("Please enter number of quarters: ")) # Asking user for number of quarters to simulate
    hatchery = Hatchery(num_quarters=num_quarters)
    for _ in range(hatchery.quarters):
        if not hatchery.run_quarter():
            break # If hatchery goes bankrupt, stop the simulation
        hatchery.quarters += 1

if __name__ == "__main__":
    main() # Run main function to start the simulation