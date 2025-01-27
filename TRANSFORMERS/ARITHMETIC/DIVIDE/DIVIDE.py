import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def DIVIDE(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Divide 2 or more numeric arrays, matrices, dataframes, or constants element-wise.
    When a constant is added to an array or matrix, each element in the array or
    matrix will be increased by the constant value.
    """

    if len(dc_inputs) < 2:
        raise ValueError(
            f"To add the values, DIVIDE node requires two inputs, {len(dc_inputs)} was given!"
        )
    a = dc_inputs[0].y
    b = dc_inputs[1].y

    x = dc_inputs[0].x
    y = np.divide(a, b)

    return DataContainer(x=x, y=y)
