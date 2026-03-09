# BFOR 206 Lab 8-1: Read/Write

## Task Description

Create a folder named `data` and add the following JSON files to it:

- `question1.json`
- `question2.json`

The questions should have the following format:

```json
{
  "question_id": "Q1",
  "question_text": "What is the capital of France?",
  "answers": [
    {"answer_text": "Paris", "is_correct": true},
    {"answer_text": "London", "is_correct": false},
  ]
}
```

Read the JSON files in the data folder. For each file, find the question ID, question text, and
the correct answer. Write these to a file named `answers.csv` in a folder named `output`. The output should be in the following format:

```text
question_id,question_text,correct_answer
```

## Testing

```bash
# list the files of the data folder
ls data/

# run this in the terminal
python read_write_lab.py

# print the contents of the output file
cat output/answers.csv
```

The output should show a list of the files, the script should run without errors, and the contents of the `answers.csv` file should show the question ID, question text, and correct answer for each question in the JSON files.

## Submission instructions

**Scripts that output Python errors will not be accepted!**

Run your script to show that the code runs without errors
and produces the correct output.

When you are finished, show the instructor:

1. The output from the three commands above.
2. Your code.
