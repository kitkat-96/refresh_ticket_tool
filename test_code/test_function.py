import random
from pathlib import Path


def test_page (queue_url_weight, glasto_url_weight):
    # Use relative paths based on the current file location
    base_dir = Path(__file__).parent 

    glasto_url = (base_dir / "glasto_site.htm").as_uri()
    queue_url = (base_dir / "glasto_queue.htm").as_uri()

    site_options = [queue_url, glasto_url]
    page_choice = random.choices(site_options, weights=[queue_url_weight, glasto_url_weight])[0]
    
    return str(page_choice)
