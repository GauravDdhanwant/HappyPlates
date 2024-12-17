import streamlit as st

def update_url(**kwargs):
    """Update query parameters dynamically."""
    query_params = st.query_params
    query_params.clear()
    for key, value in kwargs.items():
        query_params[key] = value

def login_screen():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        update_url(workflow="restaurant-details")
        st.rerun()

def enter_restaurant_details():
    st.title("1. Enter Restaurant Details")
    restaurant_id = st.text_input("Restaurant ID", "")
    menu_language = st.selectbox("Menu Language", ["English", "Spanish", "French"])
    menu_type = st.selectbox("Menu Type", ["Lunch", "Dinner"])
    if st.button("Next ➞"):
        update_url(workflow="upload-menu-pdf", restaurant_id=restaurant_id, menu_language=menu_language, menu_type=menu_type)
        st.rerun()

def upload_menu_pdf():
    st.title("2. Upload Menu PDF")
    restaurant_id = st.query_params.get("restaurant_id", "")
    st.write(f"Restaurant ID: {restaurant_id}")
    menu_id = st.text_input("Menu ID", "")
    if st.button("Next ➞"):
        update_url(workflow="slice-pdf-sections", restaurant_id=restaurant_id, menu_id=menu_id)
        st.rerun()

def slice_pdf_sections():
    st.title("3. Slice PDF into Sections")
    restaurant_id = st.query_params.get("restaurant_id", "")
    menu_id = st.query_params.get("menu_id", "")
    st.write(f"Restaurant ID: {restaurant_id}, Menu ID: {menu_id}")
    slice_id = st.text_input("Slice ID", "")
    if st.button("Next ➞"):
        update_url(workflow="view-manage-menu", restaurant_id=restaurant_id, menu_id=menu_id, slice_id=slice_id)
        st.rerun()

def manage_menu():
    st.title("4. View and Manage Menu")
    restaurant_id = st.query_params.get("restaurant_id", "")
    menu_id = st.query_params.get("menu_id", "")
    slice_id = st.query_params.get("slice_id", "")
    st.write(f"Restaurant ID: {restaurant_id}, Menu ID: {menu_id}, Slice ID: {slice_id}")
    if st.button("Next ➞"):
        update_url(workflow="save-finalize-menu", restaurant_id=restaurant_id, menu_id=menu_id, slice_id=slice_id)
        st.rerun()

def save_and_finalize():
    st.title("5. Save and Finalize Menu")
    restaurant_id = st.query_params.get("restaurant_id", "")
    menu_id = st.query_params.get("menu_id", "")
    slice_id = st.query_params.get("slice_id", "")
    st.write(f"Restaurant ID: {restaurant_id}, Menu ID: {menu_id}, Slice ID: {slice_id}")
    if st.button("Submit ✓"):
        st.success("Menu submitted successfully!")
        update_url(workflow="restaurant-details")
        st.rerun()

def main():
    # Initialize session state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    
    # Extract query parameters
    query_params = st.query_params
    page = query_params.get("workflow", "login")

    # Control navigation
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
