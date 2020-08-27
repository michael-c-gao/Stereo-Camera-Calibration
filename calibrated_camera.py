import cv2
import numpy as np
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

def main():
    #call camera
    vid = cv2.VideoCapture(1)
    vid.set(3, 1920)
    vid.set(4, 1080)
    #load fundamentral matrix data
    data = np.load('stereocamera.npz')
    mtx1 = data['mat1']
    dist1 = data['dist1']
    mtx2 = data['mat2']
    dist2 = data['dist2']
    photo_ctr = 1
    count = 0
    while True:

        ret, frame = vid.read()


        if ret:
            #initial camera settings
            height, width, channel = frame.shape
            left = frame[:, :int(width / 2), :]
            right = frame[:, int(width / 2):, :]

            #undistort camera
            limg = cv2.undistort(left, mtx1, dist1, None)
            rimg = cv2.undistort(right, mtx2, dist2, None)

            #display stacked images
            #cv2.imshow('img', np.vstack((frame,np.hstack((limg, rimg)))))
            #count = count + 1

            #display images
            cv2.imshow('left', limg)
            cv2.imshow('right', rimg)




            n=cv2.waitKey(1) & 0xFF
            # s keyboard character == save image
            if n == ord('s'):
                cv2.imwrite('undistortedleft'+str(id) + '.jpg',limg)
                cv2.imwrite('undistortedright' + str(id) + '.jpg',rimg)
                photo_ctr =  photo_ctr +1
            #n keyboard character == exit cameras
            if n == ord('q'):
                break



    vid.release()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
