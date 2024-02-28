def handle(exception):
    assert exception is not None, "Checker didn't catch hold violations"
    corners = ["min_tt_025C_1v80", "nom_tt_025C_1v80", "max_tt_025C_1v80"]
    for corner in corners:
        assert corner in str(exception), "Didn't catch correct corner"
