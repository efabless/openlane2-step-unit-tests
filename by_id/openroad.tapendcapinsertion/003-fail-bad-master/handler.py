import re


def handle(step, exception, caplog):
    log = open(step.get_log_path()).readlines()  # caplog is empty ?
    assert exception is not None, "Didn't fail on bad master"
