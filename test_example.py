import os
from xml.dom.xmlbuilder import Options

import pytest
import asyncio
from browser_use.agent.service import Agent
from browser_use.agent.views import ActionResult
from browser_use.browser.browser import Browser, BrowserConfig
from langchain_google_genai import ChatGoogleGenerativeAI


@pytest.mark.asyncio
async def test_testsigma_login():
    """Test login to Testsigma application"""

    

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


    agent = Agent(task, llm, use_vision=True)
    history = await agent.run()
    test_result = history.final_result()

    # Add assertions based on what final_result() returns
    assert test_result is not None, "Test result should not be None"
    print("Test Successful...........")

