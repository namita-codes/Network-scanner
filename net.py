import socket
import threading
from queue import Queue

# Number of threads
NUM_THREADS = 100
queue = Queue()
open_ports = []

# Function to scan a port
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.5)  # Increased timeout to 1.5 seconds
        result = sock.connect_ex((ip, port))
        if result == 0:
            with print_lock:
                print(f"Port {port} is open")
                open_ports.append(port)
        sock.close()
    except Exception as e:
        print(f"Exception occurred: {e}")

# Thread function to get ports from the queue and scan them
def threader():
    while True:
        worker = queue.get()
        if worker is None:
            break
        scan_port(target, worker)
        queue.task_done()

# Print lock to ensure thread-safe printing
print_lock = threading.Lock()

# Main function
if __name__ == "__main__":
    target = input("Enter the target IP address: ")
    ip = socket.gethostbyname(target)
    print(f"Starting scan on {ip}")

    # Starting threads
    threads = []
    for _ in range(NUM_THREADS):
        thread = threading.Thread(target=threader)
        thread.daemon = True
        thread.start()
        threads.append(thread)

    # Adding ports to the queue
    for port in range(1, 65535):
        queue.put(port)

    # Wait for the queue to be empty
    queue.join()

    # Stop workers
    for _ in range(NUM_THREADS):
        queue.put(None)
    for thread in threads:
        thread.join()

    print("Scanning complete!")
    if open_ports:
        print(f"Open ports: {sorted(open_ports)}")
    else:
        print("No open ports found.")
