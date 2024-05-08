from twilio.rest import Client
import openpyxl

# Tu SID de cuenta de Twilio
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
# Tu token de autenticación de Twilio
auth_token = 'your_auth_token'
# El número de teléfono de Twilio (debe ser un número de WhatsApp Business)
twilio_number = 'whatsapp:+14155238886'

# Ruta del archivo Excel
excel_file = "datos.xlsx"

# Función para leer los datos del Excel
def leer_datos_excel(excel_file):
    wb = openpyxl.load_workbook(excel_file)
    sheet = wb.active
    datos = []
    for row in sheet.iter_rows(values_only=True):
        datos.append(row)
    return datos

# Función para enviar mensaje por WhatsApp usando Twilio
def enviar_mensaje_whatsapp(numero, mensaje):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                              body=mensaje,
                              from_=twilio_number,
                              to=numero
                          )

# Leer los datos del Excel
datos = leer_datos_excel(excel_file)

# Iterar sobre los datos y enviar mensajes por WhatsApp
for fila in datos:
    numero = str(fila[0])
    mensaje = fila[1]
    enviar_mensaje_whatsapp(numero, mensaje)
