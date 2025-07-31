# app.py
from flask import Flask, request, jsonify, render_template
from key_word import get_keywords
from news_analyzer import analyze_news
from tracker import watch_latest_news
from openai import OpenAI
from tele import send_telegram_message
client = OpenAI(api_key='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') 


app = Flask(__name__)
latest_matches = []
tracker_started = False  # ✅ to prevent re-triggering
stock_selected = None  # 🔑 Remember which stock was selected

def handle_matched_article(article):
    print("📢 Matched:", article["headline"])
    print(article["headline"])
    print(article["description"])
    try:
        analysis = analyze_news(
            stock_name=stock_selected,
            headline=article["headline"],
            description=article["description"],
            article_body=article["body"],
            client=client
        )

        message = f"""📊 *AI Analysis:*
                {analysis}

                📰 *Headline:* {article['headline']}

                📄 *Summary Snippet:*
                {article['body'][:500]}...

                🔗 [Read more]({article['url']})
                """
        send_telegram_message(analysis)
    except Exception as e:
        article["analysis"] = f"❌ Analysis failed: {e}"

    latest_matches.append(article)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_keywords', methods=['POST'])
def keyword_route():
    global tracker_started
    stock_name = request.form.get('stock')
    try:
        keywords = get_keywords(stock_name,client)

        if not tracker_started:
            tracker_started = True
            watch_latest_news(handle_matched_article, keywords)  #  start tracker with keywords

        return jsonify({"keywords": keywords})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/latest')
def latest_news():
    return jsonify(latest_matches[-1] if latest_matches else {})

if __name__ == '__main__':
    app.run(debug=True)
