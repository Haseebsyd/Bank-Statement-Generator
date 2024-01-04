from flask import Flask, request, jsonify
from flask_cors import CORS
from database_service import get_transactions
from pdf_service import create_pdf
from email_service import send_email_with_attachment
import os

app = Flask(__name__)
CORS(app, resources={r"/generate-statement": {"origins": "http://localhost:3000"}})  # Enable CORS for all routes

@app.route('/')
def home():
    return "Bank Statement Generation Service"

def process_bank_statement(selected_user_email, start_date, end_date, first_name, last_name, email):
    csv_file_path = './transactions.csv'
    pdf_file_name = 'statement.pdf'
    pdf_file_path = os.path.join(os.getcwd(), pdf_file_name)
    
    transactions = get_transactions(csv_file_path, selected_user_email, start_date, end_date)
    create_pdf(transactions, pdf_file_path, first_name, last_name, selected_user_email)  # Ensure create_pdf accepts these args
    
    send_email_with_attachment(email, pdf_file_path, first_name=first_name, last_name=last_name, user_email=selected_user_email)

@app.route('/generate-statement', methods=['POST'])
def generate_statement():
    data = request.json
    start_date = data.get('startDate')
    end_date = data.get('endDate')
    user_email = data.get('email')
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    selected_user_email = data.get('selectedUserEmail')

    # Validate the input
    if not all([start_date, end_date, user_email, selected_user_email, first_name, last_name]):
        return jsonify({'error': 'Missing data'}), 400

    try:
        process_bank_statement(selected_user_email, start_date, end_date, first_name, last_name, user_email)
        return jsonify({'message': 'Statement generation completed', 'email': selected_user_email})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)