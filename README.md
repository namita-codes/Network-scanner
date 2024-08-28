# Network-scanner
This Python script performs a port scan on a specified target IP address, identifying open ports. It employs multithreading to enhance scanning efficiency.

Purpose:

- This Python script performs a port scan on a specified target IP address, identifying open ports.
- It employs multithreading to enhance scanning efficiency.

Key Components:

- `NUM_THREADS`: A constant defining the number of worker threads to be used.
- `queue`:A thread-safe queue to distribute port numbers among the threads.
- `open_ports`: A list to store the discovered open ports.
- `scan_port(ip, port)`: A function that attempts to connect to the target IP address on the given port. If successful, it indicates that the port is open.
- `threader()`:A thread function that continuously takes ports from the queue, scans them, and marks the task as completed.
- `print_lock`: A lock to ensure thread-safe printing.

Workflow:

1. The user enters the target IP address.
2. The script resolves the hostname to an IP address.
3. A pool of `NUM_THREADS` worker threads is created.
4. Port numbers from 1 to 65535 are added to the queue.
5. Worker threads take port numbers from the queue and scan them.
6. Open ports are discovered and added to the `open_ports` list.
7. When all ports have been scanned, the threads are terminated.
8. The script prints the open ports or indicates that no open ports were found.

Enhancements:

- **Increased Timeout:** The `scan_port` function's timeout is increased to 1.5 seconds to accommodate slower responses.
- **Thread Safety:** The `print_lock` ensures that multiple threads don't print simultaneously, preventing race conditions.
- **Error Handling:** The `scan_port` function includes a `try-except` block to handle potential exceptions during the connection attempt.

Additional Considerations:

- Port Ranges: You can customize the port range to scan specific ports or ranges.
- Network Restrictions: Be aware of network restrictions or firewalls that might interfere with the scanning process.
- Ethical Considerations: Use this tool responsibly and adhere to ethical guidelines when scanning networks that are not your own.
