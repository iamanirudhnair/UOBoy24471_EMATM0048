Simulation of Fish Hatchery

Overview of the Project
The project is a text-based simulation of fish hatchery management system. Using this application, a hatchery manager must make various managerial decisions for each quarter of a year. The decisions expected to be put into place vary from managing the types of fish species in the hatchery, to hiring and letting go of technicians, selling fish, buying supplies, and managing warehouse inventory. The goal is to keep the hatchery afloat from quarter to quarter without going bankrupt. Moving from one quarter to the next causes change in the cash level within the hatchery. The fixed costs in the hatchery diminish that degree by the expenditure of salaries for technicians, feed costs, and warehouse maintenance.

The simulation runs through a series of quarters wherein the user inputs data at the beginning of each quarter. Input here includes the number of technicians to keep, what species of fish to raise, if any of these are to be sold, supplies to be purchased, and so on. Input is to be submitted for the entire quarter before aspects such as cash balance, current supply levels, and status of technicians are updated. The simulation ends when the hatchery has finally gone bankrupt or after a predefined number of quarters.

Project structure
This project is organized into a number of Python files, each one implementing aspects of the application and structuring the project. In the following description, you will find a summary of the files contained in the project:

main.py
This is the starting point of the simulation program. It begins its execution by prompting the user to enter the number of simulated quarters, and the creation of a Hatchery with the parameters undertaken.

Key methods:
main(): Prompt the user for input, create a hatchery, and run the simulation for the input number of quarters or until the hatchery goes bankrupt.

hatchery.py
In this file, the class Hatchery, which is a model of the fish hatchery, implement most of the logic engaged in conducting the simulation. Hiring technicians, selling fish, and purchasing supplies will be taken care of herein. It has logic for: 

Adjusting technician numbers based on user input.
Selling fish while taking into account the availability of supplies and technicians.
Paying technicians and managing supply costs.
Updating cash balance and displaying the hatchery's status after each quarter.

__init__(): Initializes the hatchery with a number of quarters, initial cash, fixed costs, and sets up the warehouse, technicians, fish species, and vendors.
run_quarter(): Runs the entire simulation for one quarter (including technician management, fish sales, payments, supply purchases, and cash management).
hire_technician(): Hires a technician and adds him to the hatchery's workforce if there is vacancy.
fire_technician(): Fires any technician, reducing the workforce.
sell_fish(): Sells a specified amount of fish, updating the hatchery's supplies and cash.