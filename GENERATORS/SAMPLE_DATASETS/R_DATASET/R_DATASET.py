from flojoy import flojoy, DataContainer
from rdatasets import data


@flojoy
def R_DATASET(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """
    Retrieves a pandas DataFrame from rdatasets using the provided dataset_key parameter and returns it wrapped in a DataContainer.

    Args:
        dc_inputs (list[DataContainer]): A list of DataContainer objects, but not used in this function.
        params (dict): A dictionary of parameters for this function.
            dataset_key (str): The key used to retrieve the DataFrame.

    Returns:
        DataContainer: A DataContainer object containing the retrieved pandas DataFrame.
    """
    dataset_key = params["dataset_key"]
    df = data(dataset_key)
    return DataContainer(type="dataframe", m=df)
