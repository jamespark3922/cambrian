import os
import json
import csv

from datetime import datetime
import pandas as pd


def compute_metrics(jsonl_file, csv_file, extra_outdir=None):

    test_list = []
    model = ""
    with open(jsonl_file, 'r') as file:
        for line in file:
            data = json.loads(line)
            test_list.append(data)
    file_path = f"./answers/{model}_userqa_prediction.excel"
    pd.DataFrame(test_list).to_excel(file_path)
    # add_data_to_csv(csv_file, combined_data)
    print(f"prediction file: {file_path} is created.")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--answers_file", type=str, required=True, help="Path to the answers file")
    parser.add_argument("--csv_file", type=str, default="./experiments.csv", help="Path to the output csv file to store the experiment data")
    parser.add_argument("--extra_outdir", type=str, default=None, help="Path to an extra output directory in which to store a copy of the information")

    args = parser.parse_args()

    compute_metrics(args.answers_file, args.csv_file, args.extra_outdir)
