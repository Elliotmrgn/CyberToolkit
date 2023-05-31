import requests
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser


def getDenies(url="www.google.com"):
    # Check if the URL has a trailing slash, and add it if missing
    if not url.endswith('/'):
        url += '/'

    # Construct the URL for the robots.txt file
    robots_url = urljoin(url, 'robots.txt')

    # Send a GET request to retrieve the robots.txt file
    response = requests.get(robots_url)
    print(response)

    if response.status_code == 200:
        # Parsing the robots.txt file
        robots_parser = RobotFileParser()
        robots_parser.parse(response.text)

        # Checking if a specific user agent is allowed or disallowed
        user_agent = '*'  # You can specify a different user agent if needed
        allowed = robots_parser.can_fetch(user_agent, url)

        # Return the result
        # result = f"The robots.txt file exists for {url} and is {'allowed' if allowed else 'disallowed'} for user agent {user_agent}"
        return response.text
    elif response.status_code == 404:
        return f"The robots.txt file does not exist for {url}"
    else:
        return f"Failed to retrieve the robots.txt file for {url}. Error code: {response.status_code}"
