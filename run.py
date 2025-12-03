# Importa a função factory do app.py
from app import create_app

# Chama a função factory para criar a instância do app no modo development
app = create_app('development')

# Bloco de execução padrão: Inicia o servidor Flask
if __name__ == '__main__':
    # O Flask usa a variável 'app' por padrão, que contém a instância retornada por create_app()
    app.run(debug=True)