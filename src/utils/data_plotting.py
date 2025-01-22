import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from typing import Dict
import numpy as np

def plot_gr_logs(df: pd.DataFrame, title: str) -> None:
    """
    Plots gamma-ray (GR) logs from the provided DataFrame on the specified axes.

    Args:
        df (pd.DataFrame): DataFrame containing the well log data, 
            where 'GR' represents gamma-ray values and 'TDEP' represents depth values.
        title (str): Title for the plot.

    Returns:
        None
    """
    fig, ax = plt.subplots(1, 1, figsize=(4, df['TDEP'].max()//14))

    # Extract GR and TDEP values for plotting the GR log in the range 0 to 150
    x_0_150 = df['GR']
    y_0_150 = df['TDEP']

    # Create a copy of the DataFrame to adjust GR values for the range 150 to 300
    df_150_300 = df.copy()
    df_150_300['GR'] = df_150_300['GR'] - 150
    x_150_300 = df_150_300['GR']
    y_150_300 = df_150_300['TDEP']

    # Plot the original GR logs (0 to 150 range) with blue color
    ax.plot(x_0_150, y_0_150, label='GR', color='blue', linewidth=0.75, zorder=2)

    # Plot the adjusted GR logs (150 to 300 range) with the same color and style
    ax.plot(x_150_300, y_150_300, color='blue', linewidth=0.75, zorder=2)

    # Set the X-axis ticks and labels for both GR ranges (0-150 and 150-300)
    ticks_x_axis = [0,  15,  30,  45,  60,  75,  90, 105, 120, 135, 150]
    labels_x_axis = ['0\n150', '15\n165', '30\n180', '45\n195', '60\n210', 
                     '75\n225', '90\n240', '105\n255', '120\n270', '135\n285', '150\n300']
    ax.set_xticks(ticks_x_axis)
    ax.set_xticklabels(labels_x_axis)

    # Position X-axis ticks and labels at the top of the plot
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')

    # Format the Y-axis tick labels to display intervals of 50
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:.0f}' if x % 50 == 0 else ''))

    # Disable X-axis and Y-axis tick markers (removes small tick lines)
    ax.tick_params(axis='x', which='both', bottom=False, top=False)
    ax.tick_params(axis='y', which='both', left=False, right=False)

    # Add gridlines to the plot
    ax.grid(True, axis='both', zorder=0)

    # Set the gridline interval on the Y-axis
    ax.yaxis.set_major_locator(plt.MultipleLocator(5))

    # Set X-axis limits to restrict the GR range from 0 to 150
    ax.set_xlim(0, 150)
    ax.set_ylim(0, df['TDEP'].max())

    # Invert the Y-axis to represent depth increasing downwards
    ax.invert_yaxis()

    # Add title and labels to the X and Y axes with bold font
    ax.set_title(title, fontweight='bold')
    ax.set_xlabel('GR', fontweight='bold')
    ax.set_ylabel('TDEP', fontweight='bold')

    # Display the legend for the GR log
    ax.legend()


def plot_dt_logs(df: pd.DataFrame, title: str) -> None:
    """
    Plots DT logs from the provided DataFrame on the specified axes.

    Args:
        df (pd.DataFrame): DataFrame containing the well log data, 
            where 'GR' represents gamma-ray values and 'TDEP' represents depth values.
        title (str): Title for the plot.

    Returns:
        None
    """
    fig, ax = plt.subplots(1, 1, figsize=(8, df['TDEP'].max()//14))

    # Extract DT and TDEP values for plotting the DT logs
    x = df['DT']
    y = df['TDEP']

    # Plot the original DT logs with 
    ax.plot(x, y, label='DT', color='black', linewidth=0.75, zorder=2)

    # Set the X-axis ticks and labels for both DT ranges 
    ticks_x_axis = list(range(40, 241, 10))
    ax.set_xticks(ticks_x_axis)

    # Position X-axis ticks and labels at the top of the plot
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')

    # Format the Y-axis tick labels to display intervals of 50
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:.0f}' if x % 50 == 0 else ''))

    # Disable X-axis and Y-axis tick markers (removes small tick lines)
    ax.tick_params(axis='x', which='both', bottom=False, top=False)
    ax.tick_params(axis='y', which='both', left=False, right=False)

    # Add gridlines to the plot
    ax.grid(True, axis='both', zorder=0)

    # Set the gridline interval on the Y-axis
    ax.yaxis.set_major_locator(plt.MultipleLocator(5))

    # Set X-axis limits to restrict the GR range from 0 to 150
    ax.set_xlim(40, 240)
    ax.set_ylim(0, df['TDEP'].max())

    # Invert the Y-axis to represent depth increasing downwards
    ax.invert_yaxis()
    ax.invert_xaxis()

    # Add title and labels to the X and Y axes with bold font
    ax.set_title(title, fontweight='bold')
    ax.set_xlabel('DT', fontweight='bold')
    ax.set_ylabel('TDEP', fontweight='bold')

    # Display the legend for the GR log
    ax.legend()


def plot_linear_res_logs(df: pd.DataFrame, title: str) -> None:
    """
    Plots DT logs from the provided DataFrame on the specified axes.

    Args:
        df (pd.DataFrame): DataFrame containing the well log data, 
            where 'GR' represents gamma-ray values and 'TDEP' represents depth values.
        title (str): Title for the plot.

    Returns:
        None
    """
    fig, ax = plt.subplots(1, 1, figsize=(7, df['TDEP'].max()//14))

    # Extract DT and TDEP values for plotting the DT logs
    x = df['ILD']
    y = df['TDEP']

    # Plot the original DT logs with 
    ax.plot(x, y, label='ILD', color='green', linewidth=0.75, linestyle='--', zorder=2)

    # Set the X-axis ticks and labels for both res ranges 
    sequence = np.arange(-0.7, 1.41, 0.11) 
    ax.set_xticks(sequence)

    # Position X-axis ticks and labels at the top of the plot
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')

    # Format the Y-axis tick labels to display intervals of 50
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:.0f}' if x % 50 == 0 else ''))

    # Disable X-axis and Y-axis tick markers (removes small tick lines)
    ax.tick_params(axis='x', which='both', bottom=False, top=False)
    ax.tick_params(axis='y', which='both', left=False, right=False)

    # Add gridlines to the plot
    ax.grid(True, axis='both', zorder=0)

    # Set the gridline interval on the Y-axis
    ax.yaxis.set_major_locator(plt.MultipleLocator(5))

    # Set X-axis limits to restrict the GR range from 0 to 150
    ax.set_xlim(-0.7, 1.3)
    ax.set_ylim(0, df['TDEP'].max())

    # Invert the Y-axis to represent depth increasing downwards
    ax.invert_yaxis()

    # Add title and labels to the X and Y axes with bold font
    ax.set_title(title, fontweight='bold')
    ax.set_xlabel('RESD', fontweight='bold')
    ax.set_ylabel('TDEP', fontweight='bold')

    # Display the legend for the GR log
    ax.legend()


def plot_linear_res_logs_2_runs(df: pd.DataFrame, df2: pd.DataFrame, title: str) -> None:
    """
    Plots linear RES logs from the provided DataFrame on the specified axes.

    Args:
        df (pd.DataFrame): DataFrame containing the well log data, 
            where 'GR' represents gamma-ray values and 'TDEP' represents depth values.
        title (str): Title for the plot.

    Returns:
        None
    """
    fig, ax = plt.subplots(1, 1, figsize=(7.2, df['TDEP'].max()//14))

    # Extract DT and TDEP values for plotting the DT logs
    x = df['ILD']
    y = df['TDEP']
    x_2 = df2['ILD']
    y_2 = df2['TDEP']

    # Plot the original DT logs with 
    ax.plot(x, y, label='ILD 1', color='green', linewidth=0.75, linestyle='--', zorder=2)
    ax.plot(x_2, y_2, label='ILD 2', color='green', linewidth=0.75, linestyle='--', zorder=3)

    # Set the X-axis ticks and labels for both res ranges 
    sequence = np.arange(-0.7, 1.41, 0.11) 
    ax.set_xticks(sequence)

    # Position X-axis ticks and labels at the top of the plot
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')

    # Format the Y-axis tick labels to display intervals of 50
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:.0f}' if x % 50 == 0 else ''))

    # Disable X-axis and Y-axis tick markers (removes small tick lines)
    ax.tick_params(axis='x', which='both', bottom=False, top=False)
    ax.tick_params(axis='y', which='both', left=False, right=False)

    # Add gridlines to the plot
    ax.grid(True, axis='both', zorder=0)

    # Set the gridline interval on the Y-axis
    ax.yaxis.set_major_locator(plt.MultipleLocator(5))

    # Set X-axis limits to restrict the GR range from 0 to 150
    ax.set_xlim(-0.7, 1.3)
    ax.set_ylim(0, df['TDEP'].max())

    # Invert the Y-axis to represent depth increasing downwards
    ax.invert_yaxis()

    # Add title and labels to the X and Y axes with bold font
    ax.set_title(title, fontweight='bold')
    ax.set_xlabel('ILD', fontweight='bold')
    ax.set_ylabel('TDEP', fontweight='bold')

    # Display the legend for the GR log
    ax.legend()


def plot_dt_logs_2_runs(df: pd.DataFrame, df2: pd.DataFrame, title: str) -> None:
    """
    Plots DT logs from the provided DataFrame on the specified axes.

    Args:
        df (pd.DataFrame): DataFrame containing the well log data, 
            where 'GR' represents gamma-ray values and 'TDEP' represents depth values.
        title (str): Title for the plot.

    Returns:
        None
    """
    fig, ax = plt.subplots(1, 1, figsize=(8, df['TDEP'].max()//14))

    # Extract DT and TDEP values for plotting the DT logs
    x = df['DT']
    y = df['TDEP']
    x_2 = df2['DT']
    y_2 = df2['TDEP']

    # Plot the original DT logs with 
    ax.plot(x, y, label='DT 1', color='lightblue', linewidth=0.75, zorder=2)
    ax.plot(x_2, y_2, label='DT 2', color='salmon', linewidth=0.75, zorder=3)

    # Set the X-axis ticks and labels for both DT ranges 
    ticks_x_axis = list(range(40, 241, 10))
    ax.set_xticks(ticks_x_axis)

    # Position X-axis ticks and labels at the top of the plot
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')

    # Format the Y-axis tick labels to display intervals of 50
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:.0f}' if x % 50 == 0 else ''))

    # Disable X-axis and Y-axis tick markers (removes small tick lines)
    ax.tick_params(axis='x', which='both', bottom=False, top=False)
    ax.tick_params(axis='y', which='both', left=False, right=False)

    # Add gridlines to the plot
    ax.grid(True, axis='both', zorder=0)

    # Set the gridline interval on the Y-axis
    ax.yaxis.set_major_locator(plt.MultipleLocator(5))

    # Set X-axis limits to restrict the GR range from 0 to 150
    ax.set_xlim(40, 240)
    ax.set_ylim(0, df['TDEP'].max())

    # Invert the Y-axis to represent depth increasing downwards
    ax.invert_yaxis()
    ax.invert_xaxis()

    # Add title and labels to the X and Y axes with bold font
    ax.set_title(title, fontweight='bold')
    ax.set_xlabel('DT', fontweight='bold')
    ax.set_ylabel('TDEP', fontweight='bold')

    # Display the legend for the GR log
    ax.legend()



def plot_rhob_logs_2_runs(df: pd.DataFrame, df2: pd.DataFrame, title: str) -> None:
    """
    Plots RHOB logs from the provided DataFrame on the specified axes.

    Args:
        df (pd.DataFrame): DataFrame containing the well log data, 
            where 'GR' represents gamma-ray values and 'TDEP' represents depth values.
        title (str): Title for the plot.

    Returns:
        None
    """
    fig, ax = plt.subplots(1, 1, figsize=(8, df['TDEP'].max()//14))

    # Extract RHOB and TDEP values for plotting the RHOB logs
    x = df['RHOB']
    y = df['TDEP']

    x_2 = df2['RHOB']
    y_2 = df2['TDEP']

    # Create a copy of the DataFrame to adjust GR values for the range 150 to 300
    df_copy = df.copy()
    df_copy['RHOB'] = df_copy['RHOB'] + 1
    x_ = df_copy['RHOB']
    y_ = df_copy['TDEP']

    df2_copy = df2.copy()
    df2_copy['RHOB'] = df2_copy['RHOB'] + 1
    x_2_ = df2_copy['RHOB']
    y_2_ = df2_copy['TDEP']

    # Plot the RHOB logs in the range of 1-2 
    ax.plot(x, y, label='RHOB', color='salmon', linewidth=0.75, zorder=2)

    # Plot the original RHOB logs with 
    ax.plot(x_, y_, color='salmon', linewidth=0.75, zorder=2)

    # Plot the RHOB logs in the range of 1-2 
    ax.plot(x_2, y_2, label='RHOB', color='lightblue', linewidth=0.75, zorder=3)

    # Plot the original RHOB logs with 
    ax.plot(x_2_, y_2_, color='lightblue', linewidth=0.75, zorder=3)

    # Set the X-axis ticks and labels for both RHOB ranges 
    sequence = np.arange(2, 3.05, 0.05) 
    ax.set_xticks(sequence)

    # Position X-axis ticks and labels at the top of the plot
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')

    # Format the Y-axis tick labels to display intervals of 50
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:.0f}' if x % 50 == 0 else ''))

    # Disable X-axis and Y-axis tick markers (removes small tick lines)
    ax.tick_params(axis='x', which='both', bottom=False, top=False)
    ax.tick_params(axis='y', which='both', left=False, right=False)

    # Add gridlines to the plot
    ax.grid(True, axis='both', zorder=0)

    # Set the gridline interval on the Y-axis
    ax.yaxis.set_major_locator(plt.MultipleLocator(5))

    # Set X-axis limits to restrict the GR range from 0 to 150
    ax.set_xlim(2, 3)
    ax.set_ylim(0, df['TDEP'].max())

    # Invert the Y-axis to represent depth increasing downwards
    ax.invert_yaxis()

    # Add title and labels to the X and Y axes with bold font
    ax.set_title(title, fontweight='bold')
    ax.set_xlabel('RHOB', fontweight='bold')
    ax.set_ylabel('TDEP', fontweight='bold')

    # Display the legend for the GR log
    ax.legend()


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def plot_gr_logs_2_wells(df: pd.DataFrame, df2: pd.DataFrame, title: str) -> None:
    """
    Plots gamma-ray (GR) logs from the provided DataFrame on the specified axes.

    Args:
        df (pd.DataFrame): DataFrame containing the well log data, 
            where 'GR' represents gamma-ray values and 'TDEP' represents depth values.
        df2 (pd.DataFrame): DataFrame containing the well log data, 
            where 'GR' represents gamma-ray values and 'TDEP' represents depth values.
        title (str): Title for the plot.

    Returns:
        None
    """
    fig, ax = plt.subplots(1, 1, figsize=(4, df['TDEP'].max()//14))

    # Extract GR and TDEP values for plotting the GR log in the range 0 to 150
    x_0_150 = df['GR']
    y_0_150 = df['TDEP']
    x2_0_150 = df2['GR']
    y2_0_150 = df2['TDEP']

    # Create a copy of the DataFrame to adjust GR values for the range 150 to 300
    df_150_300 = df.copy()
    df_150_300['GR'] = df_150_300['GR'] - 150
    x_150_300 = df_150_300['GR']
    y_150_300 = df_150_300['TDEP']

    df2_150_300 = df2.copy()
    df2_150_300['GR'] = df2_150_300['GR'] - 150
    x2_150_300 = df2_150_300['GR']
    y2_150_300 = df2_150_300['TDEP']

    # Plot the original GR logs (0 to 150 range) with blue color
    ax.plot(x_0_150, y_0_150, label=f'GR 1', color='blue', linewidth=0.75, zorder=3)

    # Plot the adjusted GR logs (150 to 300 range) with the same color and style
    ax.plot(x_150_300, y_150_300, color='blue', linewidth=0.75, zorder=3)

    # Plot the original GR logs (0 to 150 range) with blue color
    ax.plot(x2_0_150, y2_0_150, label='GR 2', color='red', linewidth=1.5, zorder=2)

    # Plot the adjusted GR logs (150 to 300 range) with the same color and style
    ax.plot(x2_150_300, y2_150_300, color='red', linewidth=1.5, zorder=2)

    # Set the X-axis ticks and labels for both GR ranges (0-150 and 150-300)
    ticks_x_axis = [0,  15,  30,  45,  60,  75,  90, 105, 120, 135, 150]
    labels_x_axis = ['0\n150', '15\n165', '30\n180', '45\n195', '60\n210', 
                     '75\n225', '90\n240', '105\n255', '120\n270', '135\n285', '150\n300']
    ax.set_xticks(ticks_x_axis)
    ax.set_xticklabels(labels_x_axis)

    # Position X-axis ticks and labels at the top of the plot
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')

    # Format the Y-axis tick labels to display intervals of 50
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:.0f}' if x % 50 == 0 else ''))

    # Disable X-axis and Y-axis tick markers (removes small tick lines)
    ax.tick_params(axis='x', which='both', bottom=False, top=False)
    ax.tick_params(axis='y', which='both', left=False, right=False)

    # Add gridlines to the plot
    ax.grid(True, axis='both', zorder=0)

    # Set the gridline interval on the Y-axis
    ax.yaxis.set_major_locator(plt.MultipleLocator(5))

    # Set X-axis limits to restrict the GR range from 0 to 150
    ax.set_xlim(0, 150)
    ax.set_ylim(0, df['TDEP'].max())

    # Invert the Y-axis to represent depth increasing downwards
    ax.invert_yaxis()

    # Add title and labels to the X and Y axes with bold font
    ax.set_title(title, fontweight='bold')
    ax.set_xlabel('GR', fontweight='bold')
    ax.set_ylabel('TDEP', fontweight='bold')

    # Display the legend for the GR log
    ax.legend()


def plot_gr_logs_5_runs(df_spliced: pd.DataFrame, 
                        df2: pd.DataFrame,
                        df3: pd.DataFrame,
                        df4: pd.DataFrame,
                        df5: pd.DataFrame, 
                        title: str) -> None:
    """
    Plots gamma-ray (GR) logs from the provided DataFrames on the specified axes.

    Args:
        df_spliced (pd.DataFrame): DataFrame containing the well log data, 
            where 'GR' represents gamma-ray values and 'TDEP' represents depth values.
        df2 (pd.DataFrame): DataFrame containing the well log data, 
            where 'GR' represents gamma-ray values and 'TDEP' represents depth values.
        df3 (pd.DataFrame): DataFrame containing the well log data, 
            where 'GR' represents gamma-ray values and 'TDEP' represents depth values.
        df4 (pd.DataFrame): DataFrame containing the well log data, 
            where 'GR' represents gamma-ray values and 'TDEP' represents depth values.
        df5 (pd.DataFrame): DataFrame containing the well log data, 
            where 'GR' represents gamma-ray values and 'TDEP' represents depth values.
        title (str): Title for the plot.

    Returns:
        None
    """
    fig, ax = plt.subplots(1, 1, figsize=(4, df_spliced['TDEP'].max()//14))

    # Extract GR and TDEP values for plotting the GR log in the range 0 to 150
    x_0_150 = df_spliced['GR']
    y_0_150 = df_spliced['TDEP']

    # Create a copy of the DataFrame to adjust GR values for the range 150 to 300
    df_150_300 = df_spliced.copy()
    df_150_300['GR'] = df_150_300['GR'] - 150
    x_150_300 = df_150_300['GR']
    y_150_300 = df_150_300['TDEP']

    # Plot the original GR logs (0 to 150 range) with blue color
    ax.plot(x_0_150, y_0_150, label=f'GR Emendado', color='black', linewidth=0.5, linestyle='--', zorder=5)

    # Plot the adjusted GR logs (150 to 300 range) with the same color and style
    ax.plot(x_150_300, y_150_300, color='black', linewidth=0.5, linestyle='--', zorder=5)

    # Extract GR and TDEP values for plotting the GR log in the range 0 to 150
    x2_0_150 = df2['GR']
    y2_0_150 = df2['TDEP']

    # Create a copy of the DataFrame to adjust GR values for the range 150 to 300
    df2_150_300 = df2.copy()
    df2_150_300['GR'] = df2_150_300['GR'] - 150
    x2_150_300 = df2_150_300['GR']
    y2_150_300 = df2_150_300['TDEP']

    # Plot the original GR logs (0 to 150 range) with red color
    ax.plot(x2_0_150, y2_0_150, label='GR 1', color='salmon', linewidth=1, zorder=4)

    # Plot the adjusted GR logs (150 to 300 range) with the same color and style
    ax.plot(x2_150_300, y2_150_300, color='salmon', linewidth=1, zorder=4)

    # Extract GR and TDEP values for plotting the GR log in the range 0 to 150
    x3_0_150 = df3['GR']
    y3_0_150 = df3['TDEP']

    # Create a copy of the DataFrame to adjust GR values for the range 150 to 300
    df3_150_300 = df3.copy()
    df3_150_300['GR'] = df3_150_300['GR'] - 150
    x3_150_300 = df3_150_300['GR']
    y3_150_300 = df3_150_300['TDEP']

    # Plot the original GR logs (0 to 150 range) with blue color
    ax.plot(x3_0_150, y3_0_150, label='GR 2', color='lightblue', linewidth=1.5, zorder=3)

    # Plot the adjusted GR logs (150 to 300 range) with the same color and style
    ax.plot(x3_150_300, y3_150_300, color='lightblue', linewidth=1.5, zorder=3)

        # Extract GR and TDEP values for plotting the GR log in the range 0 to 150
    x4_0_150 = df4['GR']
    y4_0_150 = df4['TDEP']

    # Create a copy of the DataFrame to adjust GR values for the range 150 to 300
    df4_150_300 = df4.copy()
    df4_150_300['GR'] = df4_150_300['GR'] - 150
    x4_150_300 = df4_150_300['GR']
    y4_150_300 = df4_150_300['TDEP']

    # Plot the original GR logs (0 to 150 range) with green color
    ax.plot(x4_0_150, y4_0_150, label='GR 3', color='lightgreen', linewidth=2, zorder=2)

    # Plot the adjusted GR logs (150 to 300 range) with the same color and style
    ax.plot(x4_150_300, y4_150_300, color='lightgreen', linewidth=2, zorder=2)

        # Extract GR and TDEP values for plotting the GR log in the range 0 to 150
    x5_0_150 = df5['GR']
    y5_0_150 = df5['TDEP']

    # Create a copy of the DataFrame to adjust GR values for the range 150 to 300
    df5_150_300 = df5.copy()
    df5_150_300['GR'] = df5_150_300['GR'] - 150
    x5_150_300 = df5_150_300['GR']
    y5_150_300 = df5_150_300['TDEP']

    # Plot the original GR logs (0 to 150 range) with red color
    ax.plot(x5_0_150, y5_0_150, label='GR 4', color='yellow', linewidth=2.5, zorder=1)

    # Plot the adjusted GR logs (150 to 300 range) with the same color and style
    ax.plot(x5_150_300, y5_150_300, color='yellow', linewidth=2.5, zorder=1)

    # Set the X-axis ticks and labels for both GR ranges (0-150 and 150-300)
    ticks_x_axis = [0,  15,  30,  45,  60,  75,  90, 105, 120, 135, 150]
    labels_x_axis = ['0\n150', '15\n165', '30\n180', '45\n195', '60\n210', 
                     '75\n225', '90\n240', '105\n255', '120\n270', '135\n285', '150\n300']
    ax.set_xticks(ticks_x_axis)
    ax.set_xticklabels(labels_x_axis)

    # Position X-axis ticks and labels at the top of the plot
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')

    # Format the Y-axis tick labels to display intervals of 50
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:.0f}' if x % 50 == 0 else ''))

    # Disable X-axis and Y-axis tick markers (removes small tick lines)
    ax.tick_params(axis='x', which='both', bottom=False, top=False)
    ax.tick_params(axis='y', which='both', left=False, right=False)

    # Add gridlines to the plot
    ax.grid(True, axis='both', zorder=0)

    # Set the gridline interval on the Y-axis
    ax.yaxis.set_major_locator(plt.MultipleLocator(5))

    # Set X-axis limits to restrict the GR range from 0 to 150
    ax.set_xlim(0, 150)
    ax.set_ylim(0, df_spliced['TDEP'].max())

    # Invert the Y-axis to represent depth increasing downwards
    ax.invert_yaxis()

    # Add title and labels to the X and Y axes with bold font
    ax.set_title(title, fontweight='bold')
    ax.set_xlabel('GR', fontweight='bold')
    ax.set_ylabel('TDEP', fontweight='bold')

    # Display the legend for the GR log
    ax.legend()


def plot_gr_logs_4_runs(df_spliced: pd.DataFrame, 
                        df2: pd.DataFrame,
                        df3: pd.DataFrame,
                        df4: pd.DataFrame,
                        df5: pd.DataFrame, 
                        title: str) -> None:
    """
    Plots gamma-ray (GR) logs from the provided DataFrames on the specified axes.

    Args:
        df_spliced (pd.DataFrame): DataFrame containing the well log data, 
            where 'GR' represents gamma-ray values and 'TDEP' represents depth values.
        df2 (pd.DataFrame): DataFrame containing the well log data, 
            where 'GR' represents gamma-ray values and 'TDEP' represents depth values.
        df3 (pd.DataFrame): DataFrame containing the well log data, 
            where 'GR' represents gamma-ray values and 'TDEP' represents depth values.
        df4 (pd.DataFrame): DataFrame containing the well log data, 
            where 'GR' represents gamma-ray values and 'TDEP' represents depth values.
        df5 (pd.DataFrame): DataFrame containing the well log data, 
            where 'GR' represents gamma-ray values and 'TDEP' represents depth values.
        title (str): Title for the plot.

    Returns:
        None
    """
    fig, ax = plt.subplots(1, 1, figsize=(4, df_spliced['TDEP'].max()//14))

    # Extract GR and TDEP values for plotting the GR log in the range 0 to 150
    x2_0_150 = df2['GR']
    y2_0_150 = df2['TDEP']

    # Create a copy of the DataFrame to adjust GR values for the range 150 to 300
    df2_150_300 = df2.copy()
    df2_150_300['GR'] = df2_150_300['GR'] - 150
    x2_150_300 = df2_150_300['GR']
    y2_150_300 = df2_150_300['TDEP']

    # Plot the original GR logs (0 to 150 range) with red color
    ax.plot(x2_0_150, y2_0_150, label='GR 1', color='red', linewidth=1, zorder=4)

    # Plot the adjusted GR logs (150 to 300 range) with the same color and style
    ax.plot(x2_150_300, y2_150_300, color='red', linewidth=1, zorder=4)

    # Extract GR and TDEP values for plotting the GR log in the range 0 to 150
    x3_0_150 = df3['GR']
    y3_0_150 = df3['TDEP']

    # Create a copy of the DataFrame to adjust GR values for the range 150 to 300
    df3_150_300 = df3.copy()
    df3_150_300['GR'] = df3_150_300['GR'] - 150
    x3_150_300 = df3_150_300['GR']
    y3_150_300 = df3_150_300['TDEP']

    # Plot the original GR logs (0 to 150 range) with blue color
    ax.plot(x3_0_150, y3_0_150, label='GR 2', color='blue', linewidth=1.5, zorder=3)

    # Plot the adjusted GR logs (150 to 300 range) with the same color and style
    ax.plot(x3_150_300, y3_150_300, color='blue', linewidth=1.5, zorder=3)

        # Extract GR and TDEP values for plotting the GR log in the range 0 to 150
    x4_0_150 = df4['GR']
    y4_0_150 = df4['TDEP']

    # Create a copy of the DataFrame to adjust GR values for the range 150 to 300
    df4_150_300 = df4.copy()
    df4_150_300['GR'] = df4_150_300['GR'] - 150
    x4_150_300 = df4_150_300['GR']
    y4_150_300 = df4_150_300['TDEP']

    # Plot the original GR logs (0 to 150 range) with green color
    ax.plot(x4_0_150, y4_0_150, label='GR 3', color='green', linewidth=2, zorder=2)

    # Plot the adjusted GR logs (150 to 300 range) with the same color and style
    ax.plot(x4_150_300, y4_150_300, color='green', linewidth=2, zorder=2)

        # Extract GR and TDEP values for plotting the GR log in the range 0 to 150
    x5_0_150 = df5['GR']
    y5_0_150 = df5['TDEP']

    # Create a copy of the DataFrame to adjust GR values for the range 150 to 300
    df5_150_300 = df5.copy()
    df5_150_300['GR'] = df5_150_300['GR'] - 150
    x5_150_300 = df5_150_300['GR']
    y5_150_300 = df5_150_300['TDEP']

    # Plot the original GR logs (0 to 150 range) with red color
    ax.plot(x5_0_150, y5_0_150, label='GR 4', color='yellow', linewidth=2.5, zorder=1)

    # Plot the adjusted GR logs (150 to 300 range) with the same color and style
    ax.plot(x5_150_300, y5_150_300, color='yellow', linewidth=2.5, zorder=1)

    # Set the X-axis ticks and labels for both GR ranges (0-150 and 150-300)
    ticks_x_axis = [0,  15,  30,  45,  60,  75,  90, 105, 120, 135, 150]
    labels_x_axis = ['0\n150', '15\n165', '30\n180', '45\n195', '60\n210', 
                     '75\n225', '90\n240', '105\n255', '120\n270', '135\n285', '150\n300']
    ax.set_xticks(ticks_x_axis)
    ax.set_xticklabels(labels_x_axis)

    # Position X-axis ticks and labels at the top of the plot
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')

    # Format the Y-axis tick labels to display intervals of 50
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:.0f}' if x % 50 == 0 else ''))

    # Disable X-axis and Y-axis tick markers (removes small tick lines)
    ax.tick_params(axis='x', which='both', bottom=False, top=False)
    ax.tick_params(axis='y', which='both', left=False, right=False)

    # Add gridlines to the plot
    ax.grid(True, axis='both', zorder=0)

    # Set the gridline interval on the Y-axis
    ax.yaxis.set_major_locator(plt.MultipleLocator(5))

    # Set X-axis limits to restrict the GR range from 0 to 150
    ax.set_xlim(0, 150)
    ax.set_ylim(0, df_spliced['TDEP'].max())

    # Invert the Y-axis to represent depth increasing downwards
    ax.invert_yaxis()

    # Add title and labels to the X and Y axes with bold font
    ax.set_title(title, fontweight='bold')
    ax.set_xlabel('GR', fontweight='bold')
    ax.set_ylabel('TDEP', fontweight='bold')

    # Display the legend for the GR log
    ax.legend()


def plot_combined(df, df2, df_spliced, df3, df4, df5, df6, title1, title2, fundo):
    """
    Combines two plots (linear RES logs and GR logs) side by side in a single figure.

    Args:
        df, df2 (pd.DataFrame): DataFrames for the linear RES logs.
        df_spliced, df3, df4, df5 (pd.DataFrame): DataFrames for the GR logs.
        title1, title2 (str): Titles for the two plots.

    Returns:
        None
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, fundo // 14), sharey=True)
    
    # Plot linear RES logs
    ax1 = axes[0]
    x = df['ILD']
    y = df['TDEP']
    x_2 = df2['ILD']
    y_2 = df2['TDEP']
    x_spliced = df_spliced['ILD']
    y_spliced = df_spliced['TDEP']

    ax1.plot(x, y, label='ILD 1', color='lightgreen', linewidth=0.75, zorder=1)
    ax1.plot(x_2, y_2, label='ILD 2', color='lightgreen', linewidth=0.75, zorder=1)
    ax1.plot(x_spliced, y_spliced, label='ILD spliced', color='black', linestyle='--', linewidth=0.75, zorder=2)
    # Set the X-axis ticks and labels for both res ranges 
    sequence = np.arange(-0.7, 1.41, 0.11) 
    ax1.set_xticks(sequence)

    # Position X-axis ticks and labels at the top of the plot
    ax1.xaxis.set_ticks_position('top')
    ax1.xaxis.set_label_position('top')

    # Format the Y-axis tick labels to display intervals of 50
    ax1.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:.0f}' if x % 50 == 0 else ''))

    # Disable X-axis and Y-axis tick markers (removes small tick lines)
    ax1.tick_params(axis='x', which='both', bottom=False, top=False)
    ax1.tick_params(axis='y', which='both', left=False, right=False)

    # Add gridlines to the plot
    ax1.grid(True, axis='both', zorder=0)

    # Set the gridline interval on the Y-axis
    ax1.yaxis.set_major_locator(plt.MultipleLocator(5))

    # Set X-axis limits to restrict the GR range from 0 to 150
    ax1.set_xlim(-0.7, 1.3)
    ax1.set_ylim(0, df['TDEP'].max())

    # Invert the Y-axis to represent depth increasing downwards
    ax1.invert_yaxis()

    # Add title and labels to the X and Y axes with bold font
    ax1.set_title(title1, fontweight='bold')
    ax1.set_xlabel('ILD', fontweight='bold')
    ax1.set_ylabel('TDEP', fontweight='bold')
    ax1.legend()

    # Plot GR logs
    ax2 = axes[1]

        # Set the X-axis ticks and labels for both GR ranges (0-150 and 150-300)
    ticks_x_axis = [0,  15,  30,  45,  60,  75,  90, 105, 120, 135, 150]
    labels_x_axis = ['0\n150', '15\n165', '30\n180', '45\n195', '60\n210', 
                     '75\n225', '90\n240', '105\n255', '120\n270', '135\n285', '150\n300']
    ax2.set_xticks(ticks_x_axis)
    ax2.set_xticklabels(labels_x_axis)

    # Position X-axis ticks and labels at the top of the plot
    ax2.xaxis.set_ticks_position('top')
    ax2.xaxis.set_label_position('top')

    for df_gr, color, label in zip([df3, df4, df5, df6], ['lightblue', 'lightgreen', 'yellow', 'salmon'], ['GR 1', 'GR 2', 'GR 3', 'GR 4']):
        x_gr_0_150 = df_gr['GR']
        y_gr_0_150 = df_gr['TDEP']

        df_gr_150_300 = df_gr.copy()
        df_gr_150_300['GR'] = df_gr_150_300['GR'] - 150
        x_gr_150_300 = df_gr_150_300['GR']
        y_gr_150_300 = df_gr_150_300['TDEP']

        ax2.plot(x_gr_0_150, y_gr_0_150, label=label, color=color, linewidth=1.5)
        ax2.plot(x_gr_150_300, y_gr_150_300, color=color, linewidth=1.5)

    x_0_150 = df_spliced['GR']
    y_0_150 = df_spliced['TDEP']

    df_150_300 = df_spliced.copy()
    df_150_300['GR'] = df_150_300['GR'] - 150
    x_150_300 = df_150_300['GR']
    y_150_300 = df_150_300['TDEP']

    ax2.plot(x_0_150, y_0_150, label='GR Emendado', color='black', linewidth=0.5, linestyle='--', zorder=5)
    ax2.plot(x_150_300, y_150_300, color='black', linewidth=0.5, linestyle='--', zorder=5)

    ax2.set_title(title2, fontweight='bold')
    ax2.set_xlabel('GR', fontweight='bold')
    # Format the Y-axis tick labels to display intervals of 50
    ax2.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:.0f}' if x % 50 == 0 else ''))

    # Disable X-axis and Y-axis tick markers (removes small tick lines)
    ax2.tick_params(axis='x', which='both', bottom=False, top=False)
    ax2.tick_params(axis='y', which='both', left=False, right=False)

    # Add gridlines to the plot
    ax2.grid(True, axis='both', zorder=0)

    # Set the gridline interval on the Y-axis
    ax2.yaxis.set_major_locator(plt.MultipleLocator(5))
    ax2.set_xlim(0, 150)
    ax2.set_ylim(0, df_spliced['TDEP'].max())

        # Invert the Y-axis to represent depth increasing downwards
    ax2.invert_yaxis()
    ax2.legend()

    # Adjust spacing between subplots
    plt.tight_layout()


def plot_nphi_logs_3_runs(
        df: pd.DataFrame,
        df2: pd.DataFrame,
        df3: pd.DataFrame, 
        title: str) -> None:
    """
    Plots NPHI (Neutron Porosity) logs for three data runs from the provided DataFrames.

    Args:
        df (pd.DataFrame): DataFrame containing the primary well log data. 
            Must include columns 'NPHI' (neutron porosity values) and 'TDEP' (depth values).
        df2 (pd.DataFrame): DataFrame containing the first additional run of NPHI log data.
            Must include columns 'NPHI' and 'TDEP'.
        df3 (pd.DataFrame): DataFrame containing the second additional run of NPHI log data.
            Must include columns 'NPHI' and 'TDEP'.
        title (str): Title for the plot.

    Returns:
        None: The function generates and displays a plot but does not return any value.
    """
    fig, ax = plt.subplots(1, 1, figsize=(8, df['TDEP'].max()//14))

    # Extract NPHI and TDEP values for plotting the NPHI logs
    x = df['NPHI']
    y = df['TDEP']
    x_2 = df2['NPHI']
    y_2 = df2['TDEP']
    x_3 = df3['NPHI']
    y_3 = df3['TDEP']

    # Plot the original NPHI logs with 
    ax.plot(x, y, label='NPHI Emendado', color='black', linewidth=1.25, zorder=2)
    ax.plot(x_2, y_2, label='Corrida 1', color='lightgreen', linestyle='--', linewidth=0.75, zorder=3)
    ax.plot(x_3, y_3, label='Corrida 2', color='lightgreen', linestyle='--', linewidth=0.75, zorder=3)

    # Set the X-axis ticks and labels for both NPHI ranges 
    ticks_x_axis = list(range(-15, 46, 3))
    ax.set_xticks(ticks_x_axis)

    # Position X-axis ticks and labels at the top of the plot
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')

    # Format the Y-axis tick labels to display intervals of 50
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:.0f}' if x % 50 == 0 else ''))

    # Disable X-axis and Y-axis tick markers (removes small tick lines)
    ax.tick_params(axis='x', which='both', bottom=False, top=False)
    ax.tick_params(axis='y', which='both', left=False, right=False)

    # Add gridlines to the plot
    ax.grid(True, axis='both', zorder=0)

    # Set the gridline interval on the Y-axis
    ax.yaxis.set_major_locator(plt.MultipleLocator(5))

    # Set X-axis limits to restrict the GR range from 0 to 150
    ax.set_xlim(-15, 45)
    ax.set_ylim(0, df['TDEP'].max())

    # Invert the Y-axis to represent depth increasing downwards
    ax.invert_yaxis()
    ax.invert_xaxis()

    # Add title and labels to the X and Y axes with bold font
    ax.set_title(title, fontweight='bold')
    ax.set_xlabel('NPHI', fontweight='bold')
    ax.set_ylabel('TDEP', fontweight='bold')

    # Display the legend for the GR log
    ax.legend()


def plot_cali_logs_4_runs(df_spliced: pd.DataFrame, 
                        df2: pd.DataFrame,
                        df3: pd.DataFrame,
                        df4: pd.DataFrame,
                        df5: pd.DataFrame, 
                        title: str) -> None:
    fig, ax = plt.subplots(1, 1, figsize=(4, df_spliced['TDEP'].max()//14))

    # Extract GR and TDEP values for plotting the GR log in the range 0 to 150
    x2_0_150 = df2['CALI']
    y2_0_150 = df2['TDEP']

    # Create a copy of the DataFrame to adjust GR values for the range 150 to 300
    df2_150_300 = df2.copy()
    df2_150_300['CALI'] = df2_150_300['CALI'] - 10
    x2_150_300 = df2_150_300['CALI']
    y2_150_300 = df2_150_300['TDEP']

    # Plot the original GR logs (0 to 150 range) with red color
    ax.plot(x2_0_150, y2_0_150, label='Corrida 1', color='red', linewidth=1, zorder=4)

    # Plot the adjusted GR logs (150 to 300 range) with the same color and style
    ax.plot(x2_150_300, y2_150_300, color='red', linewidth=1, zorder=4)

    # Extract GR and TDEP values for plotting the GR log in the range 0 to 150
    x3_0_150 = df3['CALI']
    y3_0_150 = df3['TDEP']

    # Create a copy of the DataFrame to adjust GR values for the range 150 to 300
    df3_150_300 = df3.copy()
    df3_150_300['CALI'] = df3_150_300['CALI'] - 10
    x3_150_300 = df3_150_300['CALI']
    y3_150_300 = df3_150_300['TDEP']

    # Plot the original GR logs (0 to 150 range) with blue color
    ax.plot(x3_0_150, y3_0_150, label='Corrida 2', color='blue', linewidth=1.5, zorder=3)

    # Plot the adjusted GR logs (150 to 300 range) with the same color and style
    ax.plot(x3_150_300, y3_150_300, color='blue', linewidth=1.5, zorder=3)

        # Extract GR and TDEP values for plotting the GR log in the range 0 to 150
    x4_0_150 = df4['CALI']
    y4_0_150 = df4['TDEP']

    # Create a copy of the DataFrame to adjust GR values for the range 150 to 300
    df4_150_300 = df4.copy()
    df4_150_300['CALI'] = df4_150_300['CALI'] - 10
    x4_150_300 = df4_150_300['CALI']
    y4_150_300 = df4_150_300['TDEP']

    # Plot the original GR logs (0 to 150 range) with green color
    ax.plot(x4_0_150, y4_0_150, label='Corrida 3', color='green', linewidth=2, zorder=2)

    # Plot the adjusted GR logs (150 to 300 range) with the same color and style
    ax.plot(x4_150_300, y4_150_300, color='green', linewidth=2, zorder=2)

        # Extract GR and TDEP values for plotting the GR log in the range 0 to 150
    x5_0_150 = df5['CALI']
    y5_0_150 = df5['TDEP']

    # Create a copy of the DataFrame to adjust GR values for the range 150 to 300
    df5_150_300 = df5.copy()
    df5_150_300['CALI'] = df5_150_300['CALI'] - 10
    x5_150_300 = df5_150_300['CALI']
    y5_150_300 = df5_150_300['TDEP']

    # Plot the original GR logs (0 to 150 range) with red color
    ax.plot(x5_0_150, y5_0_150, label='Corrida 4', color='yellow', linewidth=2.5, zorder=1)

    # Plot the adjusted GR logs (150 to 300 range) with the same color and style
    ax.plot(x5_150_300, y5_150_300, color='yellow', linewidth=2.5, zorder=1)

    # Set the X-axis ticks and labels for both GR ranges (0-150 and 150-300)
    ticks_x_axis = [6,  7,  8,  9,  10,  11,  12, 13, 14, 15, 16]
    labels_x_axis = ['6\n16', '7\n17', '8\n18', '9\n19', '10\n20', 
                     '11\n21', '12\n22', '13\n23', '14\n24', '15\n25', '16\n26']
    ax.set_xticks(ticks_x_axis)
    ax.set_xticklabels(labels_x_axis)

    # Position X-axis ticks and labels at the top of the plot
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')

    # Format the Y-axis tick labels to display intervals of 50
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:.0f}' if x % 50 == 0 else ''))

    # Disable X-axis and Y-axis tick markers (removes small tick lines)
    ax.tick_params(axis='x', which='both', bottom=False, top=False)
    ax.tick_params(axis='y', which='both', left=False, right=False)

    # Add gridlines to the plot
    ax.grid(True, axis='both', zorder=0)

    # Set the gridline interval on the Y-axis
    ax.yaxis.set_major_locator(plt.MultipleLocator(5))

    # Set X-axis limits to restrict the GR range from 0 to 150
    ax.set_xlim(6, 16)
    ax.set_ylim(0, df_spliced['TDEP'].max())

    # Invert the Y-axis to represent depth increasing downwards
    ax.invert_yaxis()

    # Add title and labels to the X and Y axes with bold font
    ax.set_title(title, fontweight='bold')
    ax.set_xlabel('CALI', fontweight='bold')
    ax.set_ylabel('TDEP', fontweight='bold')

    # Display the legend for the GR log
    ax.legend()



def plot_cali_logs_5_runs(df_spliced: pd.DataFrame, 
                        df2: pd.DataFrame,
                        df3: pd.DataFrame,
                        df4: pd.DataFrame,
                        df5: pd.DataFrame, 
                        title: str) -> None:

    fig, ax = plt.subplots(1, 1, figsize=(4, df_spliced['TDEP'].max()//14))

    # Extract CALI and TDEP values for plotting the GR log in the range 0 to 150
    x_0_150 = df_spliced['CALI']
    y_0_150 = df_spliced['TDEP']

    # Create a copy of the DataFrame to adjust GR values for the range 150 to 300
    df_150_300 = df_spliced.copy()
    df_150_300['CALI'] = df_150_300['CALI'] - 10
    x_150_300 = df_150_300['CALI']
    y_150_300 = df_150_300['TDEP']

    # Plot the original GR logs (0 to 150 range) with blue color
    ax.plot(x_0_150, y_0_150, label=f'CALI Emendado', color='black', linewidth=1.25, zorder=1)

    # Plot the adjusted GR logs (150 to 300 range) with the same color and style
    ax.plot(x_150_300, y_150_300, color='black', linewidth=1.25, zorder=1)

    # Extract GR and TDEP values for plotting the GR log in the range 0 to 150
    x2_0_150 = df2['CALI']
    y2_0_150 = df2['TDEP']

    # Create a copy of the DataFrame to adjust GR values for the range 150 to 300
    df2_150_300 = df2.copy()
    df2_150_300['CALI'] = df2_150_300['CALI'] - 10
    x2_150_300 = df2_150_300['CALI']
    y2_150_300 = df2_150_300['TDEP']

    # Plot the original GR logs (0 to 150 range) with red color
    ax.plot(x2_0_150, y2_0_150, label='Corrida 1', color='salmon', linewidth=0.75, linestyle='--', zorder=2)

    # Plot the adjusted GR logs (150 to 300 range) with the same color and style
    ax.plot(x2_150_300, y2_150_300, color='salmon', linewidth=0.75, linestyle='--', zorder=2)

    # Extract GR and TDEP values for plotting the GR log in the range 0 to 150
    x3_0_150 = df3['CALI']
    y3_0_150 = df3['TDEP']

    # Create a copy of the DataFrame to adjust GR values for the range 150 to 300
    df3_150_300 = df3.copy()
    df3_150_300['CALI'] = df3_150_300['CALI'] - 10
    x3_150_300 = df3_150_300['CALI']
    y3_150_300 = df3_150_300['TDEP']

    # Plot the original GR logs (0 to 150 range) with blue color
    ax.plot(x3_0_150, y3_0_150, label='Corrida 2', color='lightblue', linewidth=0.75, linestyle='--', zorder=3)

    # Plot the adjusted GR logs (150 to 300 range) with the same color and style
    ax.plot(x3_150_300, y3_150_300, color='lightblue', linewidth=0.75, linestyle='--', zorder=3)

        # Extract GR and TDEP values for plotting the GR log in the range 0 to 150
    x4_0_150 = df4['CALI']
    y4_0_150 = df4['TDEP']

    # Create a copy of the DataFrame to adjust GR values for the range 150 to 300
    df4_150_300 = df4.copy()
    df4_150_300['CALI'] = df4_150_300['CALI'] - 10
    x4_150_300 = df4_150_300['CALI']
    y4_150_300 = df4_150_300['TDEP']

    # Plot the original GR logs (0 to 150 range) with green color
    ax.plot(x4_0_150, y4_0_150, label='Corrida 3', color='lightgreen', linewidth=0.75, linestyle='--', zorder=4)

    # Plot the adjusted GR logs (150 to 300 range) with the same color and style
    ax.plot(x4_150_300, y4_150_300, color='lightgreen', linewidth=0.75, linestyle='--', zorder=4)

        # Extract GR and TDEP values for plotting the GR log in the range 0 to 150
    x5_0_150 = df5['CALI']
    y5_0_150 = df5['TDEP']

    # Create a copy of the DataFrame to adjust GR values for the range 150 to 300
    df5_150_300 = df5.copy()
    df5_150_300['CALI'] = df5_150_300['CALI'] - 10
    x5_150_300 = df5_150_300['CALI']
    y5_150_300 = df5_150_300['TDEP']

    # Plot the original GR logs (0 to 150 range) with red color
    ax.plot(x5_0_150, y5_0_150, label='Corrida 4', color='yellow', linewidth=0.75, linestyle='--', zorder=5)

    # Plot the adjusted GR logs (150 to 300 range) with the same color and style
    ax.plot(x5_150_300, y5_150_300, color='yellow', linewidth=0.75, linestyle='--', zorder=5)

    # Set the X-axis ticks and labels for both GR ranges (0-150 and 150-300)
    ticks_x_axis = [6,  7,  8,  9,  10,  11,  12, 13, 14, 15, 16]
    labels_x_axis = ['6\n16', '7\n17', '8\n18', '9\n19', '10\n20', 
                     '11\n21', '12\n22', '13\n23', '14\n24', '15\n25', '16\n26']
    ax.set_xticks(ticks_x_axis)
    ax.set_xticklabels(labels_x_axis)

    # Position X-axis ticks and labels at the top of the plot
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')

    # Format the Y-axis tick labels to display intervals of 50
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:.0f}' if x % 50 == 0 else ''))

    # Disable X-axis and Y-axis tick markers (removes small tick lines)
    ax.tick_params(axis='x', which='both', bottom=False, top=False)
    ax.tick_params(axis='y', which='both', left=False, right=False)

    # Add gridlines to the plot
    ax.grid(True, axis='both', zorder=0)

    # Set the gridline interval on the Y-axis
    ax.yaxis.set_major_locator(plt.MultipleLocator(5))

    # Set X-axis limits to restrict the GR range from 0 to 150
    ax.set_xlim(6, 16)
    ax.set_ylim(0, df_spliced['TDEP'].max())

    # Invert the Y-axis to represent depth increasing downwards
    ax.invert_yaxis()

    # Add title and labels to the X and Y axes with bold font
    ax.set_title(title, fontweight='bold')
    ax.set_xlabel('CALI', fontweight='bold')
    ax.set_ylabel('TDEP', fontweight='bold')

    # Display the legend for the GR log
    ax.legend()
