import os
import glob
import subprocess


def handle(step):
    # 1. Verify automatic propagation
    sta_logs = glob.glob(os.path.join(step.step_dir, "*", "sta.log"))
    assert (
        len(sta_logs) == 1
    ), "Test set up improperly - make sure there is only one corner when updating the test"
    sta_log = sta_logs[0]
    result = subprocess.call(
        [
            "grep",
            "No information on clock propagation in input SDC file-- unpropagating all clocks",
            sta_log,
        ]
    )
    assert result == 0, "Clock unpropagation message not printed"

    # 2. Verify clocks propagated
    max_reports = glob.glob(os.path.join(step.step_dir, "*", "max.rpt"))
    assert (
        len(max_reports) == 1
    ), "Test set up improperly - make sure there is only one corner when updating the test"
    max_rpt = max_reports[0]
    result = subprocess.call(
        [
            "grep",
            "clock network delay (ideal)",
            max_rpt,
        ]
    )
    assert result == 0, "Clock not successfully unpropagated automatically"