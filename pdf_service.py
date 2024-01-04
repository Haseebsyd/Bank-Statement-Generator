from fpdf import FPDF
import pandas as pd
from datetime import datetime

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Bank Statement', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

def create_pdf(transactions, filename, first_name, last_name, selected_user_email):
    pdf = PDF()
    pdf.add_page()

    # Metadata
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f'For: {first_name} {last_name}', 0, 1, 'L')
    pdf.cell(0, 10, 'Requested on: ' + datetime.now().strftime('%B %d, %Y'), 0, 1, 'L')
    pdf.ln(10)

    # Table
    pdf.set_font("Arial", 'B', 12)
    col_width_date = (pdf.w - 20) / 2
    col_width_amount = (pdf.w - 20) / 2

    # Print the headers
    pdf.cell(col_width_date, 10, 'Date', border=1, align='C')
    pdf.cell(col_width_amount, 10, '$ Amount (USD)', border=1, ln=1, align='C')

    # Print the rows
    pdf.set_font("Arial", size=12)
    total_spent = 0
    for index, transaction in transactions.iterrows():
        date = transaction['date_of_transaction'].strftime('%B %d, %Y')
        amount = transaction['amount']
        total_spent += amount
        pdf.cell(col_width_date, 10, date, border=1, align='C')
        pdf.cell(col_width_amount, 10, f"{amount:.2f}", border=1, ln=1, align='C')

    # Summary
    pdf.ln(10)
    pdf.set_font("Arial", '', 12)
    total_transactions = len(transactions)
    average_spent = total_spent / total_transactions if total_transactions > 0 else 0
    summary = (
        f"{selected_user_email} has spent a total of ${total_spent:.2f} from "
        f"{transactions['date_of_transaction'].min().strftime('%B %d, %Y')} to "
        f"{transactions['date_of_transaction'].max().strftime('%B %d, %Y')}. "
        f"There is a total of {total_transactions} transactions and "
        f"the average spent per transaction is ${average_spent:.2f}."
    )
    pdf.multi_cell(0, 10, summary)

    pdf.output(filename)
