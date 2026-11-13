import unittest
from solution import bfs

class TestSmartGrid(unittest.TestCase):
    
    def test_energy_calculation(self):
        stations = {
            "A": 10,
            "B": 20,
            "C": 15,
            "D": 5
        }
        total_energy = sum(stations.values())
        
        self.assertEqual(total_energy, 50)
        
    def test_network_connectivity(self):
        network = {
            "A": ["B", "C"],
            "B": ["A", "D"],
            "C": ["A", "D"],
            "D": ["B", "C"]
        }
        result = bfs(network, "A", "D")
        
        self.assertTrue(result)
        
    def test_disconnected_network(self):
        network = {
            "A": ["C"],
            "B": [],
            "C": ["A"],
            "D": []
        }
        result = bfs(network, "A", "D")
        
        self.assertFalse(result)