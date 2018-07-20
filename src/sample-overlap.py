import cv2
l_img = cv2.imread("large.png")
s_img = cv2.imread("happy.jpeg")
x_offset=y_offset=500
#l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
l_img[]
cv2.imshow('dst_rt', l_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#small_image.copyTo(big_image(cv::Rect(x,y,small_image.cols, small_image.rows)));
