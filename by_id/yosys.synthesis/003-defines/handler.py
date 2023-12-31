import os
import subprocess


def handle(step, test, exception):
    assert exception is not None, "Preprocessor did not remove Verilog module"
    if "synlig" in test:
        result = subprocess.call(
            ["grep", "UHDM", os.path.join(step.step_dir, "yosys-synthesis.log")]
        )
        assert result == 0, "Synlig was not used in the synthesis process"
