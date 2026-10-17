
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv(
    dotenv_path=Path(__file__).resolve().parent / ".env"
)

BASE_URL = "https://www.moltbook.com/api/v1"


def _headers() -> dict:
    """Return authenticated headers without exposing the key."""
    api_key = os.getenv("MOLTBOOK_API_KEY")

    if not api_key:
        raise RuntimeError(
            "MOLTBOOK_API_KEY is missing from .env."
        )

    return {"Authorization": f"Bearer {api_key}"}


def fetch_posts(limit: int = 5) -> list[dict]:
    """Fetch public posts without modifying anything."""
    if not 1 <= limit <= 10:
        raise ValueError("Limit must be between 1 and 10.")

    response = requests.get(
        f"{BASE_URL}/posts",
        params={"limit": limit, "sort": "new"},
        timeout=20,
    )
    response.raise_for_status()

    data = response.json()

    if isinstance(data, list):
        posts = data
    elif isinstance(data, dict):
        posts = data.get("posts", data.get("data", []))

        if isinstance(posts, dict):
            posts = posts.get("posts", [])
    else:
        raise ValueError("Unexpected Moltbook response.")

    if not isinstance(posts, list):
        raise ValueError("Moltbook posts field was not a list.")

    return [post for post in posts if isinstance(post, dict)]


def create_comment(post_id: str, content: str) -> dict:
    """Publish a comment when explicitly called."""
    if not post_id.strip():
        raise ValueError("Post ID cannot be empty.")

    content = content.strip()
    if not content or len(content) > 500:
        raise ValueError("Comment must be 1–500 characters.")

    response = requests.post(
        f"{BASE_URL}/posts/{post_id}/comments",
        headers=_headers(),
        json={"content": content},
        timeout=20,
    )
    response.raise_for_status()
    result = response.json()

    if result.get("verification") or result.get("verification_required"):
        print("Moltbook requires verification before publishing.")
        print("Check the response structure without sharing secrets.")
    elif result.get("success") is False:
        print("Moltbook rejected the submission.")

    return result

def create_post(
    title: str,
    content: str,
    submolt: str = "general",
) -> dict:
    """Publish an original text post when explicitly called."""
    title = title.strip()
    content = content.strip()
    submolt = submolt.strip()

    if not title or not content or not submolt:
        raise ValueError(
            "Title, content, and submolt are required."
        )

    if len(title) > 200 or len(content) > 10000:
        raise ValueError("Post exceeds configured size limits.")

    response = requests.post(
        f"{BASE_URL}/posts",
        headers=_headers(),
        json={
            "submolt": submolt,
            "title": title,
            "content": content,
        },
        timeout=20,
    )
    response.raise_for_status()
    return response.json()
