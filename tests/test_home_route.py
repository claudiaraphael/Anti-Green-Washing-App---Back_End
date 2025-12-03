from app import create_app

# Exemplo de teste:
def test_home_page():
    test_app = create_app('testing')
    # ... executa testes no test_app