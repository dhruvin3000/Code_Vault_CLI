"""Test script to verify system monitoring works"""
import time

print("Starting test script...")
print("This will run for 3 seconds to generate monitoring data")

# Simulate some work
for i in range(3):
    print(f"Working... {i+1}/3")
    # Do some computation
    result = sum(range(1000000))
    time.sleep(1)

print(f"Final result: {result}")
print("Test complete!")
