import pandas as pd
import requests

def get_EOD_bids(start_date, end_date):
    """Pulls real time data from Theta Data and organizes the bids
into a tuple. 
    """

    request = requests.get(
            url = 'http://127.0.0.1:25510/v2/hist/stock/eod',
            params = {
                "root": "NVDA",
                "start_date": start_date,
                "end_date": end_date,
                "use_csv": "false" 
            }
        )
    data = request.json()
    df = pd.DataFrame(data=data['response'], columns=data['header']['format'])
    list = df['bid'].tolist()
    bid_tuple = tuple(list)
    return bid_tuple