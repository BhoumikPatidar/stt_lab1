#!/usr/bin/env bash
set -e

# Ensure perf works in container
sudo ln -sf $(find /usr/lib/linux-tools-* -type f -name perf | head -1) /usr/local/bin/perf || true

# Verify installations
perf --version
papi_avail

echo "Dev container is ready! You can now build your GEMM prototype."
