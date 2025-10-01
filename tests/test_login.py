from pages.login_page import LoginPage

# Test login with valid credentials (Standard user)
def test_valid_login(driver):

    # Load page
    login_page = LoginPage(driver)
    login_page.load_page()

    # Login
    login_page.login("standard_user","secret_sauce")

    # Confirm redirect
    assert "inventory.html" in driver.current_url, "❌ TC001 Failed:Did not redirect. Redirect to inventory page expected"


# Test login with Invalid credentials (Standard user)
def test_invalid_login(driver):

    # Load page
    login_page = LoginPage(driver)
    login_page.load_page()

    # Login
    login_page.login("standard_user","secret_saucee")

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

# Test login with valid credentials (Locked out user)
def test_locked_user_valid_login(driver):

    # Load page
    login_page = LoginPage(driver)
    login_page.load_page()

    # Login
    login_page.login("locked_out_user","secret_sauce")

    # Confirm no redirect
    assert "index.html" in driver.current_url, "❌ TC004 Failed:Should not redirect. Redirect to inventory page unexpected"

    # Confirm if error message got displayed
        # Get err msg
    err_message = login_page.get_text("//h3[@data-test='error']")
    assert "this user has been locked out" in err_message, "❌ TC004 Failed: Unexpected error message. Got:{unexpected_message}".format(unexpected_message = err_message)


# Test login with Invalid credentials (Locked out user)
def test_locked_user_invalid_login(driver):

    # Load page
    login_page = LoginPage(driver)
    login_page.load_page()

    # Login
    login_page.login("locked_out_user","secret_saucee")

    # Confirm if user didnt get redirected
    assert "index.html" in driver.current_url, "❌ TC005 Failed: Did not stay on the login page."

    # Confirm if error message got displayed
        # Get err msg
    err_message = login_page.get_text("//h3[@data-test='error']")
    assert "Username and password do not match any user in this service" in err_message, "❌ TC005 Failed: Unexpected error message. Got:{unexpected_message}".format(unexpected_message = err_message)


# Test login with empty password (Locked out user)
def test_locked_user_login_no_password(driver):

    # Load page
    login_page = LoginPage(driver)
    login_page.load_page()

    # Login
    login_page.login("locked_out_user","")

    # Confirm if user didnt get redirected
    assert "index.html" in driver.current_url, "❌ TC006 Failed: Did not stay on the login page."

    # Confirm if error message got displayed
        # Get err msg
    err_message = login_page.get_text("//h3[@data-test='error']")
    assert "Password is required" in err_message, "❌ TC006 Failed: Unexpected error message. Got:{unexpected_message}".format(unexpected_message = err_message)

# Test login with valid credentials (Problem user)
def test_problem_user_valid_login(driver):

    # Load page
    login_page = LoginPage(driver)
    login_page.load_page()

    # Login
    login_page.login("problem_user","secret_sauce")

    # Confirm redirect
    assert "inventory.html" in driver.current_url, "❌ TC007 Failed:Did not redirect. Redirect to inventory page expected"


# Test login with Invalid credentials (Problem user)
def test_problem_user_invalid_login(driver):

    # Load page
    login_page = LoginPage(driver)
    login_page.load_page()

    # Login
    login_page.login("problem_user","secret_saucee")

    # Confirm if user didnt get redirected
    assert "index.html" in driver.current_url, "❌ TC008 Failed: Did not stay on the login page."

    # Confirm if error message got displayed
        # Get err msg
    err_message = login_page.get_text("//h3[@data-test='error']")
    assert "Username and password do not match any user in this service" in err_message, "❌ TC008 Failed: Unexpected error message. Got:{unexpected_message}".format(unexpected_message = err_message)


# Test login with empty password (Problem user)
def test_problem_user_login_no_password(driver):

    # Load page
    login_page = LoginPage(driver)
    login_page.load_page()

    # Login
    login_page.login("problem_user","")

    # Confirm if user didnt get redirected
    assert "index.html" in driver.current_url, "❌ TC009 Failed: Did not stay on the login page."

    # Confirm if error message got displayed
        # Get err msg
    err_message = login_page.get_text("//h3[@data-test='error']")
    assert "Password is required" in err_message, "❌ TC009 Failed: Unexpected error message. Got:{unexpected_message}".format(unexpected_message = err_message)


# Test login with valid credentials (Performance glitch user)
def test_performance_glitch_user_valid_login(driver):

    # Load page
    login_page = LoginPage(driver)
    login_page.load_page()

    # Login
    login_page.login("performance_glitch_user","secret_sauce")

    # Confirm redirect
    assert "inventory.html" in driver.current_url, "❌ TC010 Failed:Did not redirect. Redirect to inventory page expected"


# Test login with Invalid credentials (Performance glitch user)
def test_performance_glitch_user_invalid_login(driver):

    # Load page
    login_page = LoginPage(driver)
    login_page.load_page()

    # Login
    login_page.login("performance_glitch_user","secret_sauce1")

    # Confirm if user didnt get redirected
    assert "index.html" in driver.current_url, "❌ TC011 Failed: Did not stay on the login page."

    # Confirm if error message got displayed
        # Get err msg
    err_message = login_page.get_text("//h3[@data-test='error']")
    assert "Username and password do not match any user in this service" in err_message, "❌ TC011 Failed: Unexpected error message. Got:{unexpected_message}".format(unexpected_message = err_message)


# Test login with empty password (Performance glitch user)
def test_performance_glitch_user_login_no_password(driver):

    # Load page
    login_page = LoginPage(driver)
    login_page.load_page()

    # Login
    login_page.login("performance_glitch_user","")

    # Confirm if user didnt get redirected
    assert "index.html" in driver.current_url, "❌ TC012 Failed: Did not stay on the login page."

    # Confirm if error message got displayed
        # Get err msg
    err_message = login_page.get_text("//h3[@data-test='error']")
    assert "Password is required" in err_message, "❌ TC009 Failed: Unexpected error message. Got:{unexpected_message}".format(unexpected_message = err_message)
