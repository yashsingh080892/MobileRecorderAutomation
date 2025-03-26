import os
from xml.dom.xmlbuilder import Options

import controller
import pytest
import asyncio
from browser_use.agent.service import Agent
from browser_use.agent.views import ActionResult
from browser_use.browser.browser import Browser, BrowserConfig
from langchain_google_genai import ChatGoogleGenerativeAI

class Controller:
    def action(self, description):
        def decorator(func):
            return func
        return decorator

class ActionResult:
    def __init__(self, extracted_content=None):
        self.extracted_content = extracted_content

# Define controller actions for steps 10 and 11

controller = Controller()



@controller.action('10. Click on record button')
async def click_record_button_and_wait(page, button_locator: str, wait_time: int) -> ActionResult:
    try:
        # Find the record button and click it
        record_button = await page.query_selector('//span[text()="Record"]')  # Use the appropriate locator
        if record_button:
            await record_button.click()
            print("Clicked the record button.")

        # Wait for the specified amount of time
        await page.wait_for_timeout(wait_time * 1000)  # Playwright expects milliseconds

        return ActionResult(extracted_content=f"Waited for {wait_time} seconds after clicking.")

    except Exception as e:
        print(f"Error occurred: {e}")
        return ActionResult(extracted_content="Failed to perform the action.")

@pytest.mark.asyncio
async def test_testsigma_login():
    """Test login to Testsigma application"""

    chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    user_data_dir = "/tmp/chrome-user-data-dir"
    extension_path='/Users/yashaswi.singh/Downloads/build-chrome_staging_7.9.1'
    extra_args = [
        f'--user-data-dir={user_data_dir}',  # Fresh user data directory
        f'--load-extension={extension_path}'
    ]

    browser = Browser(
        config=BrowserConfig(
            chrome_instance_path=chrome_path,
            extra_chromium_args=extra_args
        )
    )

    task = (

        '1. Open the URL "https://app.testsigma.com/ui/" in the Chrome browser'
        '2. Enter the username "sigma@qateam.com" in the username field'
        '3. Enter the password "Testsigma@123" in the password field'
        '4. Click on the "Sign In" or "Login" button to log into the Testsigma application'
        '5. Wait for 5 seconds for the page to load'
        '6. Go to url https://app.testsigma.com/ui/td/184/cases/filters/881'
        '7. Click on record button'
        '8. wait for 4 seconds'
        '9. Click on version dropdown and select Android 13 value in it'
        '10. Click on device dropdown and select samsung s23 ultra in it'
        '9. Click on record button again'
        '10. wait for 20 seconds'
        '11. click on add new step'

    )


    llm = ChatGoogleGenerativeAI(
        model='gemini-2.0-flash',
        api_key='AIzaSyAxidOVqiJoYMyGVJQ6TltE4BxnVl6cMqU'
    )


    agent = Agent(task, llm, use_vision=True,browser=browser)
    history = await agent.run()
    test_result = history.final_result()

    # Add assertions based on what final_result() returns
    assert test_result is not None, "Test result should not be None"
