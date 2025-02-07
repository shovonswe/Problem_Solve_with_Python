def calculate_waiting_time(process_ids, burst_times):
    # Create a list for storing waiting times
    wait_times = [0] * len(process_ids)

    # Loop to calculate waiting times
    for x in range(1, len(process_ids)):
        wait_times[x] = burst_times[x - 1] + wait_times[x - 1]
    
    return wait_times

def calculate_turnaround_time(process_ids, burst_times, wait_times):
    # Create a list for turnaround times
    turn_times = [0] * len(process_ids)

    # Loop to calculate turnaround times
    for y in range(len(process_ids)):
        turn_times[y] = burst_times[y] + wait_times[y]
    
    return turn_times

def calculate_avg_times(process_ids, burst_times):
    # Calculate wait times and turnaround times
    wait_times = calculate_waiting_time(process_ids, burst_times)
    turn_times = calculate_turnaround_time(process_ids, burst_times, wait_times)

    # Get the totals
    total_wait = sum(wait_times)
    total_turnaround = sum(turn_times)

    # Print out process details
    print("Process  Burst Time  Waiting Time  Turnaround Time")
    for z in range(len(process_ids)):
        print(f"{process_ids[z]}        {burst_times[z]}          {wait_times[z]}             {turn_times[z]}")

    # Calculate and display averages
    print(f"\nAverage waiting time: {total_wait / len(process_ids):.2f}")
    print(f"Average turnaround time: {total_turnaround / len(process_ids):.2f}")

def run_program():
    # Ask for number of processes
    count = int(input("How many processes do you want to enter? "))
    process_ids = [i + 1 for i in range(count)]

    # Get the burst time for each process
    burst_times = []
    for j in range(count):
        bt = int(input(f"Enter the burst time for process {j + 1}: "))
        burst_times.append(bt)

    # Call function to calculate average times
    calculate_avg_times(process_ids, burst_times)

# Start the program
run_program()
