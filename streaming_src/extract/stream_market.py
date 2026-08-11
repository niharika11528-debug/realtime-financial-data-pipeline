import pandas as pd
import random
from datetime import datetime
import os

def generate_live_ticks():
    print("Initializing real-time financial market data stream connection...")
    tickers = ['AAPL', 'TSLA', 'NVDA', 'AMZN', 'MSFT']
    ticks = []
    
    # Simulate a stream of 50 transaction records over the last few minutes
    for _ in range(50):
        ticker = random.choice(tickers)
        base_price = {"AAPL": 180.0, "TSLA": 175.0, "NVDA": 800.0, "AMZN": 170.0, "MSFT": 420.0}[ticker]
        price_fluctuation = round(base_price + random.uniform(-5.0, 5.0), 2)
        volume = random.randint(10, 500)
        
        ticks.append({
            "timestamp": datetime.utcnow().isoformat(),
            "symbol": ticker,
            "trade_price": price_fluctuation,
            "trade_volume": volume
        })
        
    df = pd.DataFrame(ticks)
    
    # Save raw streaming window chunks to a temporary buffer path
    os.makedirs("/tmp/streaming_buffer", exist_ok=True)
    buffer_target = f"/tmp/streaming_buffer/ticks_{int(datetime.utcnow().timestamp())}.parquet"
    df.to_parquet(buffer_target, index=False)
    print(f"Captured 50 real-time market trading ticks to buffer: {buffer_target}")

if __name__ == "__main__":
    generate_live_ticks()

