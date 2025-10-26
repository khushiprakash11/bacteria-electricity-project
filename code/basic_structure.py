"""
Bacteria Electricity Generation - Demo Structure
This shows the basic framework of the analysis
"""


class BacteriaAnalyzer:
    def __init__(self, strain_name):
        self.strain_name = strain_name
        self.voltage = None
        self.current = None

    def measure_output(self, voltage, current):
        """Record electrical output measurements"""
        self.voltage = voltage
        self.current = current

    def calculate_power(self):
        """Calculate basic power output"""
        # Simplified calculation for demo
        if self.voltage and self.current:
            return self.voltage * self.current
        return 0

    def display_results(self):
        """Show the results"""
        power = self.calculate_power()
        print(f"Strain: {self.strain_name}")
        print(f"Power Output: {power} mW")


# Example usage
bacteria = BacteriaAnalyzer("Geobacter sulfurreducens")
bacteria.measure_output(0.5, 0.3)
bacteria.display_results()
