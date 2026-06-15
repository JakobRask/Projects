def generate_alert(kri_result):
    alerts = []
    for metric, details in kri_result.items():
        if details["status"] == "RED":
            alerts.append(
                f"CRITICAL: {metric} exceeds risk appetite."
            )
        elif details["status"] == "AMBER":
            alerts.append(
                f"WARNING: {metric} approaching threshold."
            )
    return alerts