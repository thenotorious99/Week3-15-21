class Phone:
    def __init__(self, name, model, battery):
        self.name = name
        self.model = model
        self.battery = battery

    def charge_battery(self):
            self.battery += 0.10
            if self.battery > 1.0:
                self.battery = 1.0

    def checking_model(self):
        battery_percent = int(self.battery * 100)
        return f"{self.name} {self.model} battery:{battery_percent}%"

phone1 = Phone("Samsung", "S23", 0.65)
print(phone1.checking_model())

phone1.charge_battery()
print(phone1.checking_model())