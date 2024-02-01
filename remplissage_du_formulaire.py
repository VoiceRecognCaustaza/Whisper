import whisper
import re
def extract_invoice_info(text):
    info = {}

    # Date Issued
    match = re.search(r"Date issued(?: is the|is filled with|is|,|.)? (.+?)(\.|Date due|Date)", text, re.IGNORECASE)
    if match:
        info["Date Issued"] = match.group(1).strip()

    # Date Due
    match = re.search(r"Date due(?: is|is filled with|is the|,|.)? (.+?)(\.|Invoice status)", text, re.IGNORECASE)
    if match:
        info["Date Due"] = match.group(1).strip()

    # Invoice Status
    match = re.search(r"Invoice status(?: is filled with|is|,|.)? (.+?) (\.|service|Services)", text, re.IGNORECASE)
    if match:
        info["Invoice Status"] = match.group(1).strip()

    # Service
    match = re.search(r"( Services| Service)(?: is filled with|is|are|,|.)? (.+?) (\.|Balance)", text, re.IGNORECASE)
    if match:
        info["Service"] = match.group(2).strip()

    # Balance
    match = re.search(r"Balance(?: is filled with|is|,|.)? (.+?) (\.|Item name)", text, re.IGNORECASE)
    if match:
        info["Balance"] = match.group(1).strip()

    # Item Name
    match = re.search(r"Item name(?: is|is filled with|,|.)? (.+?) (\.|Item description)", text, re.IGNORECASE)
    if match:
        info["Item Name"] = match.group(1).strip()

    # Item Description
    match = re.search(r"Item description(?: is filled with|is|,|.)? (.+?) (\.|Cost|,)", text, re.IGNORECASE)
    if match:
        info["Item Description"] = match.group(1).strip()

    # Cost
    match = re.search(r"Cost(?: is equal|is equal to|is|,|.)? \$([\d.]+)(\.| Hours|,)", text, re.IGNORECASE)
    if match:
        info["Cost"] = match.group(1).strip()

    # Hours
    match = re.search(r"( Hours| hours| Ours)(?: is equal|is equal to|is|,|.)? ([\d.]+)(\.| Sales person| Salesperson)", text, re.IGNORECASE)
    if match: 
        info["Hours"] = match.group(2).strip()

    # Salesperson
    match = re.search(r"(Sales person| Salesperson)(?: is|is filled with|is named|nammed|,|.)? (.+?)(\.| Thanks for your business)", text, re.IGNORECASE)
    if match:
        info["Salesperson"] = match.group(2).strip()

    # Thanks for your business
    match = re.search(r"( Thanks for your business| thanks for your business)(\.| discount| Discount)", text)
    if match:
        info["Thanks for your business"] = "Thanks for your business"

    # Discount
    match = re.search(r"Discount(?: is equal to|equals|is|,|.)? (\d+)%?(\.| Tax)", text, re.IGNORECASE)
    if match:
        info["Discount"] = match.group(1).strip()

    # Tax
    match = re.search(r"( Tax| tax)(?: is|equals|is equal to|,|.)? (\d+)%\.", text, re.IGNORECASE)
    if match:
        info["Tax"] = match.group(2).strip()

    return info

def fill_invoice_form(audio_file_path):
    try:
        # Charger le modèle Whisper
        model = whisper.load_model('base')

        # Transcrire le fichier audio
        result = model.transcribe(audio_file_path, language='English')
        transcribed_text = result["text"]
        print("Le text extrait: ",transcribed_text)

        # Extraire les informations de la facture à partir du texte transcrit
        invoice_info = extract_invoice_info(transcribed_text)

        if invoice_info:
            # Vous pouvez utiliser les informations pour remplir un formulaire ou effectuer d'autres actions
            print("Les informations de facturation extraites:")
            return invoice_info
        else:
            # Gérer le cas où les informations de facturation ne peuvent pas être extraites
            print("Les informations de facturation ne peuvent pas être extraites.")
            return None

    except Exception as e:
        # Gérer les exceptions
        print({"error": str(e)})

# Remplacez 'path/to/your/audio/file.mp3' par le chemin réel de votre fichier audio
audio_file_path = r'C:\Users\ASUS\OneDrive\Bureau\Caustaza\Codes\whisper\Date Issued is the 2 (1).mp3'

# Testez le modèle Whisper avec le fichier audio fourni et remplissez le formulaire
invoice_info_result = fill_invoice_form(audio_file_path)
print(invoice_info_result)