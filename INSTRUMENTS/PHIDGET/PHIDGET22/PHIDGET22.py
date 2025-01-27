from flojoy import flojoy, DataContainer
import Phidget22
from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *


def onVoltageRatioChange(self, voltageRatio):
    """Declaration of the Event handler, print Voltage variation for a channel"""
    print("VoltageRatio [" + str(self.getChannel()) + "]: " + str(voltageRatio))


@flojoy
def PHIDGET22(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Pressure Measurement with Phidget 22 sensors"""
    voltage: list[float] = []
    pressions: list[float] = []
    N = params["n_sensors"]

    for i in range(0, N):
        # Creation of an instance of the VoltageRationInput class
        voltageRatioInput = VoltageRatioInput()
        # Set Channel for Communication with the Phidget Interface Kit :
        voltageRatioInput.setChannel(i)
        # Assign the handler that will be called when the event occurs :
        voltageRatioInput.setOnVoltageRatioChangeHandler(onVoltageRatioChange)
        # Open the Channel after event handler is set :
        voltageRatioInput.openWaitForAttachment(5000)

        volt_i: float = (
            voltageRatioInput.getVoltageRatio()
        )  # Measure Voltage from the sensor
        voltage.append(volt_i)  # Add Voltage to the list of measurements

        # Example of a Calibration to convert Voltage into pressions :
        pression_i: float = (volt_i - params["calibration1"]) / params["calibration2"]

        pressions.append(pression_i)

    return DataContainer(x={"a": voltage, "b": pressions}, y=pressions)


@flojoy
def PHIDGET22_MOCK(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Mock Function for the node Phidget 22"""
    voltage: list[float] = []
    pressions: list[float] = []
    N = 4

    for i in range(0, N):
        volt_i: int = i * 10 + 4  # Scalar operation to modify data
        voltage.append(volt_i)  # Add Voltage to the list of measurements
        pression_i: float = (volt_i - 0.015) / 0.06
        pressions.append(pression_i)

    return DataContainer(x={"a": voltage, "b": pressions}, y=pressions)
