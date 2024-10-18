from typing import List, Dict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os

def logical_files_to_ndarray(logical_files: List[object]) -> Dict[int, Dict[int, np.ndarray]]:
    """
    Receives the well's logical files and creates a dictionary to store the frame data.

    Args:
        logical_files (List[object]): A list of logical file objects, each containing multiple frames.

    Returns:
        Dict[int, Dict[int, np.ndarray]]: A nested dictionary where the outer keys represent the 
        logical file index and the inner keys represent frame indices, each associated with 
        NumPy arrays of curve data.
    """
    logical_files_dict = {}
    logical_file_index = 0

    for logical_file in logical_files:
        
        logical_file_dict = {}

        for frame in logical_file.frames:
            frame_index = logical_file.frames.index(frame)

            curves = frame.curves()

            logical_file_dict[frame_index] = curves
        
        logical_files_dict[logical_file_index] = logical_file_dict
        logical_file_index += 1

    return logical_files_dict

def ndarray_to_dataframe(logical_files_dict: Dict[int, Dict[int, np.ndarray]]) -> Dict[int, Dict[int, pd.DataFrame]]:
    """
    Converts a dictionary of NumPy arrays (representing well log frames) into a dictionary of pandas DataFrames.

    Args:
        logical_files_dict (Dict[int, Dict[int, np.ndarray]]): A nested dictionary where the outer keys represent 
        the logical file index and the inner keys represent frame indices, each associated with NumPy arrays 
        of curve data.

    Returns:
        Dict[int, Dict[int, pd.DataFrame]]: A nested dictionary where the outer keys represent the logical file 
        index and the inner keys represent frame indices, each associated with pandas DataFrames, where the 
        columns correspond to the curve names and the rows correspond to the data points.
    """
    logical_file_index = 0
    logical_files_df_dict = {}

    for logical_file in logical_files_dict.values():
        
        dataframe_dict = {}
        frame_index = 0

        for frame in logical_file.values():
            i = 0
            channel_names = frame.dtype.names  # Extract the names of the data channels (columns)
            frame_dict = {}

            for channel_name in channel_names:
                curves = [t[i] for t in frame]  # Extract data points for each curve (column)
                frame_dict[channel_name] = curves
                i += 1

            dataframe_dict[frame_index] = pd.DataFrame(frame_dict)  # Convert the curve data into a DataFrame
            frame_index += 1

        logical_files_df_dict[logical_file_index] = dataframe_dict
        logical_file_index += 1

    return logical_files_df_dict


def dataframes_to_csv(well_df_dict: Dict[str, Dict[int, Dict[int, pd.DataFrame]]], base_dir: str = "../data/csv_from_dlis") -> None: 
    """
    Saves each DataFrame from a nested dictionary of wells, logical files, and frames to separate CSV files.

    Args:
        well_df_dict (Dict[str, Dict[int, Dict[int, pd.DataFrame]]]): A nested dictionary where:
            - The outer keys are well names (str),
            - The second-level keys are logical file indices (int),
            - The third-level keys are frame indices (int),
            - The values are pandas DataFrames containing well log data.
        base_dir (str): The base directory where the CSV files will be saved. Defaults to '../data/csv_from_dlis'.

    Returns:
        None: The function saves CSV files and does not return any value.
    """
    for well_name, logical_files_df_dict in well_df_dict.items():
        for logical_file_index, logical_file_dfs in logical_files_df_dict.items():
            for frame_index, frame_df in logical_file_dfs.items():
                
                # Create the full file path for saving the CSV
                file_path = f"{base_dir}/{well_name}/logical_file_{logical_file_index}/frame_{frame_index}.csv"
                
                # Ensure the directories exist before saving the CSV
                os.makedirs(os.path.dirname(file_path), exist_ok=True)

                # Save the DataFrame as a CSV file
                frame_df.to_csv(file_path, index=False)


def plot_gr_logs(ax: plt.Axes, df: pd.DataFrame, title: str) -> None:
    """
    Plots gamma-ray (GR) logs from the provided DataFrame on the specified axes.

    Args:
        ax (plt.Axes): Matplotlib axes on which to plot the GR logs.
        df (pd.DataFrame): DataFrame containing the well log data, 
            where 'GR' represents gamma-ray values and 'TDEP' represents depth values.
        title (str): Title for the plot.

    Returns:
        None
    """
    # Extract GR and TDEP values for plotting the GR log in the range 0 to 150
    x_0_150 = df['GR']
    y_0_150 = df['TDEP']

    # Create a copy of the DataFrame to adjust GR values for the range 150 to 300
    df_150_300 = df.copy()
    df_150_300['GR'] = df_150_300['GR'] - 150
    x_150_300 = df_150_300['GR']
    y_150_300 = df_150_300['TDEP']

    # Plot the original GR logs (0 to 150 range) with blue color
    ax.plot(x_0_150, y_0_150, label='GR (0-150)', color='blue', linewidth=0.75, zorder=2)

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

    # Invert the Y-axis to represent depth increasing downwards
    ax.invert_yaxis()

    # Set X-axis limits to restrict the GR range from 0 to 150
    ax.set_xlim(0, 150)

    # Add title and labels to the X and Y axes with bold font
    ax.set_title(title, fontweight='bold')
    ax.set_xlabel('GR', fontweight='bold')
    ax.set_ylabel('TDEP', fontweight='bold')

    # Display the legend for the GR log
    ax.legend()
                

        
