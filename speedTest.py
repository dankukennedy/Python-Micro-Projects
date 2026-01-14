#!/usr/bin/env python3
"""
Internet Speed Test with Logging
"""

import speedtest
import time
from datetime import datetime


def test_internet_speed():
    """Test internet speed and return results"""
    try:
        st = speedtest.Speedtest()

        print("Finding optimal server...")
        st.get_best_server()

        print("Testing download speed...")
        download = st.download() / 1_000_000  # Convert to Mbps

        print("Testing upload speed...")
        upload = st.upload() / 1_000_000  # Convert to Mbps

        ping = st.results.ping

        return download, upload, ping

    except Exception as e:
        print(f"Error during speed test: {e}")
        return None, None, None


def log_to_file(download, upload, ping, filename="speedtest_log.txt"):
    """Log results to a file"""
    try:
        with open(filename, "a") as f:
            # Write a separator line
            f.write("="*60 + "\n")

            # Write timestamp
            current_time = time.ctime()
            f.write(f"Test Time: {current_time}\n")

            # Write results
            f.write(f"Download Speed: {download:.2f} Mbps\n")
            f.write(f"Upload Speed: {upload:.2f} Mbps\n")
            f.write(f"Ping/Latency: {ping:.2f} ms\n")

            # Write another separator
            f.write("="*60 + "\n\n")

        print(f"\nResults logged to: {filename}")

    except Exception as e:
        print(f"Error writing to file: {e}")


def display_results(download, upload, ping):
    """Display results in a formatted way"""
    print("\n" + "="*40)
    print("SPEED TEST RESULTS")
    print("="*40)
    print(f"Time: {time.ctime()}")
    print(f"Download Speed: {download:.2f} Mbps")
    print(f"Upload Speed: {upload:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")
    print("="*40)


def main():
    print("Starting Internet Speed Test...")
    print("Please wait, this may take up to a minute...\n")

    download, upload, ping = test_internet_speed()

    if download is not None and upload is not None and ping is not None:
        # Display results
        display_results(download, upload, ping)

        # Ask user if they want to log results
        choice = input("\nLog these results to a file? (y/n): ").lower()

        if choice in ['y', 'yes']:
            filename = input(
                "Enter filename (default: speedtest_log.txt): ")
            if not filename:
                filename = "speedtest_log.txt"

            log_to_file(download, upload, ping, filename)
    else:
        print("Failed to complete speed test. Please check your internet connection.")


if __name__ == "__main__":
    main()
