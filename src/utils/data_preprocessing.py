from typing import List, Dict
import numpy as np
import pandas as pd
import os
import glob
import re

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


def dlis_raw_dfs_to_csv(well_df_dict: Dict[str, Dict[int, Dict[int, pd.DataFrame]]], base_dir: str = "../data/csv_from_dlis_raw") -> None: 
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


def dfs_to_csv(well_df_dict: Dict[str, Dict[int, Dict[int, pd.DataFrame]]], base_dir) -> None: 
    """
    Saves each DataFrame from a nested dictionary of wells, logical files, and frames to separate CSV files.

    Args:
        well_df_dict (Dict[str, Dict[int, Dict[int, pd.DataFrame]]]): A nested dictionary where:
            - The outer keys are well names (str),
            - The second-level keys are logical file indices (int),
            - The third-level keys are frame indices (int),
            - The values are pandas DataFrames containing well log data.
        base_dir (str): The base directory where the CSV files will be saved.

    Returns:
        None: The function saves CSV files and does not return any value.
    """
    for well, w_dict in well_df_dict.items():
        for logical_file, lf_dict in w_dict.items():
            for frame, df in lf_dict.items():
                
                # Create the full file path for saving the CSV
                file_path = f"{base_dir}/{well}/{logical_file}/{frame}"
                
                # Ensure the directories exist before saving the CSV
                os.makedirs(os.path.dirname(file_path), exist_ok=True)

                # Save the DataFrame as a CSV file
                df.to_csv(file_path, index=False)


def spliced_dfs_to_csv(well_df_dict: Dict[str, pd.DataFrame], base_dir:str) -> None: 
    """
    Saves the spliced DataFrames into csv files

    Args:
        well_df_dict (Dict[str, pd.DataFrame]): A dictionary where:
            - The keys are well names (str),
            - The values are pandas DataFrames containing well log data.
        base_dir (str): The base directory where the CSV files will be saved. 

    Returns:
        None: The function saves CSV files and does not return any value.
    """
    for well, df in well_df_dict.items():
                
        # Create the full file path for saving the CSV
        file_path = f"{base_dir}/{well}"
                
        # Ensure the directories exist before saving the CSV
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Save the DataFrame as a CSV file
        df.to_csv(file_path, index=False)


def load_csv_files(base_path: str) -> Dict[str, Dict[str, Dict[str, pd.DataFrame]]]:
    """
    Loads all CSV files from the specified base directory and stores them in a nested dictionary
    organized by folder, subfolder, and file name.

    Args:
        base_path (str): The root directory where CSV files are stored.

    Returns:
        Dict[str, Dict[str, Dict[str, pd.DataFrame]]]: A nested dictionary where the outer keys are folder names,
        the second level keys are subfolder names, and the innermost keys are file names.
        The values are Pandas DataFrames representing the content of each CSV file.
    """
    
    csv_data = {}

    data_path = os.path.join(base_path, '**', '*.csv')

    for file in glob.glob(data_path, recursive=True):
        relative_path = os.path.relpath(file, base_path)
        parts = relative_path.split(os.sep)

        folder_name = parts[0]
        subfolder_name = parts[1]
        file_name = parts[2]
        
        if folder_name not in csv_data:
            csv_data[folder_name] = {}
        
        if subfolder_name not in csv_data[folder_name]:
            csv_data[folder_name][subfolder_name] = {}
        
        csv_data[folder_name][subfolder_name][file_name] = pd.read_csv(file)
    
    return csv_data


def extract_coating(base_path):
    agp_data = {}

    data_path = os.path.join(base_path, '**', '*.txt')

    for file in glob.glob(data_path, recursive=True):

        with open(file, "r") as file:
            content = file.read()

        # RE to find the name of the well
        well_name_match = re.search(r"PO[ÇC]O\s*:\s*(.*)", content)
        well_name = well_name_match.group(1).strip() if well_name_match else "Nome do poço não encontrado"

        # RE to find the surface coating
        rev_superficie_match = re.search(r"REV\.\s*SUPERFICIE\s+([\d.]+)", content)
        rev_superficie = float(rev_superficie_match.group(1)) if rev_superficie_match else None

        # RE to find the intermediary coating
        rev_intermed_match = re.search(r"REV\.\s*INTERMED\.\s+([\d.]+)", content)
        rev_intermed = float(rev_intermed_match.group(1)) if rev_intermed_match else None

        agp_data[well_name] = {
            "Rev. Superficie": rev_superficie,
            "Rev. Intermed.": rev_intermed
        }

    return agp_data


def create_df_subset(well_df_dict: Dict[str, Dict[int, Dict[int, pd.DataFrame]]], curve: str):
    curve_data = {}
    
    for well, w_dict in well_df_dict.items():
        curve_data[well] = {}

        for logical_file, lf_dict in w_dict.items():
            curve_data[well][logical_file] = {}

            for frame, df in lf_dict.items():
                try:
                    curve_df = df[['TDEP', curve]]

                    curve_data[well][logical_file][frame] = curve_df
                except:
                    pass
                
    return curve_data