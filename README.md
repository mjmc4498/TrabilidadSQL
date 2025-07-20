# SQL Traceability

This tool generates a traceability report from a SQL script.

## Installation

1. Clone the repository.
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To generate a traceability report, run the following command:

```bash
python -m sql_traceability.cli <path_to_sql_file> <path_to_output_csv>
```

For example:

```bash
python -m sql_traceability.cli my_script.sql traceability_report.csv
```

This will create a CSV file with the following columns:

- `tabla_fuente`
- `campo_fuente`
- `tabla_destino`
- `campo_destino`
- `logica`
