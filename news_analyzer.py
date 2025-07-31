

def analyze_news(stock_name, headline, description, article_body,client):
    print("ENTERED analyzer")
    prompt = f"""
    Study the following news and make intelligent decisions about will this news may or may not affect the stock price of this company {stock_name}.
    -1 to 1 give range on how much will this news affect the {stock_name} 
    
    Output in readable format and include a TL&DR

    Headline: {headline}
    Description: {description}
    Body: {article_body}
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
         messages=[
        {"role": "system", "content": "You're a stock market analyst who helps people to make right decisions regarding stock prices od companies."},
        {"role": "user", "content": prompt}
    ],
        temperature=0.8
    )
    

    return response.choices[0].message.content.strip()
