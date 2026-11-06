import streamlit as st
import random


# -------------------------------
# Custom Exception
# -------------------------------
class WithdrawalException(Exception):
    pass


# -------------------------------
# Bank Account Class
# -------------------------------
class BankDemoA:

    def __init__(self, name, account_no, phone, email,
                 branch, balance):

        self.Name = name
        self.Accountno = account_no
        self.PhoneNo = phone
        self.Email = email
        self.Branch = branch
        self.Balance = balance
        self.transactions = []

    # Deposit Function
    def deposit(self, amount):

        if amount <= 0:
            return False, "Enter a valid deposit amount."

        self.Balance += amount
        self.transactions.append(
            f"Deposited: Rs. {amount:,.2f}"
        )

        return True, "Deposit Successfully Completed!"

    # Withdrawal Function
    def withdrawal(self, amount):

        try:
            if amount <= 0:
                raise WithdrawalException(
                    "Enter a valid withdrawal amount."
                )

            if amount > self.Balance:
                raise WithdrawalException(
                    "Insufficient Bank Balance!"
                )

            self.Balance -= amount
            self.transactions.append(
                f"Withdrawn: Rs. {amount:,.2f}"
            )

            return True, "Withdrawal Successfully Completed!"

        except WithdrawalException as e:
            return False, str(e)

    # Money Transfer Function
    def transfer(self, receiver, amount):

        if amount <= 0:
            return False, "Enter a valid transfer amount."

        if self.Accountno == receiver.Accountno:
            return False, "You cannot transfer money to the same account."

        if amount > self.Balance:
            return False, "Insufficient Balance!"

        # Update both account balances
        self.Balance -= amount
        receiver.Balance += amount

        # Update both transaction histories
        self.transactions.append(
            f"Transferred Rs. {amount:,.2f} to Account {receiver.Accountno}"
        )

        receiver.transactions.append(
            f"Received Rs. {amount:,.2f} from Account {self.Accountno}"
        )

        return True, "Money Transferred Successfully!"

    # Display Function
    def display(self):

        st.subheader("Account Details")
        st.write("**Name:**", self.Name)
        st.write("**Account Number:**", self.Accountno)
        st.write("**Phone Number:**", self.PhoneNo)
        st.write("**Email:**", self.Email)
        st.write("**Branch:**", self.Branch)

        st.metric(
            "Current Balance",
            f"Rs. {self.Balance:,.2f}"
        )


# -------------------------------
# Streamlit Configuration
# -------------------------------
st.set_page_config(
    page_title="My Bank | Bank_Management_System",
    page_icon="🏦",
    layout="wide"
)


# -------------------------------
# Luxury Black & Gold Theme
# -------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

:root {
    --bg: #090909;
    --panel: #141414;
    --panel-soft: #1b1b1b;
    --gold: #d4af37;
    --gold-light: #f2d675;
    --text: #f5f1e7;
    --muted: #aaa397;
}

/* Main application background */
.stApp {
    background:
        radial-gradient(circle at 85% 0%, rgba(212,175,55,.11), transparent 28%),
        linear-gradient(135deg, #080808 0%, #11100d 55%, #080808 100%);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
}

/* Main content width and spacing */
.block-container {
    padding-top: 2.2rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

/* Headings */
h1, h2, h3 {
    color: var(--gold-light) !important;
    font-family: 'Playfair Display', serif !important;
    letter-spacing: .3px;
}
p, label, li, .stMarkdown, .stText {
    color: var(--text);
}
[data-testid="stCaptionContainer"] {
    color: var(--muted);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111111 0%, #090909 100%);
    border-right: 1px solid rgba(212,175,55,.35);
}
[data-testid="stSidebar"] * {
    color: var(--text);
}
[data-testid="stSidebar"] [data-testid="stSelectbox"] > div > div {
    background: #1b1b1b;
    border: 1px solid rgba(212,175,55,.55);
    border-radius: 10px;
}

/* Inputs and select boxes */
.stTextInput input, .stNumberInput input, .stTextArea textarea {
    background: #1b1b1b !important;
    color: #f5f1e7 !important;
    border: 1px solid #5b4a20 !important;
    border-radius: 10px !important;
}
.stTextInput input:focus, .stNumberInput input:focus,
.stTextArea textarea:focus {
    border: 1px solid var(--gold) !important;
    box-shadow: 0 0 0 1px var(--gold) !important;
}
[data-baseweb="select"] > div {
    background: #1b1b1b !important;
    color: #f5f1e7 !important;
    border: 1px solid #5b4a20 !important;
    border-radius: 10px !important;
}
[data-baseweb="popover"], [data-baseweb="menu"] {
    background: #1b1b1b !important;
}
[data-baseweb="menu"] * {
    color: #f5f1e7 !important;
}

/* Buttons */
.stButton > button, .stFormSubmitButton > button {
    background: linear-gradient(135deg, #f2d675 0%, #c49a25 100%) !important;
    color: #111111 !important;
    border: 1px solid #e2c15b !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    padding: .58rem 1.25rem !important;
    transition: all .2s ease-in-out;
}
.stButton > button:hover, .stFormSubmitButton > button:hover {
    background: linear-gradient(135deg, #ffe99a 0%, #d4af37 100%) !important;
    border-color: #ffe99a !important;
    transform: translateY(-1px);
    box-shadow: 0 5px 18px rgba(212,175,55,.2);
}

/* Metrics and cards */
[data-testid="stMetric"] {
    background: linear-gradient(145deg, #1c1b18, #111111);
    border: 1px solid rgba(212,175,55,.42);
    border-radius: 14px;
    padding: 18px 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,.2);
}
[data-testid="stMetricLabel"] {
    color: #c9c0ad !important;
}
[data-testid="stMetricValue"] {
    color: var(--gold-light) !important;
}
[data-testid="stExpander"] {
    background: #151515;
    border: 1px solid rgba(212,175,55,.35);
    border-radius: 12px;
}
[data-testid="stForm"] {
    background: rgba(22,22,22,.82);
    border: 1px solid rgba(212,175,55,.3);
    border-radius: 14px;
    padding: 20px;
}

/* Alerts */
.stAlert {
    border-radius: 10px;
    border: 1px solid rgba(212,175,55,.3);
}

/* Dividers and tables */
hr {
    border-color: rgba(212,175,55,.3) !important;
}
[data-testid="stDataFrame"] {
    border: 1px solid rgba(212,175,55,.35);
    border-radius: 10px;
}

/* Radio and checkbox accents */
.stCheckbox label, .stRadio label {
    color: var(--text) !important;
}

/* Top header and toolbar */
header[data-testid="stHeader"] {
    background: rgba(8,8,8,.75);
}
footer {
    visibility: hidden;
}

/* Small luxury brand mark */
.bank-brand {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 18px 22px;
    margin-bottom: 22px;
    background: linear-gradient(110deg, rgba(212,175,55,.13), rgba(20,20,20,.75));
    border: 1px solid rgba(212,175,55,.4);
    border-radius: 16px;
}
.bank-brand-icon {
    font-size: 34px;
}
.bank-brand-title {
    color: #f2d675;
    font-family: 'Playfair Display', serif;
    font-size: 27px;
    font-weight: 700;
}
.bank-brand-subtitle {
    color: #b8ad98;
    font-size: 12px;
    letter-spacing: 2px;
    text-transform: uppercase;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="bank-brand">
    <div class="bank-brand-icon">🏦</div>
    <div>
        <div class="bank-brand-title">MY BANK</div>
        <div class="bank-brand-subtitle">Premium Banking Experience</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.title("Welcome to Premium Banking")
st.caption("Secure • Simple • Smart Banking Management")


# -------------------------------
# Session State
# -------------------------------
if "accounts" not in st.session_state:
    st.session_state.accounts = []

if "pending_account" not in st.session_state:
    st.session_state.pending_account = None

if "otp" not in st.session_state:
    st.session_state.otp = None


# -------------------------------
# Sidebar Menu
# -------------------------------
menu = st.sidebar.selectbox(
    "Select Operation",
    [
        "Dashboard",
        "Create Account",
        "Deposit",
        "Withdrawal",
        "Money Transfer",
        "Search Account",
        "All Accounts"
    ]
)


# -------------------------------
# Dashboard
# -------------------------------
if menu == "Dashboard":

    st.header("Welcome to My Bank")

    col1, col2 = st.columns(2)

    col1.metric(
        "Total Accounts",
        len(st.session_state.accounts)
    )

    total_balance = sum(
        account.Balance
        for account in st.session_state.accounts
    )

    col2.metric(
        "Total Bank Balance",
        f"Rs. {total_balance:,.2f}"
    )

    st.info("Select an operation from the sidebar.")


# -------------------------------
# Create Account
# -------------------------------
elif menu == "Create Account":

    st.header("Create New Account")

    with st.form("account_form"):

        name = st.text_input("Account Holder Name")
        account_no = st.text_input("Account Number")
        phone = st.text_input("Phone Number")
        email = st.text_input("Email ID")
        branch = st.text_input("Branch Name")

        balance = st.number_input(
            "Initial Balance",
            min_value=0.0,
            step=100.0
        )

        submit = st.form_submit_button("Create Account")

    if submit:

        if not all([
            name.strip(),
            account_no.strip(),
            phone.strip(),
            email.strip(),
            branch.strip()
        ]):
            st.error("Please fill all details.")

        elif any(
            a.Accountno == account_no.strip()
            for a in st.session_state.accounts
        ):
            st.error("Account Number Already Exists!")

        elif st.session_state.pending_account is not None:
            st.warning(
                "Please complete the previous OTP verification first."
            )

        else:
            otp = random.randint(1000, 9999)
            st.session_state.otp = otp

            st.session_state.pending_account = {
                "name": name.strip(),
                "account_no": account_no.strip(),
                "phone": phone.strip(),
                "email": email.strip(),
                "branch": branch.strip(),
                "balance": balance
            }

            st.success("Account details submitted!")

    # OTP Verification
    if st.session_state.pending_account is not None:

        st.divider()
        st.subheader("OTP Verification")

        st.info(f"Demo OTP: {st.session_state.otp}")

        with st.form("otp_form"):

            entered_otp = st.number_input(
                "Enter OTP",
                min_value=0,
                max_value=9999,
                step=1
            )

            verify = st.form_submit_button("Verify OTP")

        if verify:

            if entered_otp == st.session_state.otp:

                data = st.session_state.pending_account

                account = BankDemoA(
                    data["name"],
                    data["account_no"],
                    data["phone"],
                    data["email"],
                    data["branch"],
                    data["balance"]
                )

                st.session_state.accounts.append(account)

                st.session_state.pending_account = None
                st.session_state.otp = None

                st.success("Account Created Successfully!")

            else:
                st.error("Invalid OTP! Please Try Again.")


# -------------------------------
# Deposit
# -------------------------------
elif menu == "Deposit":

    st.header("Deposit Money")

    if st.session_state.accounts:

        account_no = st.selectbox(
            "Select Account",
            [a.Accountno for a in st.session_state.accounts],
            key="deposit_account"
        )

        account = next(
            a for a in st.session_state.accounts
            if a.Accountno == account_no
        )

        st.write("Account Holder:", account.Name)

        amount = st.number_input(
            "Enter Deposit Amount",
            min_value=0.0,
            step=100.0,
            key="deposit_amount"
        )

        if st.button("Deposit Money"):

            success, message = account.deposit(amount)

            if success:
                st.success(message)
                st.metric(
                    "Updated Balance",
                    f"Rs. {account.Balance:,.2f}"
                )
            else:
                st.error(message)

    else:
        st.warning("No Accounts Available!")


# -------------------------------
# Withdrawal
# -------------------------------
elif menu == "Withdrawal":

    st.header("Withdraw Money")

    if st.session_state.accounts:

        account_no = st.selectbox(
            "Select Account",
            [a.Accountno for a in st.session_state.accounts],
            key="withdraw_account"
        )

        account = next(
            a for a in st.session_state.accounts
            if a.Accountno == account_no
        )

        st.write("Account Holder:", account.Name)

        st.metric(
            "Available Balance",
            f"Rs. {account.Balance:,.2f}"
        )

        amount = st.number_input(
            "Enter Withdrawal Amount",
            min_value=0.0,
            step=100.0,
            key="withdraw_amount"
        )

        if st.button("Withdraw Money"):

            success, message = account.withdrawal(amount)

            if success:
                st.success(message)
                st.metric(
                    "Updated Balance",
                    f"Rs. {account.Balance:,.2f}"
                )
            else:
                st.error(message)

    else:
        st.warning("No Accounts Available!")


# -------------------------------
# Money Transfer
# -------------------------------
elif menu == "Money Transfer":

    st.header("💸 Money Transfer")
    st.write("Transfer money from one bank account to another.")

    if len(st.session_state.accounts) >= 2:

        account_numbers = [
            account.Accountno
            for account in st.session_state.accounts
        ]

        with st.form("transfer_form"):

            sender_no = st.selectbox(
                "Select Sender Account",
                account_numbers
            )

            receiver_options = [
                account_no
                for account_no in account_numbers
                if account_no != sender_no
            ]

            receiver_no = st.selectbox(
                "Select Receiver Account",
                receiver_options
            )

            sender = next(
                account for account in st.session_state.accounts
                if account.Accountno == sender_no
            )

            receiver = next(
                account for account in st.session_state.accounts
                if account.Accountno == receiver_no
            )

            st.divider()

            col1, col2 = st.columns(2)

            with col1:
                st.write("**Sender Details**")
                st.write("Name:", sender.Name)
                st.write("Account:", sender.Accountno)
                st.metric(
                    "Available Balance",
                    f"Rs. {sender.Balance:,.2f}"
                )

            with col2:
                st.write("**Receiver Details**")
                st.write("Name:", receiver.Name)
                st.write("Account:", receiver.Accountno)
                st.metric(
                    "Current Balance",
                    f"Rs. {receiver.Balance:,.2f}"
                )

            amount = st.number_input(
                "Enter Transfer Amount",
                min_value=0.0,
                step=100.0
            )

            transfer_button = st.form_submit_button(
                "Transfer Money"
            )

        if transfer_button:

            success, message = sender.transfer(
                receiver,
                amount
            )

            if success:
                st.success(message)

                col1, col2 = st.columns(2)

                col1.metric(
                    "Sender New Balance",
                    f"Rs. {sender.Balance:,.2f}"
                )

                col2.metric(
                    "Receiver New Balance",
                    f"Rs. {receiver.Balance:,.2f}"
                )

                st.info(
                    f"Rs. {amount:,.2f} transferred from "
                    f"{sender.Name} to {receiver.Name}."
                )

            else:
                st.error(message)

    elif len(st.session_state.accounts) == 1:
        st.warning(
            "Only one account exists. Create another account to transfer money."
        )

    else:
        st.warning(
            "No accounts available. Create at least two accounts first."
        )


# -------------------------------
# Search Account
# -------------------------------
elif menu == "Search Account":

    st.header("Search Bank Account")

    search_no = st.text_input("Enter Account Number")

    if st.button("Search"):

        found = False

        for account in st.session_state.accounts:

            if account.Accountno == search_no.strip():

                account.display()
                found = True
                break

        if not found:
            st.error("Account Not Found!")


# -------------------------------
# All Accounts
# -------------------------------
elif menu == "All Accounts":

    st.header("All Bank Accounts")

    if st.session_state.accounts:

        for account in st.session_state.accounts:

            with st.expander(
                f"{account.Name} - {account.Accountno}"
            ):

                account.display()

                st.write("### Transaction History")

                if account.transactions:
                    for transaction in account.transactions:
                        st.write("•", transaction)
                else:
                    st.write("No Transactions Yet.")

    else:
        st.warning("No Accounts Available!")


# -------------------------------
# Premium Footer
# -------------------------------
st.markdown("""
<div style="
    margin-top: 42px;
    padding: 16px 10px;
    text-align: center;
    color: #9f947e;
    border-top: 1px solid rgba(212,175,55,.25);
    font-size: 12px;
    letter-spacing: 1px;">
    MY BANK &nbsp; | &nbsp; PREMIUM BLACK & GOLD EXPERIENCE
</div>
""", unsafe_allow_html=True)
