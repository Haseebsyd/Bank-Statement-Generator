import pandas as pd

def get_transactions(csv_path, user_email, start_date, end_date):
    transactions = pd.read_csv(csv_path)

    transactions['date_of_transaction'] = pd.to_datetime(transactions['date_of_transaction'])
    
    filtered_transactions = transactions[
        (transactions['user_email'] == user_email) &
        (transactions['date_of_transaction'] >= pd.to_datetime(start_date)) &
        (transactions['date_of_transaction'] <= pd.to_datetime(end_date))
    ]

    return filtered_transactions
