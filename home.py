import streamlit as st
from urllib.parse import urlencode

def update_url(page_name):
    query_params = st.query_params
    query_params["workflow"] = page_name
    st.experimental_set_query_params(**query_params)

def login_screen():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username and password:  # Simple placeholder condition
            st.session_state.logged_in = True
            update_url("restaurant-details")
            st.experimental_rerun()
        else:
            st.error("Please enter both username and password.")

def logout_button():
    if st.button("Logout"):
        st.session_state.logged_in = False
        update_url("login")
        st.success("You have been logged out.")
        st.experimental_rerun()

def enter_restaurant_details():
    st.title("1. Enter Restaurant Details")
    logout_button()
    st.text_input("Restaurant ID", "")
    st.selectbox("Menu Language", ["English", "Spanish", "French"])
    st.selectbox("Menu Type", ["Lunch", "Dinner"])
    col1, col2 = st.columns(2)
    if col2.button("Next ➞"):
        update_url("upload-menu-pdf")
        st.experimental_rerun()

def upload_menu_pdf():
    st.title("2. Upload Menu PDF")
    logout_button()
    st.text_input("Menu ID", "")
    st.file_uploader("Upload Menu PDF", type=["pdf"])
    col1, col2 = st.columns(2)
    if col1.button("➞ Back"):
        update_url("restaurant-details")
        st.experimental_rerun()
    if col2.button("Next ➞"):
        update_url("slice-pdf-sections")
        st.experimental_rerun()

def slice_pdf_sections():
    st.title("3. Slice PDF into Sections")
    logout_button()
    st.write("PDF Preview (Image Placeholder)")
    st.text("Define menu sections by selecting slices")
    col1, col2 = st.columns(2)
    if col1.button("➞ Back"):
        update_url("upload-menu-pdf")
        st.experimental_rerun()
    if col2.button("Next ➞"):
        update_url("view-manage-menu")
        st.experimental_rerun()

def manage_menu():
    st.title("4. View and Manage Menu")
    logout_button()
    st.write("Manage menu items here (list placeholder)")
    col1, col2 = st.columns(2)
    if col1.button("➞ Back"):
        update_url("slice-pdf-sections")
        st.experimental_rerun()
    if col2.button("Next ➞"):
        update_url("save-finalize-menu")
        st.experimental_rerun()

def save_and_finalize():
    st.title("5. Save and Finalize Menu")
    logout_button()
    st.write("Finalize and submit the menu")
    col1, col2 = st.columns(2)
    if col1.button("➞ Back"):
        update_url("view-manage-menu")
        st.experimental_rerun()
    if col2.button("Submit ✓"):
        st.success("Menu submitted successfully!")
        update_url("restaurant-details")
        st.experimental_rerun()

def main():
    query_params = st.query_params
    page = query_params.get("workflow", "login")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if page == "login" or not st.session_state.logged_in:
        st.session_state.logged_in = False
        login_screen()
    elif st.session_state.logged_in:
        if page == "restaurant-details":
            enter_restaurant_details()
        elif page == "upload-menu-pdf":
            upload_menu_pdf()
        elif page == "slice-pdf-sections":
            slice_pdf_sections()
        elif page == "view-manage-menu":
            manage_menu()
        elif page == "save-finalize-menu":
            save_and_finalize()
    else:
        st.warning("You have been logged out. Please log in again.")
        update_url("login")
        st.experimental_rerun()

if __name__ == "__main__":
    main()
