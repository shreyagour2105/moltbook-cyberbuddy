
from safety import is_relevant, validate_comment


def test_relevant_post():
    assert is_relevant(
        "I am learning Python for cybersecurity"
    )


def test_irrelevant_post():
    assert not is_relevant(
        "My favourite recipe for chocolate cake"
    )


def test_valid_comment():
    assert validate_comment(
        "Python is useful for building practical "
        "cybersecurity tools and automating analysis."
    )


def test_short_comment():
    assert not validate_comment("Nice post")


def test_comment_with_link():
    assert not validate_comment(
        "This is a useful discussion about Python security "
        "tools and analysis https://example.com"
    )


def test_empty_comment():
    assert not validate_comment("")

def test_rejects_empty_whitespace_comment():
    assert not validate_comment("        ")


def test_rejects_oversized_comment():
    assert not validate_comment("security " * 100)


def test_rejects_markdown_link():
    comment = (
        "This security review is useful, but see "
        "[this reference](https://example.com) for details."
    )
    assert not validate_comment(comment)


def test_rejects_comment_with_www_link():
    comment = (
        "This security review is useful, but visit "
        "www.example.com for more technical details."
    )
    assert not validate_comment(comment)


def test_rejects_irrelevant_post():
    assert not is_relevant(
        "My favourite recipes for homemade chocolate cake"
    )

