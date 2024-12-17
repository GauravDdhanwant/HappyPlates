import streamlit as st
from urllib.parse import urlencode

def update_url(page_name):
    st.query_params.clear()
    st.query_params["workflow"] = page_name

def login_screen():
    st.title("Login")
    st.text_input("Username")
    st.text_input("Password", type="password")
    if st.button("Login"):
        st.session_state.logged_in = True
        st.session_state.page = "restaurant-details"
        st.rerun()

def logout_button():
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "login"
        st.success("You have been logged out.")
        st.rerun()

def enter_restaurant_details():
    st.title("1. Enter Restaurant Details")
    logout_button()
    st.text_input("Restaurant ID", "")
    st.selectbox("Menu Language", ["English", "Spanish", "French"])
    st.selectbox("Menu Type", ["Lunch", "Dinner"])
    col1, col2 = st.columns(2)
    if col2.button("Next ➞"):
        st.session_state.page = "upload-menu-pdf"
        st.rerun()

def upload_menu_pdf():
    st.title("2. Upload Menu PDF")
    logout_button()
    st.text_input("Menu ID", "")
    st.file_uploader("Upload Menu PDF", type=["pdf"])
    col1, col2 = st.columns(2)
    if col1.button("➞ Back"):
        st.session_state.page = "restaurant-details"
        st.rerun()
    if col2.button("Next ➞"):
        st.session_state.page = "slice-pdf-sections"
        st.rerun()

def slice_pdf_sections():
    st.title("3. Slice PDF into Sections")
    logout_button()
    st.write("PDF Preview (Image Placeholder)")
    st.text("Define menu sections by selecting slices")
    col1, col2 = st.columns(2)
    if col1.button("➞ Back"):
        st.session_state.page = "upload-menu-pdf"
        st.rerun()
    if col2.button("Next ➞"):
        st.session_state.page = "view-manage-menu"
        st.rerun()

def manage_menu():
    st.title("4. View and Manage Menu")
    logout_button()
    st.write("Manage menu items here (list placeholder)")
    col1, col2 = st.columns(2)
    if col1.button("➞ Back"):
        st.session_state.page = "slice-pdf-sections"
        st.rerun()
    if col2.button("Next ➞"):
        st.session_state.page = "save-finalize-menu"
        st.rerun()

def save_and_finalize():
    st.title("5. Save and Finalize Menu")
    logout_button()
    st.write("Finalize and submit the menu")
    col1, col2 = st.columns(2)
    if col1.button("➞ Back"):
        st.session_state.page = "view-manage-menu"
        st.rerun()
    if col2.button("Submit ✓"):
        st.success("Menu submitted successfully!")
        st.session_state.page = "restaurant-details"
        st.rerun()

def main():
    if "page" not in st.session_state:
        st.session_state.page = "login"
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.page == "login" or not st.session_state.logged_in:
        st.session_state.logged_in = False
        login_screen()
    elif st.session_state.logged_in:
        if st.session_state.page == "restaurant-details":
            enter_restaurant_details()
        elif st.session_state.page == "upload-menu-pdf":
            upload_menu_pdf()
        elif st.session_state.page == "slice-pdf-sections":
            slice_pdf_sections()
        elif st.session_state.page == "view-manage-menu":
            manage_menu()
        elif st.session_state.page == "save-finalize-menu":
            save_and_finalize()
    else:
        st.warning("You have been logged out. Please log in again.")
        st.session_state.page = "login"
        st.rerun()

if __name__ == "__main__":
    main()
