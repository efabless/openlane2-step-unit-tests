def handle(exception, caplog):
    corners = [
        "max_tt_025C_1v80",
        "min_tt_025C_1v80",
        "nom_tt_025C_1v80",
        "max_ff_n40C_1v95",
        "max_ss_100C_1v60",
        "min_ff_n40C_1v95",
        "min_ss_100C_1v60",
        "nom_ff_n40C_1v95",
        "nom_ss_100C_1v60",
    ]
    for corner in corners:
        assert (
            corner in caplog.text
        ), f"Did not warn about violation in corner: '{corner}'"
