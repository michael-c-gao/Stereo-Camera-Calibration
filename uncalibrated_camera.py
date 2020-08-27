import cv2

def main():

    vid = cv2.VideoCapture(1)
    vid.set(3, 1920)
    vid.set(4, 1080)
    id = 1
    while(True):

        ret, frame = vid.read()
        height, width, channel = frame.shape
        left = frame[:, :int(width/2), :]
        right = frame[:, int(width/2):, :]

        cv2.imshow('left', left)
        cv2.imshow('right', right)

        n = cv2.waitKey(1) & 0xFF
        if n == ord('s'):
            cv2.imwrite('left'+str(id) + '.jpg',left)
            cv2.imwrite('right' + str(id) + '.jpg',right)
            id = id +1
        if n == ord('q'):
            break



    vid.release()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
