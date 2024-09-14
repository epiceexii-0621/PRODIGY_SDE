from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

# Path to your ChromeDriver
CHROMEDRIVER_PATH = "/path/to/chromedriver"  # Replace with your path to ChromeDriver

# Amazon URL for laptops
URL = "https://www.amazon.com/s?k=laptops"

# Initialize WebDriver
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)

# Function to get product info
def get_product_info(url):
    driver.get(url)
    time.sleep(5)  # Wait for the page to load

    products = []

    # Locate the product elements
    items = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
    for item in items:
        try:
            name = item.find_element(By.XPATH, ".//h2/a/span").text
        except:
            name = "N/A"
        try:
            price = item.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
        except:
            price = "N/A"
        try:
            rating = item.find_element(By.XPATH, ".//span[@class='a-icon-alt']").text
        except:
            rating = "N/A"
        products.append([name, price, rating])

    return products

# Function to save data to CSV
def save_to_csv(products, filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Product Name", "Price", "Rating"])
        writer.writerows(products)

if __name__ == "__main__":
    products = get_product_info(URL)
    save_to_csv(products, "amazon_products.csv")
    print(f"Data saved to amazon_products.csv")

    # Close the WebDriver
    driver.quit()
