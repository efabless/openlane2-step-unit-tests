import pytest
from openlane.steps.step import StepError


def handle(step):
    from openlane.steps import Step

    DRT = Step.factory.get("OpenROAD.DetailedRouting")

    try:
        drt = DRT(step.config, step.state_out)
        drt.start(step_dir=".")
    except StepError as e:
        pytest.fail("")
