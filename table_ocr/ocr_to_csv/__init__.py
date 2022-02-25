import csv
import io
import os
import pandas as pd


def text_files_to_csv(files):
    """Files must be sorted lexicographically
    Filenames must be <row>-<colum>.txt.
    000-000.txt
    000-001.txt
    001-000.txt
    etc...
    """
    rows = []
    for f in files:
        directory, filename = os.path.split(f)
        with open(f) as of:
            txt = of.read().strip()
        row, column = map(int, filename.split(".")[0].split("-"))
        if row == len(rows):
            rows.append([])
        rows[row].append(txt)

    csv_file = io.StringIO()
    writer = csv.writer(csv_file)

    with open('output.txt', 'w') as f:
        wt = csv.writer(f)
        wt.writerows(rows)

    archivo = pd.read_csv('output.txt')
    archivo.to_html('output.txt', index=False)


    writer.writerows(rows)
    return csv_file.getvalue()

def main(files):
    return text_files_to_csv(files)
