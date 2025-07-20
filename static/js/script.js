document.getElementById('trace-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const sqlScript = document.getElementById('sql-script').value;
    const resultDiv = document.getElementById('trace-result');

    try {
        const ast = SQLParser.parse(sqlScript);
        let table = '<table><tr><th>Tabla Fuente</th><th>Campo Fuente</th><th>Tabla Destino</th><th>Campo Destino</th><th>Lógica</th></tr>';

        if (ast.type === 'select') {
            const sourceTable = ast.from[0].table;
            const destTable = ast.into.name;

            ast.columns.forEach(column => {
                let sourceField, destField, logic;

                if (column.alias) {
                    destField = column.alias;
                    sourceField = column.expr.column;
                    logic = `${column.expr.column} AS ${column.alias}`;
                } else {
                    destField = column.expr.column;
                    sourceField = column.expr.column;
                    logic = column.expr.column;
                }

                table += `<tr><td>${sourceTable}</td><td>${sourceField}</td><td>${destTable}</td><td>${destField}</td><td>${logic}</td></tr>`;
            });
        }

        table += '</table>';
        resultDiv.innerHTML = table;
    } catch (error) {
        console.error('Error:', error);
        resultDiv.innerHTML = '<p>Ocurrió un error al analizar el SQL. Por favor, comprueba la sintaxis.</p>';
    }
});
