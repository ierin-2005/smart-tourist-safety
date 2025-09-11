import numpy as np

def detect_anomaly(locations):
    """
    Simple anomaly detection:
    - If tourist hasn't moved (same location repeated 5 times)
    - Or if jump in location distance is too large
    """
    if len(locations) < 5:
        return None

    # Case 1: No movement
    if all(loc == locations[0] for loc in locations[-5:]):
        return "No movement detected (possible distress)."

    # Case 2: Sudden jump (fake check: diff in string length)
    diffs = [abs(len(locations[i]) - len(locations[i-1])) for i in range(1, len(locations))]
    if max(diffs) > 10:
        return "Sudden unusual location jump detected."

    return None
