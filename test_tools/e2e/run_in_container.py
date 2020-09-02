from end_to_end_tests import manager as test_manager

import time

manager = test_manager.EndToEndTestManager()

print("sleeping..")
time.sleep(60)
for test in manager.get_tests():
    t = test[1]()
    t.run_wrapper()
