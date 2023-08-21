import requests
from bs4 import BeautifulSoup

# Define the base URL and headers
base_url = "https://www.amazon.in/s"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
}

# Parameters for the initial search page
search_params = {
    "k": "bags",
    "crid": "2M096C61O4MLT",
    "qid": "1653308124",
    "sprefix": "ba,aps,283",
    "ref": "sr_pg_1"
}

# Function to scrape product information from a page
def scrape_page(page_url):
    response = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    product_list = []
    
    # Extract product information here
    # For example, find product URL, name, price, rating, and reviews
    
    return product_list

# Main scraping function
def scrape_amazon_products(base_url, search_params, num_pages):
    all_products = []
    
    for page_num in range(1, num_pages + 1):
        search_params["page"] = page_num
        response = requests.get(base_url, params=search_params, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find and extract individual product URLs from the search results
        product_links = [a["href"] for a in soup.select("a.a-link-normal.s-no-outline")]
        
        for product_link in product_links:
            product_url = "https://www.amazon.in" + product_link
            product_info = scrape_page(product_url)
            all_products.extend(product_info)
            
    return all_products

# Number of pages to scrape
num_pages_to_scrape = 20

# Scrape the products
scraped_products = scrape_amazon_products(base_url, search_params, num_pages_to_scrape)

# Print or process the scraped product information
for product in scraped_products:
    print(product)

import requests
from bs4 import BeautifulSoup
import csv

# Define a function to scrape additional information from a product URL
def scrape_product_details(product_url):
    response = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Initialize variables to store the details
    description = ""
    asin = ""
    product_description = ""
    manufacturer = ""

    # Extract the information from the product page
    # Update the CSS selectors based on the actual structure of the page
    description_element = soup.find("div", {"id": "productDescription"})
    if description_element:
        description = description_element.get_text(strip=True)

    asin_element = soup.find("th", text="ASIN")
    if asin_element:
        asin = asin_element.find_next("td").get_text(strip=True)

    product_description_element = soup.find("div", {"id": "productDescription"})
    if product_description_element:
        product_description = product_description_element.get_text(strip=True)

    manufacturer_element = soup.find("a", {"id": "bylineInfo"})
    if manufacturer_element:
        manufacturer = manufacturer_element.get_text(strip=True)

    return {
        "Description": description,
        "ASIN": asin,
        "Product Description": product_description,
        "Manufacturer": manufacturer
    }

# Scrape product details from a list of product URLs
def scrape_product_urls(product_urls):
    product_details = []
    for url in product_urls:
        details = scrape_product_details(url)
        product_details.append(details)
    return product_details

# List of product URLs (you would have these URLs from the previous step)
product_urls =product_urls = [
    # Assuming you have a list of relative product URLs
product_urls = [
    "/dp/B12345678",
    "/dp/C98765432",
    "/dp/D54321098"
]

# Form the full URLs by concatenating the base URL and relative paths
full_product_urls = [base_url + url for url in product_urls]

# Scrape product details and export to CSV
csv_filename = "product_details.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
    fieldnames = ["Description", "ASIN", "Product Description", "Manufacturer"]
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    for url in full_product_urls:  # Use the full URLs
        details = scrape_product_details(url)
        csv_writer.writerow(details)

print("Data exported to", csv_filename)
