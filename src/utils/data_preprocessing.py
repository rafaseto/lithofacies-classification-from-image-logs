from typing import List, Dict
import numpy as np
import pandas as pd

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

def ndarray_to_dataframe(logical_files_dict):
    logical_file_index = 0
    logical_files_df_dict = {}

    for logical_file in logical_files_dict.values():
        
        dataframe_dict = {}
        frame_index = 0

        for frame in logical_file.values():
            i = 0
            channel_names = frame.dtype.names
            frame_dict = {}

            for channel_name in channel_names:
                curves = [t[i] for t in frame]
                frame_dict[channel_name] = curves
                i += 1

            dataframe_dict[frame_index] = pd.DataFrame(frame_dict)
            frame_index += 1

        logical_files_df_dict[logical_file_index] = dataframe_dict
        logical_file_index += 1

    return logical_files_df_dict
        
