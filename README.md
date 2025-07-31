# 🧠 Stock Impact Sentinel  
**Real-Time News + Generative AI + Telegram Alerts**  
*Intelligently monitors stock news and alerts you in seconds.*

---

## ✨ What It Does

A fully automated system that:
- Understands a stock’s context using **Generative AI**
- Scrapes **live news** from financial websites
- Uses AI to assess whether the news will **impact your stock**
- Sends the result instantly via **Telegram**

Built for traders, analysts, and teams who need to know:  
> _“Will this news affect my stock — and how?”_

---

## ⚙️ How It Works

1. 🧾 **Stock Input**  
   Enter a stock name (e.g., `Tata Power`) through a simple form or script.

2. 🧠 **Smart Keyword Expansion (GenAI)**  
   ChatGPT generates 20–30 highly relevant keywords — including:
   - Sector-specific terms (*power outage*, *energy reforms*)
   - Competitors (*Adani*, *NTPC*, etc.)
   - Market context (*tariff*, *policy change*, *IPO*)

3. 🕸️ **Real-Time Web Scraping Engine**  
   A **real browser** (via Playwright) loads financial news websites as a user would.  
   It dynamically scans breaking headlines and full text for keyword matches — **no reliance on RSS feeds or APIs**.

4. 🧠 **AI Impact Analysis**  
   Matching articles are passed to ChatGPT to assess:
   - Whether the news affects the stock
   - If so, the **type of impact** (📈 Positive / 📉 Negative / ⚖️ Neutral)
   - A **brief explanation** behind the conclusion

5. 📲 **Telegram Ping**  
   If relevant, a concise message is sent instantly:


# 🧰 Tech Stack

| Component            | Tools Used                  |
|----------------------|-----------------------------|
| **Language**         | Python                      |
| **Browser Automation** | Playwright                 |
| **GenAI Integration** | OpenAI GPT-4 API            |
| **News Analysis**    | Natural Language Prompting  |
| **Notifications**    | Telegram Bot API            |
| **Keyword Logic**    | Regex, Prompt Chaining      |

---

## ✅ Highlights

- ✅ Real-time scraping — powered by browser automation
- ✅ 20–30 rich keywords generated using GenAI
- ✅ Only sends alerts if news is relevant to your stock
- ✅ AI explains the impact — not just sentiment
- ✅ Fully automated from input to Telegram ping

---

## 🔐 Local Setup

```bash
git clone https://github.com/yourusername/stock-impact-sentinel.git
cd stock-impact-sentinel
pip install -r requirements.txt
