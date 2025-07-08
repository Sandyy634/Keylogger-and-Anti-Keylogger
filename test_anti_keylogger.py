import unittest
from unittest.mock import patch
import anti_keylogger_cli as detector  # ✅ make sure file is named exactly this


class TestAntiKeyloggerDetector(unittest.TestCase):

    def setUp(self):
        detector.log_entries = []
        detector.initial_processes = set()

    def test_log_function(self):
        msg = "Test log entry"
        detector.log(msg)
        self.assertTrue(any(msg in entry for entry in detector.log_entries))

    def test_get_process_snapshot_returns_set(self):
        result = detector.get_process_snapshot()
        self.assertIsInstance(result, set)
        for item in result:
            self.assertIsInstance(item, tuple)
            self.assertEqual(len(item), 2)

    def test_detect_keylogger_process_detects_malicious(self):
        # Mock a suspicious process
        fake_snapshot = {
            (1234, "python keylogger_script.py")
        }
        detector.initial_processes = set()
        detector.get_process_snapshot = lambda: fake_snapshot
        detector.detect_keylogger_process()
        self.assertTrue(any("KEYLOGGER FILE STARTED" in log for log in detector.log_entries))

    def test_detect_keylogger_process_skips_safe(self):
        # Mock a safe process
        safe_snapshot = {
            (1234, "python harmless_script.py")
        }
        detector.initial_processes = set()
        detector.get_process_snapshot = lambda: safe_snapshot
        detector.detect_keylogger_process()
        self.assertEqual(len(detector.log_entries), 0)

    @patch("builtins.input", return_value="test_logs.txt")
    def test_export_logs(self, mock_input):
        detector.log_entries = ["[2025-07-07 10:00:00] Test entry"]
        with patch("builtins.open", unittest.mock.mock_open()) as mock_file:
            detector.export_logs()
            mock_file.assert_called_once_with("test_logs.txt", "w")
            mock_file().write.assert_called_once()

    def tearDown(self):
        detector.detecting = False


if __name__ == "__main__":
    print("Running Anti-Keylogger Tests...")
    unittest.main()
