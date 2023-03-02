from playwright.sync_api import Page


def test_log_into_bank_account(page: Page) -> None:

  # Load the login page.
  page.goto("https://demo.applitools.com")

  # Verify the full login page loaded correctly.
  # eyes.check(Target.window().fully().with_name("Login page"))

  # Perform login.
  page.locator('id=username').fill('andy')
  page.locator('id=password').fill('i<3pandas')
  page.locator('id=log-in').click()

  # Verify the full main page loaded correctly.
  # This snapshot uses LAYOUT match level to avoid differences in closing time text.
  # eyes.check(Target.window().fully().with_name("Main page").layout())