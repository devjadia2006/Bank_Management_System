# My Bank – Bank Management System

A simple Bank Management System built with **Python** and **Streamlit**, featuring a premium **Luxury Black & Gold** user interface.

## Features

- **Dashboard** – View the total number of accounts and total bank balance.
- **Create Account** – Register a new account with account holder details and an initial balance.
- **OTP Verification** – Verify a newly submitted account using a demo OTP displayed in the application.
- **Deposit Money** – Add money to an existing account.
- **Withdrawal** – Withdraw money with balance validation and custom exception handling.
- **Money Transfer** – Transfer money between two different accounts.
- **Search Account** – Find an account using its account number.
- **All Accounts** – View account details and transaction history.

## Technology Used

- Python
- Streamlit
- Python `random` module

## Project Files

```text
Bank-Management-System/
├── app.py
├── README.md
└── requirements.txt
```

## Requirements

- Python 3.9 or later
- pip (Python package installer)

Install the required Python package:

```bash
pip install -r requirements.txt
```

## How to Run

1. Download or clone the project.
2. Open a terminal in the project folder.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the Streamlit application:

   ```bash
   python -m streamlit run app.py
   ```

5. Streamlit will display a local URL in the terminal. Open that URL in your web browser.

## How to Use

1. Open **Create Account** from the sidebar.
2. Enter the account holder's details and initial balance.
3. Submit the form and use the demo OTP displayed on the page to verify the account.
4. Use **Deposit**, **Withdrawal**, and **Money Transfer** to perform transactions.
5. Use **Search Account** or **All Accounts** to view account information and transaction history.
6. Return to **Dashboard** to view account totals.

## Important Notes

- This is an educational/demo project, not a production banking application.
- The OTP is displayed inside the application for demonstration. It is not sent by SMS or email.
- Account data is stored in Streamlit session state. It is temporary and may be lost when the session or application is restarted.
- The application does not use a persistent database or real bank/payment network.
- Do not enter real banking credentials or sensitive financial information.

## Author

Add your name and college details here if required.
