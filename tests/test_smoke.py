import unittest
import os
import sys
import shutil

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils.config_loader import load_config
from data.synthetic import PipeSimulator

class TestPipeline(unittest.TestCase):
    def setUp(self):
        # Create a temp config or use default
        self.config = load_config("configs/config.example.yaml")
        # Override paths for testing
        self.config['paths']['simulated_pipes'] = "tests/temp_data/test_pipes.geojson"
        
    def test_synthetic_generation(self):
        """Test if pipe simulator creates file."""
        sim = PipeSimulator(self.config)
        sim.generate()
        self.assertTrue(os.path.exists(self.config['paths']['simulated_pipes']))
        
    def tearDown(self):
        # Cleanup
        if os.path.exists("tests/temp_data"):
            shutil.rmtree("tests/temp_data")

if __name__ == '__main__':
    unittest.main()
