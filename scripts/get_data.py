#  Copyright (c) Microsoft Corporation.
#  Licensed under the MIT License.

import fire
from qlib.tests.data import GetData
#the fire package helps us to transfer our code to generate command line interfaces

if __name__ == "__main__":
    fire.Fire(GetData)
