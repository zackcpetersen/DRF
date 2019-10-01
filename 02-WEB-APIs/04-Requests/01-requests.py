import requests

def main():
    response = requests.get("https://api.exchangeratesapi.io/latest")
    if response.status_code != 200:
        print(response.status_code)
        raise Exception("There was an error")

    # print("response text: ", response.headers["Content-Type"])
    data = response.json()
    print("data: ", data)


if __name__ == "__main__":
    main()