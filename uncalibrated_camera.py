import cv2

def main():

    cap = cv2.VideoCapture(1)
    id = 1
    while(True):

        ret, frame = cap.read()
        height, width, channel = frame.shape
        left = frame[:, :int(width/2), :]
        right = frame[:, int(width/2):, :]

        cv2.imshow('loft', left)
        cv2.imshow('roght', right)

        n = cv2.waitKey(1) & 0xFF
        if n == ord('s'):
            cv2.imwrite('left'+str(id) + '.jpg',left)
            cv2.imwrite('right' + str(id) + '.jpg',right)
            id = id +1
        if n == ord('q'):
            break



    cap.release()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
