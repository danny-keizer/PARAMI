#!/bin/bash

curl -LsSf https://astral.sh/uv/install.sh | sh
git clone https://github.com/danny-keizer/Parami.git && cd Parami
uv tool install .