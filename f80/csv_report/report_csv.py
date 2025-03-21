import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

if getattr(sys, 'frozen', False):
    report_path = Path(sys.executable).parent / 'results'
else:
    report_path = Path(__file__).parents[2] / 'results'

report_path.mkdir(exist_ok=True)

def append_csv(dictn):
    datestring = datetime.now().strftime("%Y%m%d")
    file_path = "f80_%s.csv"%datestring
    csv_path: Path = report_path / file_path

    df = pd.DataFrame(dictn)

    if csv_path.exists():
        df.to_csv(csv_path, mode="a", index=False, header=False)
    else:
        df.to_csv(csv_path, index=False)

if __name__ == '__main__':
    dictn = {
        'value_1':[11],
        'value_2':[22],
        'value_3':[33],
        'value_4':[444]
    }
    append_csv_2(dictn)