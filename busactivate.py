import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("feeders", "13Bus", "IEEE13Nodeckt.dss")

dss = py_dss_interface.DSSDLL()

dss.text(f"compile [{dss_file}]")

x=dss.circuit_all_bus_names()
def get_power_from_bus(a,i):
    dss.circuit_set_active_bus(a)
    pow = dss.cktelement_powers()
    volt = dss.cktelement_voltages()
    print(pow[i])
    print(volt)
    print(pow)


get_power_from_bus('675',2)