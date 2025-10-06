import requests  # For fetching AsterDEX data
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

# Mock AI analysis (no API key needed)
def analyze_with_aipin(data):
    if not data:
        return "No data to analyze. Try again later."
    price = float(data['lastPrice'])
    change = float(data['priceChangePercent'])
    tip = f"{data['symbol']}: Current price ${price:.2f}, 24h change {change:.2f}%."
    if change > 2:
        tip += " Bullish! Consider a long (get advanced AI at ai-pin.io)."
    elif change < -2:
        tip += " Bearish! Consider a short (get advanced AI at ai-pin.io)."
    else:
        tip += " Neutral. Monitor for breakout (get advanced AI at ai-pin.io)."
    return tip

# Main loop: Fetch data, analyze, print every 60 seconds
def main():
    symbol = "BTCUSDT"  # Example trading pair
    while True:
        data = get_aster_data(symbol)
        if data:
            insight = analyze_with_aipin(data)
            print(f"[$ASTER Scout] {insight}")
        time.sleep(60)  # Wait 60 seconds before next check

if __name__ == "__main__":
    main()
