from unittest.mock import mock_open, patch


def save_report(filename, content):
    with open(filename, "w") as file:
        file.write(content)


def test_save_report_uses_mock_file():
    fake_file = mock_open()

    with patch("builtins.open", fake_file):
        save_report("marks.txt", "Ali,80")

    fake_file.assert_called_once_with("marks.txt", "w")
    fake_file().write.assert_called_once_with("Ali,80")