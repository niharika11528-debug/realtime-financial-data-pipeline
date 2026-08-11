import pandas as pd
import glob
import os

def process_live_stream():
    # 1. Scan the stream buffer path for raw real-time ticks
    buffer_files = glob.glob("/tmp/streaming_buffer/ticks_*.parquet")
    if not buffer_files:
        print("Waiting for streaming data chunks... Buffer is currently empty.")
        return
        
    latest_stream_chunk = max(buffer_files, key=os.path.getctime)
    print(f"Ingesting latest streaming data block: {latest_stream_chunk}")
    df = pd.read_parquet(latest_stream_chunk)
    
    # 2. Apply real-time transformations and streaming feature engineering
    df['trade_timestamp'] = pd.to_datetime(df['timestamp'])
    df['total_order_value'] = round(df['trade_price'] * df['trade_volume'], 2)
    
    # Financial Anomaly Detection Rule: Flag trades with total values exceeding $50,000
    df['is_high_value_anomaly'] = df['total_order_value'] > 50000.0
    
    # 3. Clean up formatting and structure the final streaming analytical view
    refined_stream = df[['trade_timestamp', 'symbol', 'trade_price', 'trade_volume', 'total_order_value', 'is_high_value_anomaly']]
    
    # 4. Stream and append directly down into the enterprise warehouse data lake
    os.makedirs("data/warehouse", exist_ok=True)
    lake_target = "data/warehouse/fact_market_streams.parquet"
    
    if os.path.exists(lake_target):
        existing_lake_df = pd.read_parquet(lake_target)
        final_consolidated_df = pd.concat([existing_lake_df, refined_stream], ignore_index=True)
    else:
        final_consolidated_df = refined_stream
        
    final_consolidated_df.to_parquet(lake_target, index=False)
    print(f"Successfully processed stream chunk. Streaming warehouse dataset updated at: {lake_target}")
    
    # Clear out the read buffer file to maintain a lean streaming profile
    os.remove(latest_stream_chunk)

if __name__ == "__main__":
    process_live_stream()

