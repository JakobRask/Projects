from datetime import datetime

def create_report(kri_results, alerts):
    report = []
    report.append("# Risk Report")
    report.append(f"Date: {datetime.today().date()}")
    report.append("\n## KRIs")
    for metric, details in kri_results.items():
        report.append(
            f"- {metric}: "
            f"{details['value']} "
            f"({details['status']})"
        )
    report.append("\n## Alerts")
    if alerts:
        report.extend([f"- {x}" for x in alerts])
    else:
        report.append("- No alerts generated.")
    with open(
        "reports/risk_report.md",
        "w"
        ) as f:
        f.write("\n".join(report))