
Dynamic Pathfinding Agent with Real-Time Re-planning
This project implements an intelligent autonomous agent capable of navigating a grid-based environment using informed search strategies. The agent is designed to handle dynamic obstacles that appear while it is in motion, necessitating real-time path detection and immediate re-planning.

 Features
Dynamic Grid Customization: Users can define grid dimensions (Rows x Columns) and obstacle density at startup.

Informed Search Algorithms: * *A Search:** Uses f(n)=g(n)+h(n) for optimal pathfinding.

Greedy Best-First Search (GBFS): Focuses solely on the heuristic h(n) for faster, though potentially non-optimal, results.

Interactive Map Editor: Users can manually place or remove walls by clicking directly on the grid.

Dynamic Obstacle Spawning: New obstacles appear randomly while the agent is in transit to simulate real-world volatility.

Intelligent Re-planning: The agent automatically detects if a new obstacle blocks its current path and recalculates a new route from its current position.

Performance Metrics: Real-time dashboard showing Nodes Visited, Path Cost, and Execution Time in milliseconds.

Requirements
Python 3.x

Tkinter (Usually included with Python standard library)

Installation & Usage
Clone the Repository:

Bash
git clone https://github.com/your-username/dynamic-pathfinding-agent.git
cd dynamic-pathfinding-agent
Run the Application:

Bash
python main.py
Setup the Environment:

Enter the desired number of Rows and Columns when prompted.

Set the Obstacle Density (e.g., 30 for 30% coverage).

(Optional) Click on cells to add or remove walls manually before starting.

Start Navigation:

Click the "Start Navigation" button to see the agent move.

 Visual Elements
Frontier Nodes (Yellow): Nodes currently in the priority queue.

Visited Nodes (Red): Nodes that have been explored/expanded.

Final Path (Green): The calculated optimal path to the goal.

Obstacles (Black): Non-traversable walls.

Algorithmic Logic
Admissibility & Consistency: The implementation uses Manhattan Distance as the default heuristic, ensuring that the search remains admissible (never overestimates the cost) and consistent for optimal A* performance.

Efficiency: Re-calculation is optimized to trigger only if a new obstacle specifically obstructs the agent's remaining path.

Author: Rameen Ahmad

Course: Artificial Intelligence - Assignment 2