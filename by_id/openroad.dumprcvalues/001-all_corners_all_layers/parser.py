import re
from decimal import Decimal


def extract_section_header(line):
    """Extracts and cleans a section header from a line (any number of '=')."""
    match = re.search(r"^=+\s+(.+)\s+=+$", line)  # Regex to match any number of =
    if match:
        return match.group(1).strip().replace(" ", "_").replace(".", "")
    return None


def parse_report_file(filepath):
    """Parses a report file and extracts RC values. Handles all three file types."""

    data = {}
    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File not found: {filepath}")
        return None

    file_type = None  # Determine file type

    if any("Technology LEF Values" in line for line in lines):
        file_type = "lef"
        data["routing_layers"] = {}
        data["vias"] = {}
    elif any("Layer Values (After Set RC)" in line for line in lines):
        file_type = "layer"
        data["routing_layers"] = {}
        data["vias"] = {}
    elif any("Resizer RC Values (After Set RC)" in line for line in lines):
        file_type = "resizer"
        data = {}
    else:
        print(f"Warning: Unknown file type: {filepath}")
        return None

    section = None
    corner_name = None

    for line in lines:
        line = line.strip()
        section_header = extract_section_header(line)

        if section_header:
            section = section_header.lower()
            if file_type == "resizer" and "corner" in section:  # Handle corner headers
                corner_name = (
                    section_header.replace("Corner_", "").strip().replace("=", "")
                )
                data[corner_name] = {}
            elif file_type == "resizer" and corner_name:
                data[corner_name].setdefault("estimation_rc_values", [])
                data[corner_name].setdefault("rt_layer_rc_values", [])
                data[corner_name].setdefault("via_r_values", [])
            continue

        if file_type in ("lef", "layer"):
            if section == "routing_layers" and line and not line.startswith("Name"):
                parts = line.split()
                if len(parts) >= 4:
                    data["routing_layers"][parts[0]] = {
                        "direction": parts[1],
                        "res": Decimal(parts[2]),
                        "cap": Decimal(parts[3]),
                    }
            elif section == "vias" and line and not line.startswith("Name"):
                parts = line.split()
                if len(parts) >= 2:
                    data["vias"][parts[0]] = {"res": Decimal(parts[1])}
        elif file_type == "resizer" and corner_name:
            if (
                section == "estimation_rc_values"
                and line
                and not line.startswith("Name")
            ):
                parts = line.split()
                data[corner_name]["estimation_rc_values"].append(
                    {
                        "name": parts[0],
                        "direction": parts[1],
                        "res": Decimal(parts[2]),
                        "cap": Decimal(parts[3]),
                    }
                )
            elif (
                section == "rt_layer_rc_values" and line and not line.startswith("Name")
            ):
                parts = line.split()
                data[corner_name]["rt_layer_rc_values"].append(
                    {
                        "name": parts[0],
                        "direction": parts[1],
                        "res": Decimal(parts[2]),
                        "cap": Decimal(parts[3]),
                    }
                )
            elif section == "via_r_values" and line and not line.startswith("Name"):
                parts = line.split()
                if len(parts) >= 2:
                    data[corner_name]["via_r_values"].append(
                        {"name": parts[0], "res": Decimal(parts[1])}
                    )

    return data
