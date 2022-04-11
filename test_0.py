from main import create_dict, generate_text


def dummy_callable(input):
    return 0


def test_create_dict_basic():
    original = "I wish I may I wish I might"
    result = create_dict(original)
    assert result == {
        ("I", "wish"): ["I", "I"],
        ("wish", "I"): ["may", "might"],
        ("I", "wish"): ["I", "I"],
        ("may", "I"): ["wish"],
        ("I", "may"): ["I"],
    }


def test_create_text():
    language_dict = {
        ("I", "wish"): ["I", "I"],
        ("wish", "I"): ["may", "might"],
        ("I", "wish"): ["I", "I"],
        ("may", "I"): ["wish"],
        ("I", "may"): ["I"],
    }
    result = generate_text(language_dict, dummy_callable, 6, seed=("I", "may"))
    assert result == "I may I wish I may"


def test_create_invalid_stops():
    """Should stop if can't find next step."""
    language_dict = {("I", "wish"): ["not_in_this_text"]}
    result = generate_text(language_dict, dummy_callable, 6, seed=("I", "wish"))
    assert result == "I wish not_in_this_text"
