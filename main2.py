import sys

def read_requests(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

def fcfs(start, requests):
    head = start
    total_movement = 0
    for request in requests:
        total_movement += abs(head - request)
        head = request
    return total_movement, requests

def scan(start, requests, num_cylinders):
    head = start
    total_movement = 0
    direction = -1  # assuming the initial direction is towards the innermost cylinder

    requests.sort()
    left = [r for r in requests if r <= head]
    right = [r for r in requests if r > head]

    if direction == -1:
        ordered_requests = left[::-1] + right
    else:
        ordered_requests = right + left[::-1]

    for request in ordered_requests:
        total_movement += abs(head - request)
        head = request

    return total_movement, ordered_requests

def c_scan(start, requests, num_cylinders):
    head = start
    total_movement = 0

    requests.sort()
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    ordered_requests = right + left

    for request in ordered_requests:
        total_movement += abs(head - request)
        head = request

    return total_movement, ordered_requests

def main():
    if len(sys.argv) != 4:
        print("Usage: python disk_scheduler.py <algorithm> <start> <filename>")
        sys.exit(1)

    algorithm = sys.argv[1].lower()
    start = int(sys.argv[2])
    filename = sys.argv[3]

    requests = read_requests(filename)
    num_cylinders = 5000  # as specified in the problem

    if algorithm == "fcfs":
        total_movement, order = fcfs(start, requests)
    elif algorithm == "scan":
        total_movement, order = scan(start, requests, num_cylinders)
    elif algorithm == "c-scan":
        total_movement, order = c_scan(start, requests, num_cylinders)
    else:
        print("Invalid algorithm specified. Use 'fcfs', 'scan', or 'c-scan'.")
        sys.exit(1)

    print(f"Algorithm: {algorithm.upper()}")
    print(f"Total head movement: {total_movement} cylinders")
    print("Order of service:", order)

if __name__ == "__main__":
    main()