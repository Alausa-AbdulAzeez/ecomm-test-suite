from pages.login_page import LoginPage

# Test login with valid credentials (Standard user)
def test_valid_login(driver):

    # Load page
    login_page = LoginPage(driver)
    login_page.load_page()

    # Login
    login_page.login("standard_user","secret_saucee")

    # Confirm redirect
    assert "inventory.html" in driver.current_url, "❌ TC001 Failed:Did not redirect. Redirect to inventory page expected"


# Test login with Invalid credentials (Standard user)
def test_invalid_login(driver):

    # Load page
    login_page = LoginPage(driver)
    login_page.load_page()

    # Login
    login_page.login("standard_user","secret_sauce")

    # Confirm if user didnt get redirected
    assert "index.html" in driver.current_url, "❌ TC002 Failed: Did not stay on the login page."

    # Confirm if error message got displayed
        # Get err msg
    err_message = login_page.get_text("//h3[@data-test='error']")
    assert "Username and password do not match any user in this service" in err_message, "❌ TC002 Failed: Unexpected error message. Got:{unexpected_message}".format(unexpected_message = err_message)


# Test login with empty password (Standard user)
def test_login_no_password(driver):

    # Load page
    login_page = LoginPage(driver)
    login_page.load_page()

    # Login
    login_page.login("standard_user","")

    # Confirm if user didnt get redirected
    assert "index.html" in driver.current_url, "❌ TC003 Failed: Did not stay on the login page."

    # Confirm if error message got displayed
        # Get err msg
    err_message = login_page.get_text("//h3[@data-test='error']")
    assert "Password is required" in err_message, "❌ TC003 Failed: Unexpected error message. Got:{unexpected_message}".format(unexpected_message = err_message)
