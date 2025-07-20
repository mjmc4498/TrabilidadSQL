document.getElementById('trace-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const sqlScript = document.getElementById('sql-script').value;
    const resultDiv = document.getElementById('trace-result');

    fetch('/trace', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'sql_script=' + encodeURIComponent(sqlScript),
    })
    .then(response => response.json())
    .then(data => {
        let table = '<table><tr><th>Source Table</th><th>Source Field</th><th>Destination Table</th><th>Destination Field</th><th>Logic</th></tr>';
        data.forEach(row => {
            table += `<tr><td>${row.tabla_fuente}</td><td>${row.campo_fuente}</td><td>${row.tabla_destino}</td><td>${row.campo_destino}</td><td>${row.logica}</td></tr>`;
        });
        table += '</table>';
        resultDiv.innerHTML = table;
    })
    .catch(error => {
        console.error('Error:', error);
        resultDiv.innerHTML = '<p>An error occurred. Please check the console for details.</p>';
    });
});
