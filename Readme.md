For (1) 
For all the images:
1. python transform_example.py --image images/example_01.png --coords "[(73, 239), (356, 117), (475, 265), (187, 443)]"
2. python transform_example.py --image images/example_02.png --coords "[(101, 185), (393, 151), (479, 323), (187, 441)]"
3. python transform_example.py --image images/example_03.png --coords "[(63, 242), (291, 110), (361, 252), (78, 386)]"

* This is only for testing. The end goal is to get the points automatically.
* Also, USE THE PROPER RELATIVE PATH. Trust me, otherwise you get this error

```
Traceback (most recent call last):
  File "transform.py", line 63, in <module>
    warped = four_point_transform(image , pts)
  File "transform.py", line 44, in four_point_transform
    warped = cv2.warpPerspective(image , M , (maxw , maxh))
cv2.error: OpenCV(4.1.1) /io/opencv/modules/imgproc/src/imgwarp.cpp:2886: error: (-215:Assertion failed) _src.total() > 0 in function 'warpPerspective'
```