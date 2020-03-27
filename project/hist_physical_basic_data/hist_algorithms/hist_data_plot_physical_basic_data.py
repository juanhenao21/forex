'''HIST data plot module.

The functions in the module plot the data obtained in the
hist_data_analysis_extraction module.

This script requires the following modules:
    * gc
    * matplotlib
    * pickle
    * hist_data_tools_data_extract

The module contains the following functions:
    * hist_fx_quotes_year_plot - plots the forex quotes for a year.
    * hist_fx_midpoint_year_plot - plots the forex quotes for a year.
    * hist_fx_spread_year_plot - plots the forex quotes for a year.
    * main - the main function of the script.

.. moduleauthor:: Juan Camilo Henao Londono <www.github.com/juanhenao21>
'''

# ----------------------------------------------------------------------------
# Modules

import gc
from matplotlib import pyplot as plt
import pickle

import hist_data_tools_extraction

# ----------------------------------------------------------------------------


def hist_fx_quotes_year_plot(fx_pair, year, weeks):
    """Plots the quotes price for a year.

    :param fx_pair: string of the abbreviation of the forex pair to be analyzed
     (i.e. 'eur_usd').
    :param year: string of the year to be analyzed (i.e. '2016').
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    try:
        function_name = hist_fx_quotes_year_plot.__name__
        hist_data_tools_extraction \
            .hist_function_header_print_plot(function_name, fx_pair, year, '')
        fx_pair_upper = fx_pair[:3].upper() + '/' + fx_pair[4:].upper()

        figure = plt.figure(figsize=(16, 9))

        for week in weeks:
            # Load data
            fx_data = pickle.load(open(
                            f'../../hist_data/extraction_data_{year}/hist_fx'
                            + f'_data_extraction/{fx_pair}/hist_fx_data'
                            + f'_extraction_{fx_pair}_w{week}.pickle', 'rb'))

            plt.plot(fx_data['Date'], fx_data['Bid'], 'g', linewidth=5,
                     label='Bid')
            plt.plot(fx_data['Date'], fx_data['Ask'], 'b', linewidth=5,
                     label='Ask')

        # plt.legend(loc='best', fontsize=25)
        plt.title(f'HIST quotes price - {fx_pair_upper}', fontsize=40)
        plt.xlabel(r'Time $[s]$', fontsize=35)
        plt.ylabel(r'Quotes $[\$]$', fontsize=35)
        plt.xticks(fontsize=25)
        plt.yticks(fontsize=25)
        plt.grid(True)
        plt.tight_layout()

        # Plotting
        hist_data_tools_extraction \
            .hist_save_plot(function_name, figure, fx_pair, year, '')

        plt.close()
        del fx_data
        del figure
        gc.collect()

        return None

    except FileNotFoundError as e:
        print('No data')
        print(e)
        print()
        return None

# ----------------------------------------------------------------------------


def hist_fx_midpoint_year_plot(fx_pair, year, weeks):
    """Plots the midpoint price for a year.

    :param fx_pair: string of the abbreviation of the forex pair to be analyzed
     (i.e. 'eur_usd').
    :param year: string of the year to be analyzed (i.e. '2016').
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    try:
        function_name = hist_fx_midpoint_year_plot.__name__
        hist_data_tools_extraction \
            .hist_function_header_print_plot(function_name, fx_pair, year, '')
        fx_pair_upper = fx_pair[:3].upper() + '/' + fx_pair[4:].upper()

        figure = plt.figure(figsize=(16, 9))

        for week in weeks:
            # Load data
            fx_data = pickle.load(open(
                            f'../../hist_data/extraction_data_{year}/hist_fx'
                            + f'_data_extraction/{fx_pair}/hist_fx_data'
                            + f'_extraction_{fx_pair}_w{week}.pickle', 'rb'))

            plt.plot(fx_data['Date'], (fx_data['Bid'] + fx_data['Ask']) / 2,
                     'g', linewidth=5)

        plt.title(f'HIST midpoint price - {fx_pair_upper}', fontsize=40)
        plt.xlabel(r'Time $[s]$', fontsize=35)
        plt.ylabel(r'$m(t) [\$]$', fontsize=35)
        plt.xticks(fontsize=25)
        plt.yticks(fontsize=25)
        plt.grid(True)
        plt.tight_layout()

        # Plotting
        hist_data_tools_extraction \
            .hist_save_plot(function_name, figure, fx_pair, year, '')

        plt.close()
        del fx_data
        del figure
        gc.collect()

        return None

    except FileNotFoundError as e:
        print('No data')
        print(e)
        print()
        return None

# ----------------------------------------------------------------------------


def hist_fx_spread_year_plot(fx_pair, year, weeks):
    """Plots the spread for a year.

    :param fx_pair: string of the abbreviation of the forex pair to be analyzed
     (i.e. 'eur_usd').
    :param year: string of the year to be analyzed (i.e. '2016').
    :return: None -- The function saves the plot in a file and does not return
     a value.
    """

    try:
        function_name = hist_fx_spread_year_plot.__name__
        hist_data_tools_extraction \
            .hist_function_header_print_plot(function_name, fx_pair, year, '')
        fx_pair_upper = fx_pair[:3].upper() + '/' + fx_pair[4:].upper()

        figure = plt.figure(figsize=(16, 9))

        for week in weeks:
            # Load data
            fx_data = pickle.load(open(
                            f'../../hist_data/extraction_data_{year}/hist_fx'
                            + f'_data_extraction/{fx_pair}/hist_fx_data'
                            + f'_extraction_{fx_pair}_w{week}.pickle', 'rb'))

            plt.plot(fx_data['Date'], fx_data['Ask'] - fx_data['Bid'], 'g',
                     linewidth=5)

        plt.title(f'HIST spread price - {fx_pair_upper}', fontsize=40)
        plt.xlabel(r'Time $[s]$', fontsize=35)
        plt.ylabel(r'Spread $[\$]$', fontsize=35)
        plt.xticks(fontsize=25)
        plt.yticks(fontsize=25)
        plt.grid(True)
        plt.tight_layout()

        # Plotting
        hist_data_tools_extraction \
            .hist_save_plot(function_name, figure, fx_pair, year, '')

        plt.close()
        del fx_data
        del figure
        gc.collect()

        return None

    except FileNotFoundError as e:
        print('No data')
        print(e)
        print()
        return None


# -----------------------------------------------------------------------------


def main():
    """The main function of the script.

    The main function is used to test the functions in the script.

    :return: None.
    """

    pass

    return None

# -----------------------------------------------------------------------------


if __name__ == "__main__":
    main()