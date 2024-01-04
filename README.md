Application For Internship ZYWA  ---  Software Engineer at Zywa (W22)

Muhammad Haseeb Syed


Portfolio: https://haseebsyd.github.io
GitHub: https://github.com/Haseebsyd
LinkedIn: https://linkedin.com/in/haseeb--syed


{
    *** DISCLAIMER *** 
        - Assumptionss were made throughout the creation of this project due to the rules being quite vauge throughot the email.
        1. Was quite confused about the CSV file and if youd enter one or if I would create it, So there is a CSV attached with three columns (emails (id), transactionDate, $ in USD)
            ^^^ ONLY DATES 2022-01-01 TO 2022-12-12 ^^^
        2. Email_Service has a hard coded email account and hashed pass, the security is pretty much non existant. 
    *** DISCLAIMER *** 
}

Project Overview
This project aims to provide a banking application service that allows users to generate a PDF statement of their transactions within a specific date range. The statement is then emailed to the user's specified address. The project consists of a React frontend, a Flask API backend, and auxiliary services for database access, PDF generation, and email delivery.

Running the Bank Statement Generator Application:
    - This guide will walk you through the steps to set up and run the Bank Statement Generator application on your local machine.

Prerequisites:
    - Before you get started, make sure you have the following installed:

- Python: The application backend is written in Python. You need Python 3.6 or higher. You can download it from python.org.
- pip: The Python package installer, which usually comes with Python.
- Node.js and npm: The execution environment for React. Download them from nodejs.org.
- Virtual Environment: A tool for creating isolated Python environments. You can install it via pip if it's not already installed with 'pip install virtualenv'.

Setup Instructions
1. Extract the Project
    Unzip the provided project file to your desired location.

2. Backend Setup
    Navigate to the backend directory of the unzipped project folder in your terminal or command prompt.

        a. Create a Virtual Environment
            'python -m venv venv'
            - This command creates a virtual environment named venv. You can name it anything you like.

        b. Activate the Virtual Environment
            On Windows:
            '.\venv\Scripts\activate'

            On macOS and Linux:
            'source venv/bin/activate'

        c. Install Dependencies
            - With the virtual environment activated, install the required Python packages using pip:
            'pip install -r requirments.txt'
            - The requirments.txt file contains all the necessary Python packages.

        d. Start the Backend Server
            - Run the following command to start the Flask server:
            'python app.py'
            - The backend server will start, and you should see a message indicating it's running on http://127.0.0.1:5000/.

3. Frontend Setup
    Open a new terminal or command prompt window and navigate to the frontend directory of the unzipped project folder.

        a. Install Node Modules
        - Install the required npm packages with:
        'npm install'
        - This command reads the package.json file and installs all the necessary dependencies for the React application.

        b. Start the React Development Server
        - Once the installation is complete, start the frontend application by going further into the directory (frontend ('cd .\bank-statement-frontend')):
        'npm start'
        - This command starts the development server, and your default web browser should open automatically to http://localhost:3000/.

Using the Application:
With both servers running, you can now use the Bank Statement Generator:
    - Fill in your personal information and the details of the enquiry on the form provided on the frontend application.
    - Click "Generate Statement" to request the bank statement.
    - If everything is set up correctly, you will receive an alert indicating the statement generation is in progress, and the PDF will be sent to the email address you provided.

Troubleshooting:
    - If you encounter any issues with the Python backend, ensure that the virtual environment is activated and all dependencies are installed.
    - If the React application fails to start, check that all npm packages are installed correctly.
    - For any CORS issues, ensure that the Flask backend has CORS set up for the React application's origin.
    - By following these instructions, you should be able to run the Bank Statement Generator application successfully on your local machine. If you encounter any issues, double-check each step and ensure all prerequisites are correctly installed.



Technologies Used:

Frontend
React: 
    - Chosen for its component-based architecture, which allows for efficient and organized UI development. React's state management makes it simple to handle user inputs and interactions.

Backend
Flask:
    - A lightweight and flexible Python web framework that provides the tools needed to construct a robust API quickly. Flask was chosen for its simplicity and ease of integration with Python's extensive libraries for data manipulation and PDF generation.

Database Service
Pandas: 
    - A powerful data analysis and manipulation library for Python, which simplifies CSV file operations. Pandas was used for its intuitive syntax and comprehensive set of functions for reading and filtering datasets.

PDF Generation
FPDF: 
    - A library that allows for easy PDF generation using Python. It was selected due to its simplicity and the control it offers over the document's layout and content.

Email Service
smtplib: 
    - A Python library used to define an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.



Service Architecture
    The services are designed to operate independently to adhere to the principles of microservices architecture. They interact with each other through the Flask API, ensuring a clear separation of concerns.

API Service:
    - The API accepts a POST request with the user's email, start date, and end date for the transaction period. It performs validation checks before proceeding with the statement generation process.

Database Service:
    - This service reads the transaction data from a CSV file and filters it based on the user's email and the provided date range. It returns the relevant transaction data for further processing.

PDF Generation Service:
    - It takes the filtered transaction data and generates a PDF document. The document contains a header, a table of transactions, and a summary that includes the total amount spent, the number of transactions, and the average transaction amount.

Email Service:
    - Once the PDF is generated, this service sends the document as an email attachment to the user's specified email address.



Security Considerations
To add authorization and authentication:
    - Implement an OAuth 2.0 provider to issue tokens upon successful authentication.
    - Use JWT (JSON Web Tokens) to secure API endpoints. The tokens would be checked for validity on every request to the server.
    - Incorporate HTTPS to encrypt data in transit between the client and server.
    - Store sensitive data like SMTP credentials and secret keys securely using environment variables or a secret management service.
    - Authorization and Authentication Implementation
    - User Registration and Login: Users must register and log in to access the statement generation service. Their credentials would be stored securely in a database with hashed passwords.

Token Generation: 
    Upon login, a JWT would be issued to the user, containing an identifier and an expiration time.

Secured Endpoints: 
    Each endpoint in the Flask API would require a valid JWT in the request header for access.

Token Verification: 
    The Flask API would verify the JWT on each request using a secret key. If the token is invalid or expired, the request would be denied.

HTTPS: 
    Secure HTTP would ensure that data exchanged between the client and server is encrypted.

Conclusion
The chosen technologies and frameworks provide a robust and scalable solution for a mid level bank statement generation. The addition of authorization and authentication will further enhance the security of the users' sensitive data.

For future improvements, integrating a database system such as PostgreSQL for user management and transaction logging, and implementing a frontend framework like Redux for state management across components, would make the application even more resilient and user-friendly.