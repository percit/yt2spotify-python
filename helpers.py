import sys

def readArgs():
    yt_client_id = str(sys.argv[1])
    yt_client_secret = str(sys.argv[2])
    channel_id = str(sys.argv[3])
    spotify_client_id = str(sys.argv[4])
    spotify_client_secret = str(sys.argv[5])
    return yt_client_id, yt_client_secret, channel_id, spotify_client_id, spotify_client_secret
    