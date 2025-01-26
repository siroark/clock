from flask import Flask, render_template_string
import os  # Importa os módulos necessários

app = Flask(__name__)

@app.route('/')
def home():
    # HTML com o relógio e o JavaScript para atualização
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Relógio Dinâmico</title>
            <style>
                body {
                    background-color: black;
                    color: white;
                    font-size: 50px;
                    text-align: center;
                    font-family: 'Arial', sans-serif;
                    margin-top: 20%;
                }
            </style>
        </head>
        <body>
            <h1 id="clock"></h1>
            <script>
                function updateClock() {
                    var now = new Date();
                    var hours = now.getHours().toString().padStart(2, '0');
                    var minutes = now.getMinutes().toString().padStart(2, '0');
                    var seconds = now.getSeconds().toString().padStart(2, '0');
                    var timeString = hours + ':' + minutes + ':' + seconds;
                    document.getElementById('clock').textContent = timeString;
                }
                setInterval(updateClock, 1000);  // Atualiza a cada 1 segundo
                updateClock();  // Inicializa a hora logo de cara
            </script>
        </body>
        </html>
    """)

# Parte para compatibilidade com o Vercel
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Usa a porta definida pelo Vercel
    app.run(host="0.0.0.0", port=port)
