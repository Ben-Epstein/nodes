import numpy as np
import traceback
from flojoy import flojoy, DataContainer

@flojoy
def LEAST_SQUARES(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Computes the least square that minimizes the distance between
      the inputs 'DataContainer' class, specifically the 'matrix' type
     and the regression. 
    Args:
        dc_inputs (list[DataContainer]: List of DataContainer objects containing 
        a coefficient matrix and dependent variable)
        params (dict): Additional parameters for least squares method (not used in this function)
        
    Returns:
        DataContainer: A 'DataContainer' class of type 'matrix' 
        that represents the weights of regression line (least squares)
    Raises: 
        Exception: If errors occurs during least square calculation """
    
    x : np.ndarray = np.eye(3)
    y : np.ndarray = np.eye(3)
    a : np.ndarray = np.eye(3, 2)

    if (dc_inputs.__len__ > 0): 
        if (dc_inputs[0].type != "matrix"):
            raise ValueError(f"unsupported DataContainer type passed to LEAST_SQUARES node: '{dc_inputs[0].type}'")
        
        x = dc_inputs[0].m
        y = dc_inputs[1].m
        

        if (x.shape[0] != y.shape[0]):
            print("matrix dimensions do not match.")

        else:
            try: 
                a = np.vstack([x, np.ones(len(x))]).T
                res = np.linalg.lstsq(a, y, rcond=None)[0]
            except np.linalg.LinAlgError:
                raise ValueError("Least Square Computation failed.")
            
            return DataContainer(type="matrix", m=res)
    else:
    
        return DataContainer(type="matrix", m=np.eye(3))
 