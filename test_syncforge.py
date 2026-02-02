# test_syncforge.py
"""
Tests for SyncForge module.
"""

import unittest
from syncforge import SyncForge

class TestSyncForge(unittest.TestCase):
    """Test cases for SyncForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SyncForge()
        self.assertIsInstance(instance, SyncForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SyncForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
