# Bitcoin Price Regression Plot

This program creates a regression plot of Bitcoin (BTC) price data from a CSV file using logarithmic regression.
Dependencies

The following Python libraries are required to run the program:

    Matplotlib
    NumPy
    Pandas
    SciPy
    scikit-learn

Installation

    Ensure that the required libraries are installed on your machine.
    Clone or download the repository.
    Open the terminal and navigate to the directory containing the program.
    Run the program with the command python bitcoin_regression.py.
    The regression plot will be displayed or saved as a PNG image in the same directory.

Usage

    Create a CSV file containing two columns: date (in the format DD/MM/YYYY) and BTC price.
    Save the CSV file in the same directory as the program.
    Open the terminal and navigate to the directory containing the program.
    Run the program with the command python bitcoin_regression.py.
    The regression plot will be displayed or saved as a PNG image in the same directory.

How it works

The program reads the CSV file using Pandas and formats the data for plotting. The logarithmic regression function is defined as y = a*log(x) + b using SciPy's curve_fit() function. The regression coefficients and R-squared value are calculated and printed to the console. The regression line is plotted using Matplotlib's semilogy() function, and the area between the line and the data is filled using fill_between().
Disclaimer

This program is intended for educational or data analysis purposes only and should not be used for malicious or speculative activities. The program and its author(s) are not responsible for any actions taken using this program.
