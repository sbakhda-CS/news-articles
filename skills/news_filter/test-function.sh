#!/usr/bin/env bash
set -e
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# test the skills using test jsons
cortex actions invoke nf/news_filter --params-file "${SCRIPT_DIR}/test/test_top_filter.json"
cortex actions invoke nf/news_filter --params-file "${SCRIPT_DIR}/test/test_all_filter.json"
#cortex actions invoke nf/news_filter --params-file "${SCRIPT_DIR}/test/test_source_filter.json"