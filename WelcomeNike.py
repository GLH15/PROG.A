from dash import html

def welcome():
    return html.Div(
        style={
            "background-image": "url('assets/imagenes/logonike.jpg')",  # Ruta de la imagen
            "background-size": "cover",  # Ajusta la imagen para cubrir el fondo
            "background-position": "center",  # Centra la imagen
            "height": "100vh",  # Ocupa toda la altura de la ventana
            "width": "100%",  # Ocupa el ancho
            "display": "flex",  # Usa flexbox para centrar el contenido
            "flex-direction": "column",
            "justify-content": "center",
            "align-items": "center",
            "text-align": "center",  # Centra el texto
        },
        children=[
            html.H1("Bienvenido al Dashboard Nike", className="text-up"),
            html.P(
                "Objetivo: Encontrar los productos con mayor y menor precio, "
                "además del promedio en productos Nike",
                className="lead",
            ),
        ],
    )