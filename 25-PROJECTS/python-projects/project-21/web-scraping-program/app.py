import requests
from bs4 import BeautifulSoup
import csv
import os

def scrape_website(url):
    """
    Scrapes data from the given URL and saves it to a CSV file.
    """
    try:
        print(f"Fetching data from {url}...")
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract data into a list of dictionaries
        data = []
        
        # Extract headings (h1, h2, h3)
        for heading in soup.find_all(["h1", "h2", "h3"]):
            data.append({"type": "heading", "text": heading.text.strip()})
        
        # Extract links
        for link in soup.find_all("a", href=True):
            data.append({"type": "link", "text": link.text.strip(), "url": link["href"]})
        
        # Extract paragraphs
        for paragraph in soup.find_all("p"):
            data.append({"type": "paragraph", "text": paragraph.text.strip()})

        # Debug: Print extracted data
        print("Extracted data:", data)

        # Save data to CSV
        save_to_csv(data, "scraped_data.csv")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def save_to_csv(data, filename):
    """
    Saves the scraped data to a CSV file.
    """
    if not data:
        print("No data to save.")
        return

    # Define CSV column headers
    headers = data[0].keys()

    # Get the current working directory
    current_directory = os.getcwd()
    print(f"Current working directory: {current_directory}")

    # Define the full path
    full_path = os.path.join(current_directory, filename)

    # Write data to CSV
    with open(full_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    print(f"Saved {len(data)} rows to '{full_path}'.")


# Main program
if __name__ == "__main__":
    # Input URL to scrape
    url = input("Enter the URL to scrape: ")

    # Call the scraping function
    scrape_website(url)

    # Debug: Confirm script execution
    print("Script execution completed.")