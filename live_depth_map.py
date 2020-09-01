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
    id = 1

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

            window_size = 0
            min_disp = -10
            max_disp = 35

            num_disp = (max_disp - min_disp)
            stereo = cv2.StereoSGBM_create(minDisparity=min_disp,
                                          numDisparities=num_disp,
                                          blockSize=2,
                                          uniquenessRatio=2,
                                          speckleWindowSize=2,
                                          speckleRange=2,
                                          disp12MaxDiff=1,
                                          P1=8 * 3 * window_size ** 2,  # 8*3*win_size**2,
                                          P2=32 * 3 * window_size ** 2)  # 32*3*win_size**2)

        

            disp = stereo.compute(limg, rimg).astype(np.float32) / 16.0
            cv2.imshow('disparity', (disp - min_disp) / num_disp)



        n = cv2.waitKey(1) & 0xFF
        # s keyboard character == save image
        if n == ord('s'):
            cv2.imwrite('undistortedleft'+str(id) + '.jpg',limg)
            cv2.imwrite('undistortedright' + str(id) + '.jpg',rimg)
            id = id+1
        #n keyboard character == exit cameras
        if n == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
