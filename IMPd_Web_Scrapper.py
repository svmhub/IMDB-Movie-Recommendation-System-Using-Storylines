# Import the required packages

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

class IMDBScraper:
    def __init__(self, year):
        self.year = year
        self.url = f"https://www.imdb.com/search/title/?year={self.year}"
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 300)
        self.movies = []

    def scrape(self):
        print(f"🚀 Starting scrape for the year: {self.year}")
        self.driver.get(self.url)
        collected_count = 0

        while True:
            try:
                # 1. Wait for movie cards to load

                self.wait.until(EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "ipc-metadata-list-summary-item")
                ))
                movie_cards = self.driver.find_elements(By.CLASS_NAME, "ipc-metadata-list-summary-item")
                total_on_page = len(movie_cards)
                
                # 2. Extract data from NEW cards only

                for card in movie_cards[collected_count:]:
                    try:
                        title = card.find_element(By.CLASS_NAME, "ipc-title__text").text
                        # Clean the title (remove the number like "1. ")
                        title = title.split(". ", 1)[-1] if ". " in title else title
                    except:
                        title = "N/A"
                    try:
                        storyline = card.find_element(By.CLASS_NAME, "ipc-html-content-inner-div").text
                    except:
                        storyline = "N/A"
                    self.movies.append({"Movie Name": title, "Storyline": storyline})
                collected_count = total_on_page
                print(f"✅ Collected {collected_count} movies so far...")

                # 3. Handle the "50 More" Button
                if not self._click_load_more(total_on_page):
                    break

            except Exception as e:
                print(f"Stopped or finished: {e}")
                break

        self._save_data()
        self.driver.quit()

    def _click_load_more(self, current_count):
        """Internal helper to find and click the load more button."""
        try:
            # Look for button specifically containing '50 more'
            button = self.driver.find_element(By.XPATH, "//button[.//span[contains(text(),'50 more')]]")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
            time.sleep(1)
            button.click()
            
            # Wait for the count to actually increase
            self.wait.until(lambda d: len(d.find_elements(By.CLASS_NAME, "ipc-metadata-list-summary-item")) > current_count)
            return True
        except:
            print("🏁 No more movies to load.")
            return False

    def _save_data(self):
        df = pd.DataFrame(self.movies)
        filename = f"imdb_movies_{self.year}.csv"
        df.to_csv(filename, index=False)
        print(f"📂 Data saved successfully to {filename}")

# --- MAIN Method to start ---

if __name__ == "__main__":
    # Get user input for the year
    target_year = input("Enter the year you want to scrape (e.g., 2024): ")
    
    # Create the 'intern' (object) and tell them to work
    scraper = IMDBScraper(target_year)
    scraper.scrape()