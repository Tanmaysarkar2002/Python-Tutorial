def img():
    import cv2
    while True:
        img=cv2.imread('python-search-and-sorting-exercise-1.png',cv2.IMREAD_GRAYSCALE)
        cv2.imshow('image',img)
        if cv2.waitKey(20) & 0xFF == ord('t'):
                break    
    cv2.destroyAllWindows()
