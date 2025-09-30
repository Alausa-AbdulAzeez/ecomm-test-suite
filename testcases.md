# Test Cases

## Login Page



| **ID** | **Title**                                    | **Pre-Condition**          | **Steps**                                                         | **Expected Result**                                       | **Status** |
| ------ | -------------------------------------------- | -------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------- | ---------- |
| TC001  | Standard user - valid login                  | User is on login page      | Enter `standard_user` + `secret_sauce` → Click Login              | Redirected to inventory page                              | Passed    |
| TC002  | Standard user - incorrect password           | User is on login page      | Enter `standard_user` + wrong password → Click Login              | Do not redirect home and display an error message                                   | Not Run    |
| TC003  | Standard user - empty password               | User is on login page      | Enter `standard_user` + empty password → Click Login              | Do not redirect home and display an error message                                   | Not Run    |
| TC004  | Locked out user - valid login                | User is on login page      | Enter `locked_out_user` + `secret_sauce` → Click Login            | Error message: *"Sorry, this user has been locked out."*  | Not Run    |
| TC005  | Locked out user - incorrect password         | User is on login page      | Enter `locked_out_user` + wrong password → Click Login            | Do not redirect home and display an error message                                   | Not Run    |
| TC006  | Locked out user - empty password             | User is on login page      | Enter `locked_out_user` + empty password → Click Login            | Do not redirect home and display an error message                                   | Not Run    |
| TC007  | Problem user - valid login                   | User is on login page      | Enter `problem_user` + `secret_sauce` → Click Login               | Redirected to inventory page | Not Run    |
| TC008  | Problem user - incorrect password            | User is on login page      | Enter `problem_user` + wrong password → Click Login               | Do not redirect home and display an error message                                   | Not Run    |
| TC009  | Problem user - empty password                | User is on login page      | Enter `problem_user` + empty password → Click Login               | Do not redirect home and display an error message                                   | Not Run    |
| TC010  | Performance glitch user - valid login        | User is on login page      | Enter `performance_glitch_user` + `secret_sauce` → Click Login    | Redirected to inventory page, slower load time            | Not Run    |
| TC011  | Performance glitch user - incorrect password | User is on login page      | Enter `performance_glitch_user` + wrong password → Click Login    | Do not redirect home and display an error message                                   | Not Run    |
| TC012  | Performance glitch user - empty password     | User is on login page      | Enter `performance_glitch_user` + empty password → Click Login    | Do not redirect home and display an error message                                   | Not Run    |
| TC013  | Empty username and password                  | User is on login page      | Leave both fields blank → Click Login                             | Do not redirect home and display an error message / login button disabled           | Not Run    |
| TC014  | Dismiss error message                        | Error message is displayed | Click the close (X) button on the error message                   | Error message disappears from screen                      | Not Run    |
| TC015  | Username with only whitespace                | User is on login page      | Enter spaces as username + valid password → Click Login           | Do not redirect home and display an error message                                   | Not Run    |
| TC016  | Case sensitivity check                       | User is on login page      | Enter `Standard_User` (wrong case) + `secret_sauce` → Click Login | Do not redirect home and display an error message                                   | Not Run    |

---

## Inventory Page
| **ID** | **Title**                   | **Pre-Condition**          | **Steps**                                           | **Expected Result**             | **Status** |
| ------ | --------------------------- | -------------------------- | --------------------------------------------------- | ------------------------------- | ---------- |
| TC101  | Hamburger menu - visible    | Logged in as standard user | Verify hamburger icon is visible                    | Hamburger icon is present       | Not Run    |
| TC102  | Hamburger menu - open/close | Logged in as standard user | Click hamburger → verify close button → click close | Menu opens and closes correctly | Not Run    |
| TC103  | Cart icon - navigation      | Logged in as standard user | Click cart icon                                     | Redirected to cart page         | Not Run    |
| TC104  | Sidebar nav links - Visibility and Navigation      | Logged in as standard user | Click hamburger icon <br> Click Individual links to test                                  | Redirected to their respective pages         | Not Run    |
| TC105  | Logo - visibility      | Logged in as standard user | Verify hamburger icon is visible                                  | Logo is present         | Passed    |
| TC106  | Logo - Navigation     | Logged in as standard user | Click logo                                | Navigates back home from any page          | Failed    |
| TC107  | Filter - visibility      | Logged in as standard user | Verify filter is visible                                  | Filter dropdown is present         | Passed    |
| TC108  | Filter Options - visibility      | Logged in as standard user | Verify filter options are visible                                  | Filter options are present in dropdown         | Passed    |
| TC109  | Filter - Filtering (A - Z)     | Logged in as standard user | Click dropdown <br> Click "Name (A to Z)"                             | Items should appear alphabetically          | Passed    |
| TC110  | Filter - Filtering (Z - A)     | Logged in as standard user | Click dropdown <br> Click "Name (Z to A)"                             | Items should appear ordered from (Z to A)         | Passed    |
| TC111  | Filter - Filtering Price (low - high)     | Logged in as standard user | Click dropdown <br> Click "Price (low to high)"                             | Items should appear with prices ordered from lowest to highest         | Passed    |
| TC112  | Filter - Filtering Price (high - low)     | Logged in as standard user | Click dropdown <br> Click "Price (high to low)"                             | Items should appear with prices ordered from highest to lowest          | Passed    |
| TC113  | page title - Visibility     | Logged in as standard user                              | Verify page title is visible          | Page title is visible    | Passed
| TC114  | Product images - Visibility     | Logged in as standard user                              | Verify product images are visible          | Pproduct images are visible     |   Passed
| TC115  | All products present     | Logged in as standard user                              | Verify products are visible          | Products are visible    |    Passed
| TC116  | Product title present     | Logged in as standard user                              | Verify products titles are visible          | Products titles are visible    | Passed
| TC117  | Product desctiption present     | Logged in as standard user                              | Verify products descriptions are visible          |  Products descriptions are visible    | Passed
| TC118  | Product price present     | Logged in as standard user                              | Verify products prices are visible          | Verify products prices are visible      | Passed
| TC120  | Product CTA present     | Logged in as standard user                              | Verify products CTAs are visible          | Products CTAs are visible     |  Passed
| TC121  | Add to cart     | Logged in as standard user                              |   Click "Add to Cart" button       |  Cart badge should increase +1    | Passed
| TC122  | Remove from cart     | Logged in as standard user                              |   Click "Remove from Cart" button       |  Cart badge should increase -1    | Passed
| TC123  | Reset app     | Logged in as standard user                              |   1. Click the hamburger menu <br> 2. Click "Reset App State" option       |  Cart badge should disapper and previously selected product's CTA should return to "ADD TO CART"     | Failed
| TC124  | Product->Cart consistency (e2e)     | Logged in as standard user                              |   1. Add product   X in the inventory <br> 2. Open the cart 3. Confirm the cart shows product X       |  Product added from the inventory page and the product in the cart should be same     | Passed



