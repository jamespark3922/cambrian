import os
import json
import csv

from m4c_evaluator import TextVQAAccuracyEvaluator
from datetime import datetime


current_time = datetime.now()
time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")


def add_data_to_csv(file_path, data):
    file_exists = os.path.exists(file_path)

    with open(file_path, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())

        if not file_exists:
            writer.writeheader()

        writer.writerow(data)


def compute_metrics(jsonl_file, csv_file, extra_outdir=None):
    test_list = []

    model = ""
    with open(jsonl_file, 'r') as file:
        for line in file:
            data = json.loads(line)
            answer = data['answer']
            question_id = data['question_id']
            model = data.get("model_id", '')
            test_list.append({
                "question_id": int(question_id),
                "answer": answer
            })
    file_path = f"./answers/{model}_vqav2_testdev_submission.json"
    with open(file_path, "w") as json_file:
        json.dump(test_list, json_file)
    combined_data = {
        "model": model,
        "time": time_string,
        "accuracy": "add here after submission",
    }
    # add_data_to_csv(csv_file, combined_data)
    print(f"submission file: {file_path} is created. please submit at eval ai server")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--answers_file", type=str, required=True, help="Path to the answers file")
    parser.add_argument("--csv_file", type=str, default="./experiments.csv", help="Path to the output csv file to store the experiment data")
    parser.add_argument("--extra_outdir", type=str, default=None, help="Path to an extra output directory in which to store a copy of the information")

    args = parser.parse_args()

    compute_metrics(args.answers_file, args.csv_file, args.extra_outdir)
