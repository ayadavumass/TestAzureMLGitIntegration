# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import time

for x in range(5 * 60):
    print("Hello, world!", flush=True)
    time.sleep(1)

# Don't actually run forever in case a process leaks by accident.
print("Okay, so it's not really infinite.")
