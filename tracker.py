from playwright.sync_api import sync_playwright
import json, time, random, re, html
from datetime import datetime
from dateutil import parser as date_parser
import threading

last_seen_time = datetime.min

def contains_keyword(text, keywords):
    return any(re.search(rf"\b{k}\b", text, re.IGNORECASE) for k in keywords)

def watch_latest_news(callback, keywords):
    def _run():
        global last_seen_time

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            print("🔁 Real-time news tracker started...")

            while True:
                try:
                    page.goto("https://www.ndtv.com/latest?pfrom=home-ndtv_mainnavigation", wait_until='domcontentloaded')
                    top_news = page.locator("a[class='NwsLstPg_ttl-lnk']").first
                    url = top_news.get_attribute("href")

                    if not url:
                        print("❌ No top news link found. Retrying...")
                        time.sleep(5)
                        continue

                    article_page = context.new_page()
                    article_page.goto(url, timeout=60000, wait_until='domcontentloaded')
                    time.sleep(random.uniform(1, 2))

                    scripts = article_page.locator("script[type='application/ld+json']").all()

                    for script in scripts:
                        try:
                            data = json.loads(script.inner_text())
                            if data.get("@type") == "NewsArticle":
                                date_published = date_parser.parse(html.unescape(data.get("datePublished", ""))).replace(tzinfo=None)

                                if date_published <= last_seen_time:
                                    article_page.close()
                                    print("⏩ Skipping old article")
                                    break

                                last_seen_time = date_published
                                headline = data.get("headline", "")
                                description = data.get("description", "")
                                body = data.get("articleBody", "")

                                full_text = f"{headline} {description} {body}"
                                if contains_keyword(full_text, keywords):
                                    article = {
                                        "headline": headline,
                                        "description": description,
                                        "body": body,
                                        "url": url,
                                        "published": str(date_published)
                                    }
                                    callback(article)
                                else:
                                    print(f"ℹ️ New article, but no keyword match: {headline}")

                                article_page.close()
                                break
                        except Exception as e:
                            continue

                    if not article_page.is_closed():
                        article_page.close()

                except Exception as e:
                    print(f"❌ Error during scraping: {e}")

                time.sleep(10)

            browser.close()

    thread = threading.Thread(target=_run, daemon=True)
    thread.start()
