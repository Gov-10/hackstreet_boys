#!/bin/bash

# Ensure paths are writable
export CARGO_HOME=$HOME/.cargo
export RUSTUP_HOME=$HOME/.rustup
export PATH="$CARGO_HOME/bin:$PATH"

# Install rustup if it's not already installed
if ! command -v rustup &> /dev/null
then
  echo "Installing rustup..."
  curl https://sh.rustup.rs -sSf | sh -s -- -y
  source $CARGO_HOME/env
fi

# Install stable Rust toolchain
rustup install stable
rustup default stable

# Confirm Cargo works (optional but useful for logs)
cargo --version
rustc --version

# Install Python dependencies
pip install -r requirements.txt
