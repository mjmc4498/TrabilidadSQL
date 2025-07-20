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
        let table = '<table><tr><th>Tabla Fuente</th><th>Campo Fuente</th><th>Tabla Destino</th><th>Campo Destino</th><th>Lógica</th></tr>';
        data.forEach(row => {
            table += `<tr><td>${row.tabla_fuente}</td><td>${row.campo_fuente}</td><td>${row.tabla_destino}</td><td>${row.campo_destino}</td><td>${row.logica}</td></tr>`;
        });
        table += '</table>';
        resultDiv.innerHTML = table;
    })
    .catch(error => {
        console.error('Error:', error);
        resultDiv.innerHTML = '<p>Ocurrió un error. Por favor, comprueba la consola para más detalles.</p>';
    });
});
