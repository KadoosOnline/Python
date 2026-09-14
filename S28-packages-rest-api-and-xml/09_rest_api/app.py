'''Reading a real, paginated REST API (the WordPress API).

    pip install -r requirements.txt

An API rarely returns everything at once: it returns PAGES.
The loop below asks for one page after another until there is nothing left.
'''

import json

try:
    import requests
except ModuleNotFoundError:
    raise SystemExit('Run "pip install -r requirements.txt" first.')

SITE_URL = 'https://yaristone.ir'
PER_PAGE = 20
TIMEOUT = 15


def fetch_all_posts(endpoint: str) -> list[dict]:
    'Download every page of posts and return them in one list.'
    all_posts: list[dict] = []
    page = 1

    while True:
        try:
            response = requests.get(
                endpoint,
                params={'page': page, 'per_page': PER_PAGE},
                timeout=TIMEOUT,
            )
            response.raise_for_status()
        except requests.RequestException as e:
            print(f'Error fetching page {page}: {e}')
            break

        posts = response.json()
        if not posts:                 # an empty page means we are done
            break

        all_posts.extend(posts)

        # The API tells us how many pages exist, in a header.
        total_pages = int(response.headers.get('X-WP-TotalPages', 1))
        if page >= total_pages:
            break

        page += 1

    return all_posts


def save_post(endpoint: str, post_id: int) -> None:
    'Download one post and save it as a JSON file.'
    try:
        response = requests.get(f'{endpoint}/{post_id}', timeout=TIMEOUT)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f'Error fetching the post: {e}')
        return

    filename = f'{post_id}.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=2)

    print(f'Post saved to {filename}')


def main() -> None:
    posts_endpoint = f'{SITE_URL}/wp-json/wp/v2/posts'

    all_posts = fetch_all_posts(posts_endpoint)

    if not all_posts:
        print('No posts found.')
        return

    print(f'\n{len(all_posts)} posts found:')
    for post in all_posts:
        # The title is itself a small object: {'rendered': '...'}
        title = post['title']['rendered']
        print(f"ID: {post['id']} - {title}")

    answer = input('\nEnter a post ID to fetch (or Enter to quit): ').strip()
    if not answer:
        return

    try:
        post_id = int(answer)
    except ValueError:
        print('Invalid ID')
        return

    save_post(posts_endpoint, post_id)


if __name__ == '__main__':
    main()
