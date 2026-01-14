
import time

def main():
    try:
        # Import inside try block to catch import errors
        import speedtest

        print("Starting speed test...")
        print("Please wait, this may take a minute...")

        # Initialize Speedtest
        st = speedtest.Speedtest()
                # Get best server
        print("\nFinding optimal server...")
        st.get_best_server()

        # Test download speed
        print("Testing download speed...")
        download = st.download() / 1_000_000  # Convert to Mbps
        print(f"✓ Download: {download:.2f} Mbps")

        # Test upload speed
        print("Testing upload speed...")
        upload = st.upload() / 1_000_000  # Convert to Mbps
        print(f"✓ Upload: {upload:.2f} Mbps")

        # Get ping
        ping = st.results.ping
        print(f"✓ Ping: {ping:.2f} ms")

        # Write in to File
        with open("speed_log.txt","a") as f:
            f.write(
                f"Access Time-{time.ctime()}, Download-{download:.2f}Mbps, Upload-{upload:.2f}Mbps, Ping-{ping:.2f}Ms")

        # Display summary
        print("\n" + "="*40)
        print("SPEED TEST RESULTS:")
        print("="*40)
        print(f"Download Speed: {download:.2f} Mbps")
        print(f"Upload Speed: {upload:.2f} Mbps")
        print(f"Latency (Ping): {ping:.2f} ms")
        print("="*40)

    except ImportError as e:
        print(f"Import Error: {e}")
        print("\nPlease install the required package:")
        print("pip install speedtest-cli")
    except speedtest.ConfigRetrievalError:
        print("Error: Could not connect to speedtest servers.")
        print("Please check your internet connection.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()