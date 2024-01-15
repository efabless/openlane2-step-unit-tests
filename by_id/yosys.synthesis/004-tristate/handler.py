import os
import subprocess


def handle(step, test):
    assert (
        step.state_out.metrics["synthesis__check_error__count"] == 0
    ), "Unexpected synthesis check errors reported"
    if "synlig" in test:
        result = subprocess.call(
            ["grep", "UHDM", os.path.join(step.step_dir, "yosys-synthesis.log")],
        )
        assert result == 0, "Synlig was not used in the synthesis process"
