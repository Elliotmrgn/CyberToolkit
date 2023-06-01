import requests
from urllib.parse import urljoin, urlsplit, urlunsplit
from urllib.robotparser import RobotFileParser




def getDenies(url="www.google.com"):  
    
    # Check if the url has a scheme
    parsed_url = urlsplit(url)
    if not parsed_url.scheme:
        url = "http://" + url
    # Construct the URL for the robots.txt file
    robots_url = urljoin(url, '/robots.txt')
    # Send a GET request to retrieve the robots.txt file
    response = requests.get(robots_url)

    if response.status_code == 200:
        # Parsing the robots.txt file
        robot = RobotFileParser()
        robot.set_url(robots_url)
        robot.read()
        
        paths = []
        for entry in robot.entries:
            for line in entry.rulelines:
                not line.allowance and paths.append(line.path)

        # Return the result
        print("**************")
        print(set(paths))
        print("**************")
        return paths
    elif response.status_code == 404:
        return f"The robots.txt file does not exist for {url}"
    else:
        return f"Failed to retrieve the robots.txt file for {url}. Error code: {response.status_code}"
