#!/bin/bash

# Ensure paths are writable
export CARGO_HOME=$HOME/.cargo
export RUSTUP_HOME=$HOME/.rustup
export PATH="$CARGO_HOME/bin:$PATH"

# Install stable toolchain (silently)
rustup install stable
rustup default stable

# Install Python dependencies
pip install -r requirements.txt
