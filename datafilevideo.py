def video():
    import pafy
    import cv2
    url = 'https://www.youtube.com/watch?v=ixEeeNjjOJ0'
    vPafy = pafy.new(url)
    play = vPafy.getbest(preftype="mp4")

    #start the video
    cap = cv2.VideoCapture(play.url)
    while (True):
        ret,frame = cap.read()
        """
        your code here
        """
        cv2.imshow('TUTORIAL ',frame)
        if cv2.waitKey(20) & 0xFF == ord('t'):
            break    

    cap.release()
    cv2.destroyAllWindows()
