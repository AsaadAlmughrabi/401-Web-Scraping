# Book Scraper

This Python script scrapes book data from a fictional bookstore website and saves the information in a JSON file. It includes functionality to count books by specific ratings.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AsaadAlmughrabi/401-Web-Scraping.git
   cd 401-Web-Scraping
   ```

2. Install dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```

## Usage

### Running the Script

To run the script and scrape book data from the website:

```bash
python scrape.py
```

### Counting Books by Rating

The script provides a function `count_books_by_rating(scraped_data, rating)` to count books with a specified rating. Modify `rating_to_count` in the script to count books with different ratings.

Example:
```python
rating_to_count = "Five"
print(f"Number of books with rating '{rating_to_count}': {count_books_by_rating(scraped_data, rating_to_count)}")
```

## File Structure

- `scrape.py`: Main Python script for scraping and processing book data.
- `book_api.json`: Output JSON file containing scraped book data.

---

**Author: Asaad Almughrabi**


