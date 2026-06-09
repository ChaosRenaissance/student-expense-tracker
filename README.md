# Student Expense Tracker

A simple Python expense tracking tool for international students to analyze monthly living costs.

## Project Goal

International students often need to manage rent, food, transportation, phone plans, tuition, and other daily expenses in a new country.

This project helps users record expenses, summarize monthly spending, and understand where their money goes.

## Features

* Load expense records from a CSV file
* Calculate total monthly spending
* Summarize expenses by category
* Print a simple monthly expense report
* Use only Python standard library for v0.1.0

## Example CSV Format

```csv
date,category,description,amount,currency
2026-09-01,Rent,September rent,1200,USD
2026-09-02,Food,Costco grocery,85.50,USD
2026-09-03,Transportation,Light rail,3.00,USD
```

## How to Run

Download this repository to your computer.

Then open the project folder in your terminal and run:

```bash
python main.py
```

The program will read `expenses.csv` and print a monthly expense summary.

## Example Output

```text
Monthly Expense Summary
-----------------------
Total spending: $1383.99

By category:
Rent: $1200.00
Food: $93.49
Transportation: $3.00
Phone: $25.00
Shopping: $45.00
Entertainment: $16.50
```

## Roadmap

### v0.1.0

* Basic CSV expense tracking
* Monthly spending summary
* Category-level summary

### Future Plans

* Export monthly summary to CSV
* Add charts
* Add budget warning system
* Add currency conversion
* Add monthly comparison
* Build a simple web dashboard

## Why This Project Matters

Moving to a new country can make budgeting difficult.

This tool is designed to help international students understand their living costs and build better financial habits.

## Maintainer

This project is maintained as an open-source tool for international students.
