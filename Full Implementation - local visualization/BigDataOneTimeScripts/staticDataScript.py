import csv
import yfinance as yf

# List of companies from various countries
companies = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA',  # USA
    'NVDA', 'JPM', 'V', 'JNJ', 'WMT',         # USA
    'BABA', 'TCEHY', 'PDD', 'BIDU', 'NIO',    # China
    '005930.KS', '000660.KS', '035420.KS',    # South Korea (Samsung, SK Hynix, NAVER)
    'TTE', 'LVMUY', 'OR.PA', 'SAN.PA',        # France
    'SAP', 'VOW3.DE', 'SIE.DE', 'ALV.DE',     # Germany
    'HSBC', 'GSK', 'BP', 'VOD',               # UK
    'TM', 'SONY', '7974.T', '6758.T',         # Japan
    'RY.TO', 'TD.TO', 'ENB.TO', 'CNR.TO',     # Canada
    'RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS',   # India
    'VALE3.SA', 'PETR4.SA', 'ITUB4.SA',       # Brazil
    'NESN.SW', 'ROG.SW', 'NOVN.SW',           # Switzerland
    'ASX.AX', 'BHP.AX', 'NAB.AX',             # Australia
    '7203.T', '9984.T', '9433.T',             # Japan (Toyota, SoftBank, KDDI)
]

def get_static_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        static_data = {
            'ticker': ticker,
            'company_name': info.get('longName', 'N/A'),
            'shares_outstanding': info.get('sharesOutstanding', 'N/A'),
            'exchange': info.get('exchange', 'N/A'),
            'index': info.get('index', 'N/A'),
            'sector': info.get('sector', 'N/A'),
            'industry': info.get('industry', 'N/A'),
            'country': info.get('country', 'N/A'),
            'ipo_date': info.get('ipoExpectedDate', 'N/A')
        }
        return static_data
    except Exception as e:
        print(f"Could not retrieve data for {ticker}: {e}")
        return None

def create_static_data_csv(filename='stocks_static_data.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=[
            'ticker', 'company_name', 'shares_outstanding', 'exchange', 'index',
            'sector', 'industry', 'country', 'ipo_date'
        ])
        writer.writeheader()
        for company in companies:
            static_data = get_static_data(company)
            if static_data:  # Only write data if it was successfully retrieved
                writer.writerow(static_data)
    print(f"{filename} created successfully!")


if __name__ == '__main__':
    create_static_data_csv()
