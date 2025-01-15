# System Monitor Alert 
## Key Features 
         1. CPU Usage Monitoring: Logs the CPU usage percentage.
         2. Memory Usage Monitoring: Logs the memory usage percentage and checks thresholds.
         3. Logs the disk usage percentage and checks thresholds.
         4. Network Activity: Logs bytes sent and received.
         5. Alert System: Sends email alerts when thresholds are crossed.
         6. Log File: Writes metrics to a system_metrics.log file every minute.
## The log file will include entries like the following, recorded every 60 seconds
<pre>
<code>
2025-01-14 14:35:12 | CPU: 15% | Memory: 50% | Disk: 60% | Sent: 123456 bytes | Received: 654321 bytes
2025-01-14 14:36:12 | CPU: 20% | Memory: 52% | Disk: 61% | Sent: 125678 bytes | Received: 658901 bytes
</code>
</pre>

