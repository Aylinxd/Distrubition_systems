import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("feeders", "13Bus", "IEEE13Nodeckt.dss")

dss = py_dss_interface.DSSDLL()

dss.text(f"compile [{dss_file}]")

#dss.text("Show voltages")
#dss.text("Show powers")

busses=dss.circuit_all_bus_names()
print(busses)
a=dss.monitors_all_names()
print(a)
dss.monitors_write_name(a[5]) #activate the monitor
mon= dss.monitors_read_name()
print(mon)
elements_0f_mon=dss.monitors_read_element()
print(elements_0f_mon)
dss.monitors_show()


dss.circuit_set_active_bus('645')
pow= dss.cktelement_powers()
volt=dss.cktelement_voltages()
print(pow)
print(volt)











