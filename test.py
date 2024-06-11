import logging
import unittest

from standard_deviation import standard_deviation

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class SampleDeviationTest(unittest.TestCase):

    
    def test_sample_deviation(self):
        logger.info("Going to run tests for sample_deviations.")
        test_1 = standard_deviation(
            data=[3, 3, 5, 9],
        )
        test_2 = standard_deviation(
            data=[13, 24, 25, 29, 17]
        )
        test_3 = standard_deviation(
            data=[76, 84, 69, 92, 58,
            89, 73, 97, 85, 77],
        )

        self.assertEqual(round(test_1, 4),  2.8284)
        self.assertEqual(round(test_2, 4),  6.4653)
        self.assertEqual(round(test_3, 4), 11.7094)
        logger.info("Tests for sample_deviation completed successfully.")
        
    
    def test_population_deviation(self):
        logger.info("Going to run tests for population_deviation.")
        test_1 = standard_deviation(
            data=[-3, 3, -5, 9], 
            sample_deviation=True
        )
        test_2 = standard_deviation(
            data=[-144, 169, -225, 512, 1024], 
            sample_deviation=True
        )
        test_3 = standard_deviation(
            data=[1, 5, 200, -533, 1000, 
                2000, -1500, -2, -50, -350],
            sample_deviation=True
        )

        self.assertEqual(round(test_1, 4),  5.4772)
        self.assertEqual(round(test_2, 4),  459.0562)
        self.assertEqual(round(test_3, 4), 874.0523)
        
        logger.info("Tests for population_deviation completed successfully.")


if __name__ == '__main__':
    unittest.main()