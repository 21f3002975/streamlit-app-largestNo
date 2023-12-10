import streamlit as st

def find_largest_number(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("Find the Largest Number among 3")

    # Input fields for three numbers
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    # Button to trigger the calculation
    if st.button("Find Largest"):
        largest_number = find_largest_number(num1, num2, num3)
        st.success(f"The largest number is: {largest_number}")

if __name__ == "__main__":
    main()
