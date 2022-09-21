import unittest
import thing

class TestRootFinder(unittest.TestCase):
    
    def test_max_abs_error(self):
        """ Tests maximum absolute error 
        """
        
        given = [1.0, -2.0, 3.0]
        expected = 3.0
        got = thing.max_abs_error(given)
        self.assertAlmostEqual(expected, got, places=7,
                               msg='expected {:.8f} but got {:.8f}'.format(expected, got))
        
      
        
if __name__ == '__main__':
    
    unittest.main()