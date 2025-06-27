import requests

# Hacer peticiones para simular errores
def test_errors():
    errors = ['400', '404', '500']
    for error in errors:
        response = requests.get(f'http://127.0.0.1:8080/cause_error/{error}')
        print(f"Simulating {error} error: {response.status_code} - {response.json()}")

if __name__ == "__main__":
    test_errors()
