class Flight:
    def __init__(self, company, number_of_flight, destination):
        self.company = company
        self.number_of_flight = number_of_flight
        self.destination = destination

    """" 
    def right_flight(self):
        return f"United Airlines tell that, this flight is for London!"
    """
flights = [
    Flight("United Airlines", 8, "London"),
    Flight("Arab Airlines", 5, "USA"),
    Flight("Surbian Airlines", 6, "London")

]
# print("Company with flights for London:")

for flight in flights:
    if flight.destination == "London":
        print(flight.company)