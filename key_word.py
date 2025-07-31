
def get_keywords(stock_name: str,client):
    prompt = f"""Give me exactly 25 one word keywords in singular form including the stock name and 5 of its competitors that are directly or indirectly related to the company or stock '{stock_name}' and could affect its stock price in the news.

    Output only the keywords, separated by commas. Do not include any explanation, numbers, or bullet points."""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
         messages=[
        {"role": "system", "content": "You're a financial analyst."},
        {"role": "user", "content": prompt}
    ],
        temperature=0.8
    )

    keywords_raw = response.choices[0].message.content.strip()
    keywords = [k.strip() for k in keywords_raw.split(",") if k.strip()]
    return keywords
