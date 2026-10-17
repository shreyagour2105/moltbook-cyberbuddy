
import re

ALLOWED_TOPICS = {
    "cybersecurity",
    "cyber security",
    "network security",
    "application security",
    "information security",
    "vulnerability",
    "secure coding",
    "cryptography",
    "hashing",
    "sha-256",
    "sha256",
    "file integrity",
    "ai security",
    "artificial intelligence",
    "ai safety",
    "agent security",
    "prompt injection",
    "jailbreak",
    "guardrail",
    "tool call",
    "tool permission",
    "agent permission",
    "unsigned skills",
    "instruction injection",
    "authentication",
    "authorization",
    "access control",
    "credential",
    "api key",
    "permission",
    "privilege",
    "security boundary",
    "trust boundary",
    "python",
    "programming",
    "software engineering",
    "secure software",
    "api security",
    "dependency security",
    "browser security",
    "audit log",
    "rollback",
    "failed tool call",
    "data integrity",
}

MAX_COMMENT_LENGTH = 500


def is_relevant(text: str) -> bool:
    """Check whether a post matches Feheart's interests."""
    text = text.casefold()
    return any(topic in text for topic in ALLOWED_TOPICS)


def validate_comment(comment: str) -> bool:
    """Reject empty, oversized, link-containing, or very short drafts."""
    comment = comment.strip()

    if not comment or len(comment) > MAX_COMMENT_LENGTH:
        return False

    if re.search(r"https?://|www\.", comment, re.IGNORECASE):
        return False

    if len(comment.split()) < 8:
        return False

    return True
