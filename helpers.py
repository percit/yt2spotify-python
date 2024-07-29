import sys

def readArgs():
    yt_client_id = str(sys.argv[1])
    yt_client_secret = str(sys.argv[2])
    channel_id = str(sys.argv[3])
    spotify_client_id = str(sys.argv[4])
    spotify_client_secret = str(sys.argv[5])
    spotify_playlist = str(sys.argv[6])
    return yt_client_id, yt_client_secret, channel_id, spotify_client_id, spotify_client_secret, spotify_playlist
    
def get_integer_input(prompt: str):
    while True:
        try:
            user_input = input(prompt)
            value = int(user_input)
            if 0 <= value <= 10:
                return value
            else: 
                print("Value must be from 0 to 10")
        except ValueError:
            print("Invalid input, number must be from 0 to 10")
