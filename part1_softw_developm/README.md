# Simulation of Fish Hatchery

## Overview of the Project

The project is a text-based simulation of fish hatchery management system. Using this application, a hatchery manager must make various managerial decisions for each quarter of a year. The decisions expected to be put into place vary from managing the types of fish species in the hatchery, to hiring and letting go of technicians, selling fish, buying supplies, and managing warehouse inventory. The goal is to keep the hatchery afloat from quarter to quarter without going bankrupt. Moving from one quarter to the next causes change in the cash level within the hatchery. The fixed costs in the hatchery diminish that degree by the expenditure of salaries for technicians, feed costs, and warehouse maintenance.

The simulation runs through a series of quarters wherein the user inputs data at the beginning of each quarter. Input here includes the number of technicians to keep, what species of fish to raise, if any of these are to be sold, supplies to be purchased, and so on. Input is to be submitted for the entire quarter before aspects such as cash balance, current supply levels, and status of technicians are updated. The simulation ends when the hatchery has finally gone bankrupt or after a predefined number of quarters.

## Project structure

This project is organized into a number of Python files, each one implementing aspects of the application and structuring the project. In the following description, you will find a summary of the files contained in the project:

### main.py
This is the starting point of the simulation program. It begins its execution by prompting the user to enter the number of simulated quarters, and the creation of a Hatchery with the parameters undertaken.

Key methods:
main(): Prompt the user for input, create a hatchery, and run the simulation for the input number of quarters or until the hatchery goes bankrupt.

# hatchery.py
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
adjust_technicians(): Prompts user input to adjust the number of technicians.
adjust_fish_sales(): Prompts the user to decide how much fish to sell.
restock_supplies(): Prompts the user to pick a vendor and restocks supplies from the vendor.

# warehouse.py
This file defines the class Warehouse that represents storage facilities for the Hatchery; it keeps track of inventories of fertilizers, feeds, and salt and computes depreciation; it also calculates costs for restocking supplies and handles depreciation of supplies over time.

__init__(): Initializes the warehouse with a selected supply capacity for main and auxiliary supply warehouses and sets cost structure for each supply type.
add_supply(): Adds a certain amount of a certain supply type (fertilizer, feed, or salt) to the warehouse.
apply_depreciation(): Applies depreciation to the supplies inside the warehouse at the end of each quarter.
get_total_cost(): Calculates total cost of all supplies in the warehouse for the current quarter. 

# technician.py
This file implements the Technician class, which represents individual workers in the hatchery. Each technician is paid a week by a quarter for 9 weeks of work.

__init__(): Initialize the technician using a name and a weekly rate of pay.
get_payment(): Calculates total earnings for the quarter based upon pay rate for the technician (paid for 9 weeks).

# vendor.py
The Vendor class represents the suppliers selling mixed supplies (the ones that supplies the hatchery with fertilizer, feed, and salt). The prices of supplies depend on which vendor is chosen.

__init__(): Initialize the vendor using a name and the prices for supplies.
get_price(): Quotes the price of a certain kind of supply type(fertilizer, feed, or salt) from the vendor.

# fish_species.py
This file implements the FishSpecies class, representing the different fish species raised out and sold in the hatchery. Every species has some specific requirement regarding what fertilizer, feed, and salt it needs as well as the time of maintenance, demand, and price per fish.

__init__(): Initialize the fish species with the type of fish, fertilizer requirements, feed requirements, salt requirements, maintenance time, demand, and price.

## Design Decisions

# Object-Oriented Design

The whole system is built on object-oriented principles such that modularity and encapsulation thrive. The hatchery, technicians, fish species, and warehouse in the simulation are all modeled as separate classes. This arrangement makes it much easier to maintain, extend, and debug the simulation.

# Separation of Concerns

Every class is responsible for dealing with a particular aspect of the hatchery simulation:

Hatchery-the main driver for the simulation orchestrating flow through any quarter.
Technician-deals with the workers and salaries.
Warehouse-deals with the inventory and depreciation.
Vendor-is responsible for the supply chain and purchasing decisions.
FishSpecies refers to the fish species along with their needs and sales related information.

# User Input Handling

User input is guided interactively after each quarter of the simulation, while error handling ensures that the input values are valid. More specifically, in the event of adjusting technicians or selling fish, the inputs are kept within range by the program, which subsequently would gracefully handle any troublesome entries made by the user.

# Flexibility and Extendibility

The design allows for flexibility and even extensibility. Thus, it is an easy matter to add new fish species by modifying the FishSpecies class. To make changes to suppliers, a new Vendor object can be added. The simulation also allows for varying the number of quarters in addition to other parameters. Therefore, it is flexible enough to accommodate different kinds of use cases.

# Bankruptcy Mechanism

There is a mechanism for bankruptcy in the simulation; if the hatchery's cash balance were to become negative, the simulation ends, and the hatchery is declared bankrupt. According to what simulation is all about, this is indeed the most critical part, which means the user must be, at all times, careful about finances.

# Executing the Simulation

To start the simulation, you will run the main.py file. The program will then request the user to specify the number of quarters for the simulation. By default, the simulation runs for 2 years (8 quarters). During the simulation, the user will be prompted to make decisions regarding technician management, fish sales, and supply purchases.

# Example Workflow:

The simulation starts by setting the number of quarters.
The quarter starts with the hiring or firing of technicians.
Sales of fish types are decided upon.
Pay the technicians and cover costs. Supply costs are deducted, and technicians are given their wages.
Concept of depreciation: Aging of warehouse supplies reduces their value.
Supply replenishment: Choose a vendor to restock supplies, if needed.
End of the quarter: Updates are made to the hatchery with respect to cash, inventory, and technician status.
The simulation continues on until all game quarters specified in this project are completed or till the hatchery goes bankrupt.

# Conclusion

In this project, the hatchery business is modeled in a fish hatchery simulation, and the user makes decisions to maximize profitability and avoid bankruptcy. Using object-oriented design, the simulation comes modularized, can be easily maintained, and better extended. It provides a thorough framework for learning about financial management, resource allocation, and decision-making activities in business. Reduction of redundancy, outrageous of varieties are foreseen; yet, balance of transitions is taken care of.
