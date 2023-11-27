import vt
import time

#4th
api_key = 'API_KEY'

# Initialize the VirusTotal client
client = vt.Client(api_key)

# Open the file containing URLs
with open("D:/2023/Research/vtURLFull.txt", "r") as f:
    arr = f.read().splitlines()
i = 0

# Open a file to append to called vtResults
with open("D:/2023/Research/vtResults.txt", "a", encoding='utf-8') as f:
    for urlWeb in arr:
        url_id = vt.url_id(urlWeb)

        try:
            url = client.get_object("/urls/{}", url_id)            
            
            # Check if 'malicious' and/or 'suspicious' is greater than 0
            if url.last_analysis_stats['malicious'] > 0 or url.last_analysis_stats['suspicious'] > 0:
                f.write(f"URL: {url.url}\n")
                f.write(f"Last analysis date: {url.last_analysis_date}\n")
                f.write(f"Last analysis results: {url.last_analysis_results}\n")
                f.write(f"Last analysis stats: {url.last_analysis_stats}\n")
                f.write(f"Last final URL: {url.last_final_url}\n")
                f.write(f"Last submission date: {url.last_submission_date}\n")
                f.write(f"Categories: {url.categories}\n")
                f.write(f"\n")

            else:
                print(f"URL: {url.url} is not malicious or suspicious\n")
                
            
            time.sleep(0.5)


        except vt.APIError as e:
            print(f"Error retrieving URL information: {e}")
            print(f"URL: {urlWeb}\n")

            # Print to the file the urlWeb that caused the error
            f.write(f"URL: {urlWeb}\n")
            f.write(f"Error retrieving URL information: {e}\n")
            time.sleep(2)

            # If the error contains quota exceeeded, stop the program
            if "Quota exceeded" in str(e):
                print("Quota exceeded")
                break

        #Print new line
        print("i = ", i)
        i = i + 1

# Close the client session
client.close()
