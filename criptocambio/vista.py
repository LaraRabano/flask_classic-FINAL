from criptocambio import app


@app.route('/')
def home():
    return "Página de inicio"


@app.route('/nuevo')
def nuevo():
    return "Nuevo movimiento"


@app.route('/modificar')
def actualizar():
    return "Actualizar movimientos"


@app.route('/borrar')
def borrar():
    return "Borrar movimiento"
