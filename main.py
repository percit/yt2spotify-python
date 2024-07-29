import helpers
import yt_api
import spotify_api

def main():
    yt_client_id, yt_client_secret, channel_id, spotify_client_id, spotify_client_secret = helpers.readArgs()

    # client = yt_auth.do_authorize(yt_client_id, yt_client_secret) 
    # this may not work now, because it takes time to change redirect uri in google console
    # yt_auth.download_playlist(client, channel_id)


    print("hello world")







if __name__ == "__main__": 
    main()