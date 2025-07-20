# SQL Traceability

This tool generates a traceability report from a SQL script. It provides a web interface to enter a SQL script and view the traceability report.

**Live Demo:** [https://mjmc4498.github.io/TrabilidadSQL](https://mjmc4498.github.io/TrabilidadSQL)

**Author:** [mjmc4498](https://github.com/mjmc4498)

## System Manual

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/mjmc4498/TrabilidadSQL.git
    cd TrabilidadSQL
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  **Start the Flask server:**
    ```bash
    python app.py
    ```

2.  Open your web browser and navigate to `http://127.0.0.1:5000`.

## User Manual

1.  Enter your SQL script in the text area.
2.  Click the "Generate Traceability" button.
3.  The traceability report will be displayed in a table below the text area.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
