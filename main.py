import sys

def read_requests(file_path):
    with open(file_path, 'r') as file:
        requests = [int(line.strip()) for line in file]
    return requests

def fcfs(initial_position, requests):
    total_movement = 0
    current_position = initial_position
    order_of_service = []

    for request in requests:
        total_movement += abs(request - current_position)
        order_of_service.append(request)
        current_position = request

    return order_of_service, total_movement

def scan(initial_position, requests, direction='up'):
    total_movement = 0
    current_position = initial_position
    order_of_service = []
    
    requests = sorted(requests)
    
    if direction == 'up':
        requests_up = [r for r in requests if r >= current_position]
        requests_down = [r for r in requests if r < current_position]
        
        order_of_service.extend(requests_up)
        order_of_service.extend(reversed(requests_down))
        
    else:
        requests_up = [r for r in requests if r > current_position]
        requests_down = [r for r in requests if r <= current_position]
        
        order_of_service.extend(reversed(requests_down))
        order_of_service.extend(requests_up)
    
    for request in order_of_service:
        total_movement += abs(request - current_position)
        current_position = request

    return order_of_service, total_movement

def cscan(initial_position, requests):
    total_movement = 0
    current_position = initial_position
    order_of_service = []

    requests = sorted(requests)
    
    requests_up = [r for r in requests if r >= current_position]
    requests_down = [r for r in requests if r < current_position]
    
    order_of_service.extend(requests_up)
    order_of_service.extend(requests_down)
    
    for request in order_of_service:
        total_movement += abs(request - current_position)
        current_position = request

    return order_of_service, total_movement

def main():
    if len(sys.argv) != 3:
        print("Usage: python disk_scheduling.py <initial_position> <file_path>")
        return
    
    initial_position = int(sys.argv[1])
    file_path = sys.argv[2]
    
    requests = read_requests(file_path)
    
    # FCFS
    fcfs_order, fcfs_movement = fcfs(initial_position, requests)
    print("FCFS Order of Service:", fcfs_order)
    print("FCFS Total Head Movement:", fcfs_movement)
    
    # SCAN (assuming upward direction)
    scan_order, scan_movement = scan(initial_position, requests, direction='up')
    print("SCAN Order of Service (up):", scan_order)
    print("SCAN Total Head Movement (up):", scan_movement)
    
    # C-SCAN
    cscan_order, cscan_movement = cscan(initial_position, requests)
    print("C-SCAN Order of Service:", cscan_order)
    print("C-SCAN Total Head Movement:", cscan_movement)

if __name__ == "__main__":
    main()