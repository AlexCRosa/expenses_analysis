import os

def check_if_report_exists(filename, report_dir):
    """ Check if a report already exists for a given filename. """

    report_filename = os.path.join(report_dir, f"{filename}_report.csv")
    return os.path.exists(report_filename)

def save_report(df, filename, report_dir):
    """ Save the categorized data as a report. """

    report_filename = os.path.join(report_dir, f"{filename}_report.csv")
    df.to_csv(report_filename, index=False)
