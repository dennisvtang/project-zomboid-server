import requests
import re


def scrape_mod_id(website_html: str) -> str | None:
    patterns = [
        r'Mod ID: (.*)(?=</div>)',
    ]

    for pattern in patterns:
        mod_id = re.search(pattern, website_html)

        if mod_id != None:
            break

    if mod_id is None:
        return None
    else:
        return mod_id.group(1)

def scrape_workshop_id(website_html: str) -> str | None:
    patterns = [
        r'Workshop ID: (\d{10})',
    ]

    for pattern in patterns:
        workshop_id = re.search(pattern, website_html)

        if workshop_id != None:
            break

    if workshop_id is None:
        return None
    else:
        return workshop_id.group(1)

def main() -> None:
    """Script entry point directly run.
    """
    website_html = requests.get('https://steamcommunity.com/sharedfiles/filedetails/?id=2790006091').text

    mod_id = scrape_mod_id(website_html)
    print(f'mod id: {mod_id}')
    workshop_id = scrape_workshop_id(website_html)
    print(f'workshop id: {workshop_id}')


if __name__ == '__main__':
    main()