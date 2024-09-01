import unittest
import code_for_tests as code
import logging


logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log",
                    encoding='UTF-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            test_obj = code.Runner('some_runner', speed=-5)
            for i in range(10):
                test_obj.walk()
            self.assertEqual(test_obj.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            test_obj = code.Runner(10)
            for i in range(10):
                test_obj.run()
            self.assertEqual(test_obj.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        test_obj_1 = code.Runner('some_runner_1')
        test_obj_2 = code.Runner('some_runner_2')
        for i in range(10):
            test_obj_1.run()
            test_obj_2.walk()
        self.assertNotEqual(test_obj_1.distance, test_obj_2.distance)


if __name__ == '__main__':
    unittest.main()
