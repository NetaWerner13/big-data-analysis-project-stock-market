import csv
import random
from datetime import datetime, timedelta
import yfinance as yf

# List of companies from various countries
companies = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA',  # USA
    'NVDA', 'JPM', 'V', 'JNJ', 'WMT',  # USA
    'BABA', 'TCEHY', 'PDD', 'BIDU', 'NIO',  # China
    '005930.KS', '000660.KS', '035420.KS',  # South Korea (Samsung, SK Hynix, NAVER)
    'TTE', 'LVMUY', 'OR.PA', 'SAN.PA',  # France
    'SAP', 'VOW3.DE', 'SIE.DE', 'ALV.DE',  # Germany
    'HSBC', 'GSK', 'BP', 'VOD',  # UK
    'TM', 'SONY', '7974.T', '6758.T',  # Japan
    'RY.TO', 'TD.TO', 'ENB.TO', 'CNR.TO',  # Canada
    'RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS',  # India
    'VALE3.SA', 'PETR4.SA', 'ITUB4.SA',  # Brazil
    'NESN.SW', 'ROG.SW', 'NOVN.SW',  # Switzerland
    'ASX.AX', 'BHP.AX', 'NAB.AX',  # Australia
    '7203.T', '9984.T', '9433.T',  # Japan (Toyota, SoftBank, KDDI)
]


# get the current price of a stock using yfinance
def get_current_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        current_price = stock.history(period='1d')['Close'][0]
        return current_price
    except Exception as e:
        print(f"Could not retrieve price for {ticker}: {e}")
        return None


# generate random order flow data based on actual prices
# set the number of records to 100,000 by default, can be changed as needed
def generate_mock_data(ticker, base_price, num_records=100000):
    data = []
    current_time = datetime.now()
    for _ in range(num_records):
        timestamp = current_time.strftime('%Y-%m-%d %H:%M:%S')
        price_variation = random.uniform(-0.05, 0.05)  # Slight variation up or down (5%)
        price = round(base_price * (1 + price_variation), 2)
        volume = random.randint(1, 10000)  # Random volume between 1 and 10,000
        action = random.choice(['BUY', 'SELL'])
        data.append([ticker, timestamp, price, volume, action])
        current_time -= timedelta(seconds=random.randint(1, 60))  # Decrement time by a random number of seconds
    return data


# Create a CSV file and write the data
def create_csv(filename='order_flow_data.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ticker', 'timestamp', 'price', 'volume', 'action'])
        for company in companies:
            base_price = get_current_price(company)
            if base_price:  # Only generate data if the price was successfully retrieved
                mock_data = generate_mock_data(company, base_price)
                writer.writerows(mock_data)
    print(f"{filename} created successfully!")


if __name__ == '__main__':
    create_csv()
