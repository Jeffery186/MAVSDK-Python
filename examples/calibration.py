#!/usr/bin/env python3

import asyncio
import logging
from mavsdk import System

# Enable INFO level logging by default so that INFO messages are shown
logging.basicConfig(level=logging.INFO)


async def run():

    drone = System()
    await drone.connect(system_address="udpin://0.0.0.0:14540")

    print("-- Starting gyroscope calibration")
    async for progress_data in drone.calibration.calibrate_gyro():
        print(progress_data)
    print("-- Gyroscope calibration finished")

    print("-- Starting accelerometer calibration")
    async for progress_data in drone.calibration.calibrate_accelerometer():
        print(progress_data)
    print("-- Accelerometer calibration finished")

    print("-- Starting magnetometer calibration")
    async for progress_data in drone.calibration.calibrate_magnetometer():
        print(progress_data)
    print("-- Magnetometer calibration finished")

    print("-- Starting board level horizon calibration")
    async for progress_data in drone.calibration.calibrate_level_horizon():
        print(progress_data)
    print("-- Board level calibration finished")


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
