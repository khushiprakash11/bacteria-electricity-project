"""
Simple visualization examples for bacteria electricity project
"""

import matplotlib.pyplot as plt


def simple_bar_chart():
    """Basic bar chart of power output"""
    bacteria = ['Geobacter', 'Shewanella', 'Rhodoferax']
    power = [0.45, 0.38, 0.31]  # Sample data in mW

    plt.bar(bacteria, power, color='green')
    plt.xlabel('Bacterial Strain')
    plt.ylabel('Power Output (mW)')
    plt.title('Electricity Generation Comparison')
    plt.savefig('visualizations/simple_comparison.png')
    plt.show()


def simple_line_plot():
    """Time-based efficiency plot"""
    hours = [0, 4, 8, 12, 16, 20, 24]
    efficiency = [65, 70, 75, 78, 76, 72, 68]  # Sample percentages

    plt.plot(hours, efficiency, marker='o', color='blue')
    plt.xlabel('Time (hours)')
    plt.ylabel('Efficiency (%)')
    plt.title('Efficiency Over 24 Hours')
    plt.grid(True)
    plt.savefig('visualizations/efficiency_plot.png')
    plt.show()


# Run the visualizations
if __name__ == "__main__":
    simple_bar_chart()
    simple_line_plot()
    print("Visualizations created!")
