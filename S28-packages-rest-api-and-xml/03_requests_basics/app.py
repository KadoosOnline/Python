'''requests: talking to a web API.

    pip install -r requirements.txt

A REST API answers an HTTP request with data (almost always JSON).
The vocabulary:
    URL          which resource
    method       GET (read), POST (create), PUT (change), DELETE (remove)
    status code  200 = OK, 404 = not found, 500 = server error
    body         the data itself
'''

try:
    import requests
except ModuleNotFoundError:
    raise SystemExit('Run "pip install -r requirements.txt" first.')


def main() -> None:
    # 1. A simple GET, with a timeout so the program cannot hang for ever.
    try:
        response = requests.get('https://api.github.com', timeout=10)
        response.raise_for_status()      # raises when the status is 4xx or 5xx
    except requests.RequestException as e:
        print('The request failed:', e)
        return

    print('Status code:', response.status_code)      # 200 means success

    # 2. The answer parsed as JSON -> a Python dictionary.
    data = response.json()
    print('Example field user_url:', data['current_user_url'])

    # 3. Query parameters: requests builds the ?q=python&sort=stars part for us.
    params = {'q': 'python', 'sort': 'stars'}
    try:
        search = requests.get(
            'https://api.github.com/search/repositories',
            params=params,
            timeout=10,
        )
        search.raise_for_status()
    except requests.RequestException as e:
        print('The search failed:', e)
        return

    result = search.json()
    print('Number of search results:', result['total_count'])
    print('The final URL was:', search.url)

    print('\nTop 5 repositories:')
    for repo in result['items'][:5]:
        print(f"  {repo['full_name']:<40} {repo['stargazers_count']:>8} stars")

    # 4. The other pieces of the answer.
    print('\nContent type:', response.headers.get('Content-Type'))
    # response.text  -> the raw text
    # response.content -> the raw bytes (for an image or a PDF)


if __name__ == '__main__':
    main()
