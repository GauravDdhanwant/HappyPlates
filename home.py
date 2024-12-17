import streamlit as st

def login_screen():
    st.title("Login")
    st.text_input("Username")
    st.text_input("Password", type="password")
    st.markdown("[Login](?workflow=restaurant-details)")

def enter_restaurant_details():
    st.title("1. Enter Restaurant Details")
    st.text_input("Restaurant ID", "")
    st.selectbox("Menu Language", ["English", "Spanish", "French"])
    st.selectbox("Menu Type", ["Lunch", "Dinner"])
    st.markdown("[Next ➞](?workflow=upload-menu-pdf)")

def upload_menu_pdf():
    st.title("2. Upload Menu PDF")
    st.text_input("Menu ID", "")
    st.file_uploader("Upload Menu PDF", type=["pdf"])
    st.markdown("[➞ Back](?workflow=restaurant-details) | [Next ➞](?workflow=slice-pdf-sections)")

def slice_pdf_sections():
    st.title("3. Slice PDF into Sections")
    st.write("PDF Preview (Image Placeholder)")
    st.markdown("[➞ Back](?workflow=upload-menu-pdf) | [Next ➞](?workflow=view-manage-menu)")

def manage_menu():
    st.title("4. View and Manage Menu")
    st.write("Manage menu items here (list placeholder)")
    st.markdown("[➞ Back](?workflow=slice-pdf-sections) | [Next ➞](?workflow=save-finalize-menu)")

def save_and_finalize():
    st.title("5. Save and Finalize Menu")
    st.write("Finalize and submit the menu")
    st.markdown("[➞ Back](?workflow=view-manage-menu) | [Submit ✓](?workflow=restaurant-details)")

def main():
    query_params = st.query_params
    page = query_params.get("workflow", "login")

    if page == "login":
        login_screen()
    elif page == "restaurant-details":
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
        login_screen()

if __name__ == "__main__":
    main()
