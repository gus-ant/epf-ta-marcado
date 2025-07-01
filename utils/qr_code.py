import qrcode
from io import BytesIO
import base64

# aqui será gerado o qrcode, que vai ser exibido em uma página dedicada
def gerar_qrcode_base64(data: str):
    img = qrcode.make(data)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode('utf-8')
