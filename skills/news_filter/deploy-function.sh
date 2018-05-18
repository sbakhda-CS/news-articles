#!/usr/bin/env bash
set -e
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Run the build for all routes
# Building zips __main__.py and requirements.txt
${SCRIPT_DIR}/build-function.sh

# Deploy our functions to Cortex setting the code to their respective zips
cortex actions deploy nf/news_filter --code "${SCRIPT_DIR}/build/function.zip" --kind python:3