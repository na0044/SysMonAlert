import unittest
from unittest.mock import patch, mock_open, call
import psutil
import time
from monitor import log_metrics, ALERT_CPU_THRESHOLD, ALERT_MEMORY_THRESHOLD, ALERT_DISK_THRESHOLD

class TestSystemMetrics(unittest.TestCase):
    
    @patch("builtins.open", new_callable=mock_open)
    @patch("psutil.cpu_percent")
    @patch("psutil.virtual_memory")
    @patch("psutil.disk_usage")
    @patch("psutil.net_io_counters")
    @patch("time.sleep", return_value=None)  # Prevent actual sleep
    def test_log_metrics(self, mock_sleep, mock_net_io, mock_disk_usage, mock_virtual_memory, mock_cpu_percent, mock_file):
        # Mock psutil responses
        mock_cpu_percent.return_value = 90  # Above CPU threshold
        mock_virtual_memory.return_value = type("vmem", (object,), {"percent": 91})()  # Above memory threshold
        mock_disk_usage.return_value = type("disk", (object,), {"percent": 92})()  # Above disk threshold
        mock_net_io.return_value = type("netio", (object,), {"bytes_sent": 1000, "bytes_recv": 2000})()
        
        # Mock time.strftime
        with patch("time.strftime", return_value="2025-01-17 12:00:00"):
            with self.assertRaises(StopIteration):  # Stop after one iteration
                log_metrics()
        
        # Check if correct log files were opened
        mock_file.assert_any_call("system_metrics.log", "a")
        mock_file.assert_any_call("alert_log.txt", "a")
        
        # Check if the correct alert log messages were written
        handle = mock_file()
        handle.write.assert_any_call(
            "2025-01-17 12:00:00 | Warning: CPU usage is at 90%\n"
        )
        handle.write.assert_any_call(
            "2025-01-17 12:00:00 | Warning: Memory usage is at 91%\n"
        )
        handle.write.assert_any_call(
            "2025-01-17 12:00:00 | Warning: Disk usage is at 92%\n"
        )

        # Check if system metrics were logged correctly
        handle.write.assert_any_call(
            "2025-01-17 12:00:00 | CPU: 90% | Memory: 91% | Disk: 92% | "
            "Sent: 1000 bytes | Received: 2000 bytes\n"
        )

if __name__ == "__main__":
    unittest.main()

