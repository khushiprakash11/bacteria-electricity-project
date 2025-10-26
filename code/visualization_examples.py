"""
Bacteria Electricity Visualization Examples
Demo code showing visualization structure
"""

import matplotlib.pyplot as plt
import numpy as np

# Note: Using sample data for demonstration
# Actual research data is kept private


def plot_power_output_comparison():
    """
    Compare power output across different bacterial strains
    """
    # Sample data (not actual research values)
    strains = ['Geobacter\nsulfurreducens', 'Shewanella\noneidensis',
               'Rhodoferax\nferrireducens']
    power_output = [0.45, 0.38, 0.31]  # Sample values in mW

    plt.figure(figsize=(10, 6))
    plt.bar(strains, power_output, color=['#2ecc71', '#3498db', '#e74c3c'])
    plt.xlabel('Bacterial Strain', fontsize=12)
    plt.ylabel('Power Output (mW)', fontsize=12)
    plt.title('Power Generation by Bacterial Strain (Demo Data)', fontsize=14)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('../visualizations/power_comparison.png', dpi=300)
    plt.show()


def plot_voltage_current_relationship():
    """
    Show voltage-current relationship
    """
    # Sample data points
    voltage = np.linspace(0, 0.8, 50)
    current = voltage * 0.6 + np.random.normal(0, 0.02, 50)  # Simulated

    plt.figure(figsize=(10, 6))
    plt.scatter(voltage, current, alpha=0.6, s=50)
    plt.xlabel('Voltage (V)', fontsize=12)
    plt.ylabel('Current (mA)', fontsize=12)
    plt.title('Voltage-Current Relationship (Sample Data)', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('../visualizations/voltage_current.png', dpi=300)
    plt.show()


def plot_efficiency_over_time():
    """
    Efficiency trends over time
    """
    # Sample time series data
    time_hours = np.arange(0, 24, 1)
    efficiency = 75 + 5 * np.sin(time_hours / 4) + \
        np.random.normal(0, 2, len(time_hours))

    plt.figure(figsize=(12, 6))
    plt.plot(time_hours, efficiency, marker='o', linewidth=2, markersize=6)
    plt.xlabel('Time (hours)', fontsize=12)
    plt.ylabel('Efficiency (%)', fontsize=12)
    plt.title('Bacterial Fuel Cell Efficiency Over Time (Demo)', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.ylim(60, 90)
    plt.tight_layout()
    plt.savefig('../visualizations/efficiency_time.png', dpi=300)
    plt.show()


def plot_multi_strain_comparison():
    """
    Compare multiple parameters across strains
    """
    strains = ['Strain A', 'Strain B', 'Strain C', 'Strain D']
    voltage = [0.6, 0.7, 0.5, 0.65]
    current = [0.4, 0.5, 0.35, 0.45]

    x = np.arange(len(strains))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    bars1 = ax.bar(x - width/2, voltage, width,
                   label='Voltage (V)', color='#3498db')
    bars2 = ax.bar(x + width/2, current, width,
                   label='Current (mA)', color='#e74c3c')

    ax.set_xlabel('Bacterial Strains', fontsize=12)
    ax.set_ylabel('Measurement Values', fontsize=12)
    ax.set_title('Multi-Parameter Comparison (Sample Data)', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(strains)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.savefig('../visualizations/multi_parameter.png', dpi=300)
    plt.show()


def create_summary_dashboard():
    """
    Create a dashboard with multiple visualizations
    """
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

    # Top left: Bar chart
    strains = ['G. sulf.', 'S. oneid.', 'R. ferri.']
    power = [0.45, 0.38, 0.31]
    ax1.bar(strains, power, color='#2ecc71')
    ax1.set_title('Power Output by Strain')
    ax1.set_ylabel('Power (mW)')

    # Top right: Line plot
    time = np.arange(0, 24, 2)
    efficiency = 70 + 10 * np.sin(time / 4)
    ax2.plot(time, efficiency, marker='o', color='#3498db')
    ax2.set_title('Efficiency Over Time')
    ax2.set_xlabel('Time (hours)')
    ax2.set_ylabel('Efficiency (%)')

    # Bottom left: Scatter
    voltage = np.random.uniform(0.3, 0.8, 30)
    current = voltage * 0.5 + np.random.normal(0, 0.05, 30)
    ax3.scatter(voltage, current, alpha=0.6, color='#e74c3c')
    ax3.set_title('Voltage-Current Relationship')
    ax3.set_xlabel('Voltage (V)')
    ax3.set_ylabel('Current (mA)')

    # Bottom right: Pie chart
    categories = ['Energy Output', 'Efficiency', 'Stability', 'Cost']
    values = [35, 25, 25, 15]
    ax4.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
    ax4.set_title('Performance Factors')

    plt.suptitle(
        'Bacterial Electricity Generation Dashboard (Demo)', fontsize=16, y=1.00)
    plt.tight_layout()
    plt.savefig('../visualizations/dashboard.png',
                dpi=300, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    print("Generating visualizations...")
    print("Note: All data shown is for demonstration purposes")
    print("-" * 50)

    plot_power_output_comparison()
    plot_voltage_current_relationship()
    plot_efficiency_over_time()
    plot_multi_strain_comparison()
    create_summary_dashboard()

    print("\nVisualizations saved to ../visualizations/ folder")
