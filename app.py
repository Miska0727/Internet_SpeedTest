import streamlit as st
import speedtest
import time

def get_speed():
    with st.spinner("Testing internet speed..."):
        # Create Speedtest object
        st_obj = speedtest.Speedtest()

        # Get download and upload speeds
        download_speed = st_obj.download()
        upload_speed = st_obj.upload()

        # Convert speeds to Mbps
        download_speed_mbps = download_speed / 10**6
        upload_speed_mbps = upload_speed / 10**6

        # Simulate delay for animation effect
        time.sleep(2)

    # Display results
    st.success("Speed Test Complete!")
    st.write(f"Download Speed: {download_speed_mbps:.2f} Mbps")
    st.write(f"Upload Speed: {upload_speed_mbps:.2f} Mbps")

def main():
    st.title("Internet Speed Test App")

    if st.button("Run Speed Test"):
        get_speed()

if __name__ == "__main__":
    main()
