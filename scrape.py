import requests
from bs4 import BeautifulSoup
import json

def extract_book_info(book_soup):
    """Extracts book information from the BeautifulSoup object."""
    title = book_soup.h3.a['title']
    price = book_soup.find(class_='price_color').text.encode('latin1').decode('utf-8')
    availability = book_soup.find(class_='availability').text.strip()
    rating_class = book_soup.p['class']
    rating = rating_class[1] if len(rating_class) > 1 else 'No rating'
    return {"title": title, "rating": rating, "price": price, "availability": availability}

def scrape_category(category_url):
    """Scrapes book data from a given category URL."""
    response = requests.get(category_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books_soup = soup.find_all(class_='product_pod')
    return [extract_book_info(book) for book in books_soup]

base_url = 'https://books.toscrape.com/catalogue/category/books'
categories = {
    "Travel": "travel_2/index.html",
    "Mystery": "mystery_3/index.html",
    "Sequential Art": "sequential-art_5/index.html"
}

scraped_data = []
for category, endpoint in categories.items():
    category_url = f"{base_url}/{endpoint}"
    books_data = scrape_category(category_url)
    scraped_data.append({"category": category,"data": books_data})


json_output = json.dumps(scraped_data, indent=2)

# Save JSON output to a file
with open('book_api.json', 'w') as file:
    file.write(json_output)

def count_books_by_rating(scraped_data, rating):
    """Counts the number of books with a specified rating."""
    count = 0
    for category in scraped_data:
        for book in category["data"]:
            if book["rating"] == rating:
                count += 1
    return count


rating_to_count = "Five"
print(f"Number of books with rating '{rating_to_count}': {count_books_by_rating(scraped_data, rating_to_count)}")
