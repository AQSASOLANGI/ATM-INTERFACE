import streamlit as st

# Initialize balance
if "balance" not in st.session_state:
    st.session_state.balance = 1000.0

st.title("🏧 ATM Management System")

st.write("### Select an option")

menu = st.selectbox(
    "ATM Menu",
    ["Check Balance", "Deposit", "Withdraw", "Exit"]
)

# Check Balance
if menu == "Check Balance":
    st.success(f"💰 Your Current Balance is: Rs. {st.session_state.balance:.2f}")

# Deposit
elif menu == "Deposit":
    amount = st.number_input("Enter amount to deposit", min_value=0.0, step=100.0)
    if st.button("Deposit"):
        if amount > 0:
            st.session_state.balance += amount
            st.success(f"✅ Rs. {amount:.2f} deposited successfully")
        else:
            st.error("❌ Invalid amount")

# Withdraw
elif menu == "Withdraw":
    amount = st.number_input("Enter amount to withdraw", min_value=0.0, step=100.0)
    if st.button("Withdraw"):
        if 0 < amount <= st.session_state.balance:
            st.session_state.balance -= amount
            st.success(f"✅ Rs. {amount:.2f} withdrawn successfully")
        else:
            st.error("❌ Insufficient balance")

# Exit
elif menu == "Exit":
    st.info("👋 Thank you for using ATM System")
    st.stop()
