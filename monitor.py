import psutil
import time

# Configuration
ALERT_CPU_THRESHOLD = 85  # Percentage
ALERT_MEMORY_THRESHOLD = 90  # Percentage
ALERT_DISK_THRESHOLD = 90  # Percentage
LOG_FILE = "system_metrics.log"
ALERT_LOG_FILE = "alert_log.txt"

# Function to log system metrics
def log_metrics():
    with open(LOG_FILE, "a") as log, open(ALERT_LOG_FILE, "a") as alert_log:
        while True:
            # CPU usage
            cpu_usage = psutil.cpu_percent(interval=1)
            # Memory usage
            memory = psutil.virtual_memory()
            memory_usage = memory.percent
            # Disk usage
            disk = psutil.disk_usage('/')
            disk_usage = disk.percent
            # Network activity
            net_io = psutil.net_io_counters()
            sent = net_io.bytes_sent
            received = net_io.bytes_recv

            # Log metrics
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            log_entry = (
                f"{timestamp} | CPU: {cpu_usage}% | Memory: {memory_usage}% | "
                f"Disk: {disk_usage}% | Sent: {sent} bytes | Received: {received} bytes\n"
            )
            log.write(log_entry)
            log.flush()

            # Check for alerts
            if cpu_usage > ALERT_CPU_THRESHOLD:
                alert_message = f"{timestamp} | Warning: CPU usage is at {cpu_usage}%\n"
                alert_log.write(alert_message)
                alert_log.flush()
            if memory_usage > ALERT_MEMORY_THRESHOLD:
                alert_message = f"{timestamp} | Warning: Memory usage is at {memory_usage}%\n"
                alert_log.write(alert_message)
                alert_log.flush()
            if disk_usage > ALERT_DISK_THRESHOLD:
                alert_message = f"{timestamp} | Warning: Disk usage is at {disk_usage}%\n"
                alert_log.write(alert_message)
                alert_log.flush()

            time.sleep(60)  # Log every 60 seconds

if __name__ == "__main__":
    print("Starting system metrics monitoring...")
    try:
        log_metrics()
    except KeyboardInterrupt:
        print("Monitoring stopped.")