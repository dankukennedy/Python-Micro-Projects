import time
import os


def main():
    try:
        import speedtest

        print("Starting speed test...")
        print("Please wait, this may take a minute...")

        # Initialize and run tests
        st = speedtest.Speedtest()
        print("\nFinding optimal server...")
        st.get_best_server()

        print("Testing download speed...")
        download = st.download() / 1_000_000

        print("Testing upload speed...")
        upload = st.upload() / 1_000_000

        ping = st.results.ping

        # Display results
        results = f"""
            {'='*40}
            SPEED TEST RESULTS:
            Accessed Time: {time.ctime()}
            Download: {download:.2f} Mbps
            Upload: {upload:.2f} Mbps
            Ping: {ping:.2f} ms
            {'='*40}
            """
        print(results)

        # Ask to save
        save = input("\nSave results to file? (y/n): ").strip().lower()

        if save in ['y', 'yes']:
            filename = input("Filename (default: speedtest_log.txt): ").strip()
            if not filename:
                filename = "speedtest_log.txt"

            # Only create directory if filename contains a path
            dir_name = os.path.dirname(filename)
            if dir_name:  # Only create directory if it's not empty
                os.makedirs(dir_name, exist_ok=True)

            with open(filename, 'a', encoding='utf-8') as f:
                f.write(results)
            print(f"✓ Results saved to {os.path.abspath(filename)}")

    except ImportError:
        print("ERROR: speedtest-cli not installed!")
        print("Install it with: pip install speedtest-cli")
    except KeyboardInterrupt:
        print("\n\nTest cancelled by user.")
    except Exception as e:
        print(f"ERROR: {e}")
        print("Make sure you're connected to the internet.")


if __name__ == "__main__":
    main()
