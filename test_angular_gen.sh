#!/bin/bash

# Set the feature name
FEATURE_NAME="patient"

# Create the component
healgen angular component $FEATURE_NAME

# Create the service
healgen angular service $FEATURE_NAME

# Create the module
healgen angular module $FEATURE_NAME

# Create the directive
healgen angular directive "highlight"

# Create the pipe
healgen angular pipe "filter"

# Create the guard
healgen angular guard "auth"

# Create the interceptor
healgen angular interceptor "auth"

echo "Feature $FEATURE_NAME for the medical system has been generated."
