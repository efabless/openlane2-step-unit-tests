import os
import subprocess


def handle(step):
    lef = step.state_out["lef"]
    result = subprocess.call(["grep", "ANTENNAGATEAREA", lef])
    assert result == 0, "Output LEF has no ANTENNAGATEAREA"
