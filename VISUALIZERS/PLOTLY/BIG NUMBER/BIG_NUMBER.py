from flojoy import flojoy, DataContainer
from node_sdk.small_memory import SmallMemory
import plotly.graph_objects as go

MEMORY_KEY = "BIG_NUMBER_MEMORY_KEY"


@flojoy
def BIG_NUMBER(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    dc_input = dc_inputs[0]
    job_id = params["job_id"]
    relative_delta = True if params["relative_delta"] == "true" else False
    suffix = params["suffix"]
    prefix = params["prefix"]
    title = params["title"]
    fig = go.Figure()
    match dc_input.type:
        case "ordered_pair":
            prev_num = SmallMemory().read_memory(job_id, MEMORY_KEY)
            big_num = dc_input.y[-1]
            fig.add_trace(
                go.Indicator(
                    mode="number+delta",
                    value=int(float(big_num)),
                    domain={"y": [0, 1], "x": [0, 1]},
                    number={"prefix": prefix, "suffix": suffix},
                    delta=None
                    if prev_num is None
                    else {
                        "reference": int(float(prev_num)),
                        "relative": relative_delta,
                        "valueformat": ".1%" if relative_delta is True else ".1f",
                    },
                    title={"text": title},
                )
            )
            SmallMemory().write_to_memory(job_id, MEMORY_KEY, big_num)
            return DataContainer(type="plotly", fig=fig)
        case _:
            raise ValueError(
                f"unsupported DataContainer type passed for BIG_NUMBER: {dc_input.type}"
            )
