import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def fetch_events():
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = uc.Chrome(options=options)
    wait = WebDriverWait(driver, 20)

    # Phase 1: Listing page → gather links & titles
    driver.get("https://www.eventbrite.com.au/d/australia--sydney/events/")
    time.sleep(3)
    for _ in range(6):
        driver.execute_script("window.scrollBy(0, window.innerHeight);")
        time.sleep(2)

    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "section.discover-vertical-event-card")
    ))
    cards = driver.find_elements(By.CSS_SELECTOR, "section.discover-vertical-event-card")
    print(f"✅ Found {len(cards)} event cards on the listing page")

    items = []
    for card in cards:
        try:
            a = card.find_element(By.CSS_SELECTOR, "a.event-card-link")
            href  = a.get_attribute("href")
            title = a.get_attribute("aria-label") or a.text
            if title.lower().startswith("view "):
                title = title[5:]
            items.append({"title": title, "link": href})
        except:
            continue

    # Phase 2: Visit each detail page for date & description
    events = []
    for idx, item in enumerate(items, 1):
        driver.get(item["link"])
        print(f"→ Visiting [{idx}/{len(items)}]: {item['title']}")
        # Wait for the detail page’s time element
        try:
            tm = wait.until(EC.presence_of_element_located((By.TAG_NAME, "time")))
            date = tm.text.strip()
        except:
            date = "N/A"

        # First descriptive paragraph
        try:
            desc = driver.find_element(
                By.CSS_SELECTOR,
                "div[class*='structured-content'] p"
            ).text.strip()
        except:
            desc = "N/A"

        events.append({
            "title":       item["title"],
            "link":        item["link"],
            "date":        date,
            "description": desc
        })
        time.sleep(1)  # small throttle

    driver.quit()
    return events

if __name__ == "__main__":
    evts = fetch_events()
    print("\n🎉 Scraped Events:\n")
    for e in evts:
        print(f"Title      : {e['title']}")
        print(f"Date/Time  : {e['date']}")
        print(f"Link       : {e['link']}")
        print(f"Description: {e['description'][:100]}…\n")
