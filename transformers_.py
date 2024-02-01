from transformers import pipeline

def extract_invoice_info(text):
    nlp = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", tokenizer="dbmdz/bert-large-cased-finetuned-conll03-english")
    entities = nlp(text)

    # Initialiser le dictionnaire d'informations
    info = {}

    # Associer les types d'entités aux champs du formulaire
    entity_mapping = {
        "B-DATE": "Date Issued",
        "I-DATE": "Date Issued",
        "B-DATE_Due": "Date Due",
        "I-DATE_Due": "Date Due",
        "B-STATUS": "Invoice Status",
        "I-STATUS": "Invoice Status",
        "B-SERVICE": "Service",
        "I-SERVICE": "Service",
        "B-BALANCE": "Balance",
        "I-BALANCE": "Balance",
        "B-ITEM_NAME": "Item Name",
        "I-ITEM_NAME": "Item Name",
        "B-ITEM_DESCRIPTION": "Item Description",
        "I-ITEM_DESCRIPTION": "Item Description",
        "B-COST": "Cost",
        "I-COST": "Cost",
        "B-HOURS": "Hours",
        "I-HOURS": "Hours",
        "B-SALESPERSON": "Salesperson",
        "I-SALESPERSON": "Salesperson",
        "B-THANKS": "Thanks for your business",
        "I-THANKS": "Thanks for your business",
        "B-DISCOUNT": "Discount",
        "I-DISCOUNT": "Discount",
        "B-TAX": "Tax",
        "I-TAX": "Tax",
    }

    # Remplir le dictionnaire d'informations avec les entités extraites
    for entity in entities:
        entity_type = entity["entity"]
        entity_text = entity["word"]

        if entity_type in entity_mapping:
            field_name = entity_mapping[entity_type]
            info[field_name] = entity_text

    # Imprimer les informations extraites
    print("Invoice Information:")
    for field, value in info.items():
        print(f"{field}: {value}")

    return info

# Exemple d'utilisation
text = "Date issued is the April 21, 2021. Date due is May 22, 2021. Invoice status is filled with draft. Services OLA balances 20. Item name is Johnny. Item description. Blah blah blah. Cost is equal $85. Ours is equal $125. Sales person is John. Thanks for your business. Discount is equal to 20%. Tax is 12%."
extract_invoice_info(text)
