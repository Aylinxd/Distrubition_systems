import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))
dss_file = pathlib.Path(script_path).joinpath( "LVTestCase", "Master.dss")
dss = py_dss_interface.DSSDLL()
dss.text(f"compile [{dss_file}]")
#dss.text("Show voltages")