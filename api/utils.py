import requests
def fetch_product_from_open_food_facts(barcode):
    """
    Récupère les détails d'un produit depuis l'API Open Food Facts.
    """
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get('status') == 1:  # Produit trouvé
            product_data = data['product']
            return {
                'name': product_data.get('product_name', ''),
                'brand': product_data.get('brands', ''),
                'category': product_data.get('categories', ''),
                'nutritional_info': product_data.get('nutriments', {}),
                'picture': product_data.get('image_url', ''),
            }
        else:
            return None  # Produit non trouvé
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")
