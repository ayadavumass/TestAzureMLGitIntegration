# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import os
import sys
import argparse
import time
# from azureml.core.run import Run

print("Driver arguments = " + repr(sys.argv))

# This should succeed, because the docs folder in the project is ignored.
os.mkdir("docs")

# Ensure that Vienna's post-run code in this process doesn't rely on the cwd.
os.chdir("docs")

parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",
                    type=int)
args = parser.parse_args()
print("== Execution Output ==")
print("Square of {0} is {1}".format(sys.argv[-1],args.square**2))

num_metrics = 1
# run = Run.get_context()
count = 0
while count < num_metrics:
    count = count + 1
    print("Logging Accuracy{}".format(count))
    print("Logging Accuracy{}".format(count))
    count2 = 0
    while count2 < 100:
        # run.log('Accuracy{}'.format(count), (count + count2))
        count2 = count2 + 1

    # time.sleep(1)

# print("RunDto Before {0}".format(run._client.get_run()))
# create_run_dto = CreateRunDto(primary_metric_name="Accuracy1")
# run._client.patch_run(create_run_dto)
# print("RunDto After {0}".format(run._client.get_run()))

# run.complete()

print("curr dir {}".format(os.getcwd()))
