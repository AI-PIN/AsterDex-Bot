import requests  # For fetching AsterDEX data 
from ai_pin import AIPinAgent  
import time  # For periodic updates

# Fetch real-time AsterDEX market data
def get_aster_data(symbol='BTCUSDT'):
    url = f"https://fapi.asterdex.com/fapi/v1/ticker/24hr?symbol={symbol}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for errors
        return response.json()
    except Exception as e:
        print(f"Error fetching Aster data: {e}")
        return None

# Analyze data with AI-Pin and generate trading tip
def analyze_with_aipin(data, api_key):
    try:
        agent = AIPinAgent(api_key=api_key)  # Initialize AI-Pin agent
        prompt = f"Analyze this AsterDEX data for trading tips: {data}"
        insight = agent.query(prompt)  # Get AI-generated tip
        return insight
    except Exception as e:
        print(f"AI-Pin error: {e}")
        return "AI analysis failed. Try again later."

# Main loop: Fetch data, analyze, print every 60 seconds
def main():
    api_key = "YOUR_AIPIN_API_KEY"  # Replace with your AI-Pin API key from ai-pin.io
    symbol = "BTCUSDT"  # Example trading pair
    while True:
        data = get_aster_data(symbol)
        if data:
            insight = analyze_with_aipin(data, api_key)
            print(f"[$ASTER Scout] {symbol} Insight: {insight}")
        time.sleep(60)  # Wait 60 seconds before next check

if __name__ == "__main__":
    main()
