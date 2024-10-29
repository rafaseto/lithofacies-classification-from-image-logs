import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


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
    ax.plot(x_0_150, y_0_150, label=f'GR Emendado', color='black', linewidth=0.5, zorder=5)

    # Plot the adjusted GR logs (150 to 300 range) with the same color and style
    ax.plot(x_150_300, y_150_300, color='black', linewidth=0.5, zorder=5)

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