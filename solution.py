# Power stations and their available energy
stations = {
    "A":10,
    "B":20,
    "C":15,
    "D":5
}
print(stations)

# Connection between power stations
network = {
    "A":["B", "C"],
    "B":["A", "D"],
    "C":["A", "D"],
    "D":["B", "C"]
}
print(network)

# Store failed power cables
failed_cables = [
    ("A", "B"),
    ("B", "D")
]

# Automatically remove failed cables
for station1, station2 in failed_cables:
    network[station1].remove(station2)
    network[station2].remove(station1)

print("Network after cable failure: ")
print(network)

# Breadth-First Search
from collections import deque

def bfs(network, start, target):
    queue = deque([start])
    visited = set()
    
    while queue:
        current = queue.popleft()
        
        if current == target:
            return True
        if current in visited:
            continue
        visited.add(current)
        
        for neighbor in network[current]:
            if neighbor not in visited:
                queue.append(neighbor)
    
    return False

# Find alternative power routes
def find_path(network, start, target):
    queue = deque([[start]])
    visited = set()
    
    while queue:
        path = queue.popleft()
        current = path[-1]
        if current == target:
            return path
        if current in visited:
            continue
        visited.add(current)

        for neighbor in network[current]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                queue.append(new_path)
    return None

# Check connectivity after cable failure
result = bfs(network, "A", "B")

print("Is station B reachable from A?", result)

#Detect isolated power stations
for station in network:
    if not bfs(network, "A", station):
        print("Isolated station: ", station)
        
# Generate cable failure report
print("\n---SMARTGRID FAILURE REPORT---")

for station1, station2 in failed_cables:
    print(f"Failed cable: {station1} - {station2}")
    
#Find an alternative power route
alternative_route = find_path(network, "A", "D")

print("\n---ALTERNATIVE ROUTE---")
if alternative_route:
    print("Route: ", "-> ".join(alternative_route))
else:
    print("No alternative route avaliable.")

print("Network after failures: ", network)

# Calculate total registered energy
total_energy = sum(stations.values())

print("\n--- ENERGY REPORT ---")
print("Total registered energy: ", total_energy)

#Calculate reachable energy
reachable_energy = 0

for station in stations:
    if bfs(network, "A", station):
        reachable_energy += stations[station]

print("Reachable energy: ", reachable_energy)

# Calculate unavailable energy percentage
unavailable_energy = total_energy - reachable_energy

if total_energy > 0:
    unavailable_percentage = (unavailable_energy / total_energy) *100
else:
    unavailable_percentage = 0
    
print("Unavailable energy: ", unavailable_energy)
print("Unavailable percentage: ", unavailable_percentage, "%")

# Analyze network status
print("\n--- Network status ---")

if unavailable_percentage == 0:
    print("Status: NORMAL")
    
elif unavailable_percentage <= 20:
    print("Status: WARNING")
    
else:
    print("Status: CRITICAL")
    
# Simulate cable restoration
def restore_cable(network, station1, station2):
    restore_network = {
        station : neighbors.copy()
        for station, neighbors in network.items()
    }
    
    restore_network[station1].append(station2)
    restore_network[station2].append(station1)
    
    return restore_network

# Test cable restoration
test_network = restore_cable(network, "A", "B")

result = bfs(test_network, "A", "B")

print("\n--- CABLE RESTORATION TEST ---")
print("Sattion B restored: ", result)

# Analize possible cable repairs
print("\n--- REPAIR ANALYSIS ---")

for stations1, station2 in failed_cables:
    test_network = restore_cable(network, station1, station2)
    
    restored = bfs(test_network, "A", "B")
    
    print(f"Repair {stations1}-{station2}: {restored}")
    
# Find the best cable repair
best_repair = None

for station1, station2 in failed_cables:
    test_network = restore_cable(network, stations1, station2)
    
    if bfs(test_network, "A", "B"):
        best_repair = (station1, station2)
        break
    
# Display repair recommendation
print("\n--- REPAIR RECOMMENDATION ---")

if best_repair:
    print(f"Recommended best_repair: {best_repair[0]}-{best_repair[1]}")
else:
    print("No single cable repair can restore the connection.")
    
# Find all reachable stations
def reachable_stations(network, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        station = queue.popleft()
        
        if station not in visited:
            visited.add(station)
            
            for neighbor in network[station]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited

# Calculate recovered energy
if best_repair:
    repaired_network = restore_cable(
        network, best_repair[0], best_repair[1]
    )
    reachable = reachable_stations(repaired_network, "A")
    
    recovered_energy = sum(
        stations[station] for station in reachable
    )
    print("\n---ENERGY RECOVERY ---")
    print(f"Avaliable energy after repair: {recovered_energy}")

recovery_percentage = (recovered_energy / total_energy) * 100
print(f"Energy recovered: {recovery_percentage:.1f}%")

initial_reachable = reachable_stations(network, "A")

initial_energy = sum(
    stations[station] for station in initial_reachable
)
energy_gained = recovered_energy - initial_energy

print(f"Energy restored by repair: {energy_gained} units")


def main():
    pass

if __name__ == "__main__":
    main()